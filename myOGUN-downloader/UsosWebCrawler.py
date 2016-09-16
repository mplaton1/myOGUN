"""
Web crawler for grabbing data about OGUNs from
Usos web page and saving them into database.
"""
import re
from http.client import RemoteDisconnected
from typing import Dict, List
from urllib import parse, error, request

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .BaseWebCrawler import BaseWebCrawler
from .OGUN import OGUN, Base
from .utils import get_base_url


class UsosWebCrawler(BaseWebCrawler):
    """
    Class for web crawler gathering data from Usos.
    Entry point is visit_all_links function, inherited from BaseWebCrawler.
    """
    def __init__(self, domain=None):
        super().__init__()
        self.domain = domain
        self.data = []
        self.__engine__ = create_engine('sqlite:///usosOGUNData.sqlite')
        session = sessionmaker(bind=self.__engine__)
        self.__session__ = session()
        Base.metadata.create_all(self.__engine__)

    def __del__(self):
        self.__session__.close_all()

    _usosRegex = '\n\t\t[0-9]+'

    @staticmethod
    def _compose_url(url: str, link_data: List[str]) -> str:
        return url + '&' + parse.urlencode({'course_id': link_data[0], 'gr_no': link_data[1]})

    @staticmethod
    def _trim_data(matches_list: List[str]) -> List[str]:
        return list(map(lambda x: x[3:], matches_list))

    def memorize_data(self, link: str, data: Dict[str, str]) -> None:
        data['link'] = link
        ogun = OGUN.ogun_builder(data)

        if ogun.has_all_fields():
            self.__session__.add(ogun)
            self.__session__.commit()

    def want_to_visit_link(self, link: str):
        return True if self.domain is None else self.domain == get_base_url(link)

    @staticmethod
    def _process_row(row: BeautifulSoup) -> (str, str):
        try:
            row.td['class']
        except KeyError:
            pass
        else:
            if row.td['class'] == ["form_title"]:
                data_description = row.td.text
                try:
                    data_content = row.find_all('td')[1].text
                except IndexError:
                    data_content = None
                return data_description, data_content

    def retrieve_data(self, link: str) -> None:
        try:
            soup = BeautifulSoup(request.urlopen(link), "lxml")
            table = soup.body.find_all('table', {"class": "wrnav stretch"})[0]
        except (error.HTTPError, AttributeError, IndexError, RemoteDisconnected) as _:
            pass
        else:
            result = dict()
            for row in table.find_all('tr'):
                row_processing_result = UsosWebCrawler._process_row(row)
                if row_processing_result is not None:
                    result[row_processing_result[0]] = row_processing_result[1]
            if len(result) > 0:
                self.memorize_data(link, result)

    @staticmethod
    def get_links(link: str) -> List[str]:
        links = list(super(UsosWebCrawler, UsosWebCrawler).get_links(link))
        try:
            page_content = request.urlopen(link).read().decode('utf8')
            link_data = re.findall(UsosWebCrawler._usosRegex, page_content)
            links.append(UsosWebCrawler._compose_url(link, UsosWebCrawler._trim_data(link_data)))
        except (error.HTTPError, IndexError, RemoteDisconnected) as _:
            pass
        return links

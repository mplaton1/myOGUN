"""
Module for base web crawler.
"""
from abc import ABC, abstractmethod
from queue import Queue
from typing import Sequence, Any
from urllib import request, parse, error
from time import sleep
from http.client import RemoteDisconnected
from bs4 import BeautifulSoup
from . import utils


class BaseWebCrawler(ABC):
    """
    Base web crawler. Crawler provides two utilities:
    to visit one link and retrive data from it, or to
    continuously crawl links from a given starting url.
    Its behaviour can be further guided by want_to_visit_link
    method. If no special behaviour is need, this should return True.
    User of abstract class have to provide methods for retriving data
    and for memorizing it(if necessary).
    """
    def __init__(self, database=None):
        self.visited_pages = set()
        self.links_to_visit = Queue()
        self.scheduled_links = set()
        self.database = database

    def was_link_visited(self, link: str) -> bool:
        """
        This function informs whether web crawler has
        visited page.
        :param link
        :return: bool
        """
        return link in self.visited_pages

    @abstractmethod
    def retrieve_data(self, link: str) -> None:
        pass

    @abstractmethod
    def memorize_data(self, link: str, data: Any) -> None:
        pass

    def memorize_visited_link(self, link: str) -> None:
        """
        Memorizes that given link was visited by crawler
        :param link:
        :return: None
        """
        self.visited_pages.add(link)

    @abstractmethod
    def want_to_visit_link(self, link: str) -> bool:
        pass

    @staticmethod
    def get_links(link: str) -> Sequence[str]:
        """
        Returns a list of links accessible from given link.
        Empty list is returned, when link is invalid.
        :param link:
        :return: iterator of links on a given web page
        """
        try:
            response = request.urlopen(link)
        except (error.HTTPError, RemoteDisconnected) as _:
            return iter(())
        else:
            soup = BeautifulSoup(response, "html.parser",
                                 from_encoding=response.info().get_param('charset'))
            base_url = utils.get_base_url(link)
            return map(lambda x: parse.urljoin(base_url, x['href']), soup.find_all('a', href=True))

    def visit_link(self, link: str) -> None:
        if not self.was_link_visited(link):
            self.memorize_visited_link(link)
            self.retrieve_data(link)

            for url in self.get_links(link):
                if not self.was_link_visited(url) and self.want_to_visit_link(url) \
                        and url not in self.scheduled_links:
                    self.scheduled_links.add(url)
                    self.links_to_visit.put(url)

    def visit_all_links(self, link: str) -> None:
        if not self.want_to_visit_link(link):
            return None
        if self.was_link_visited(link):
            return None

        self.links_to_visit.put(link)

        while not self.links_to_visit.empty():
            sleep(2)
            url = self.links_to_visit.get()
            print(url)
            try:
                self.visit_link(url)
            except error.HTTPError as _:
                pass

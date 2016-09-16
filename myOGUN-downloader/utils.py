"""
Simple utilities for extracting data from usos webpage. Those include:
get_group_id, get_base_url, get_week_day, get_start_time, get_end_time.
"""
import urllib.parse


def get_base_url(url: str) -> str:
    """
    Argument must be a valid url. Returns base url.
    :param url: str
    :return: str
    """
    return "{0.scheme}://{0.netloc}/".format(urllib.parse.urlsplit(url))


def get_group_id(url: str) -> str:
    """
    Url must be valid. Returns group_id.
    :param url: str
    :return: str
    """
    try:
        query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        return query["group"][0].split("-")[1]
    except (IndexError, AttributeError, KeyError) as _:
        return None


def get_week_day(date: str) -> str:
    """
    Tries to scrape week_date from string given by crawler.
    Returns None on failure.
    :param date: str
    :return: str
    """
    try:
        return date.split()[0]
    except (IndexError, AttributeError) as _:
        return None


def get_start_time(date: str) -> str:
    """
    Tries to scrape time when lesson begins from string.
    Returns None on failure.
    :param date: str
    :return: str
    """
    try:
        return date.split()[1].split("-")[0]
    except (IndexError, AttributeError) as _:
        return None


def get_end_time(date: str) -> str:
    """
    Tries to scrape time when lesson ends from string.
    Returns None on failure.
    :param date: str
    :return: str
    """
    try:
        return date.split()[1].split("-")[1]
    except (IndexError, AttributeError) as _:
        return None

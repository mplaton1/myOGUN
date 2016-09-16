import unittest
from .BaseWebCrawler import BaseWebCrawler
from .UsosWebCrawler import UsosWebCrawler


class TestBaseWebCrawlerMethods(unittest.TestCase):
    web_crawler = None

    @classmethod
    def setUp(cls):
        BaseWebCrawler.__abstractmethods__ = set()
        TestBaseWebCrawlerMethods.web_crawler = BaseWebCrawler()

    def test_memorizing_visited_links(self):
        web_crawler = TestBaseWebCrawlerMethods.web_crawler

        link1 = "https://docs.python.org/2.7/library/unittest.html"
        link2 = "https://docs.python.org/3/library/typing.html"
        link3 = "http://www.diveinto.org/python3/strings.html"

        web_crawler.memorize_visited_link(link1)
        web_crawler.memorize_visited_link(link2)

        self.assertEqual(True, web_crawler.was_link_visited(link1), "Link was memorized!")
        self.assertEqual(True, web_crawler.was_link_visited(link2), "Link was memorized!")
        self.assertEqual(False, web_crawler.was_link_visited(link3), "Link was not memorized!")

    def test_getting_all_links(self):
        usos_web_crawler = UsosWebCrawler("http://rejestracja.usos.uw.edu.pl/")
        usos_web_crawler.visit_all_links("http://rejestracja.usos.uw.edu.pl/catalogue.php?rg=0000-2016-OG-UN")


if __name__ == '__main__':
    unittest.main()

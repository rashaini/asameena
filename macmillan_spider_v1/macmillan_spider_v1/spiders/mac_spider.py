from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from macmillan_spider_v1.items import MacmillanItem
from bs4 import BeautifulSoup


class MacmillanSpider(CrawlSpider):
    name = "macmillan"
    allowed_domains = ["macmillan.org.uk"]
    start_urls = [
        "https://www.macmillan.org.uk/",
    ]
    rules = [Rule(LinkExtractor(allow_domains=("macmillan.org.uk")), 'parse_story')]

    def parse_story(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        urls_list = []
        self.add_to_frontier(response.url, urls_list)
        result = MacmillanItem()
        result['url'] = response.url
        result['headline'] = response.xpath("//title/text()").extract()
        result['text'] = self.process_text(soup)

        return urls_list

        """ Uncomment to debug code and inspect loop"""

    # def add_to_frontier(self, url, myList):
    #     if url not in myList:
    #         myList.append(url)
    #     else:
    #         myList.append("already_in_list")

    #     return myList


    def process_text(self, soup):
        for s in soup(["script", "style"]):
            s.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line 
            in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)

        return text

    # if __name__ == '__main__':
    #     add_to_frontier()

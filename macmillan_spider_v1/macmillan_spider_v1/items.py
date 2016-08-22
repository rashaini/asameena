import scrapy
from scrapy.item import Item, Field


class MacmillanItem(scrapy.Item):
	headline = scrapy.Field()
	url = scrapy.Field()
	text = scrapy.Field()
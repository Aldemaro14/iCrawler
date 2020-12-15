# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallmartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    deliveryDate = scrapy.Field()
    pictures = scrapy.Field()
    description = scrapy.Field()
    variations = scrapy.Field()

class VariationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    label = scrapy.Field()
    availability = scrapy.Field()
    img = scrapy.Field()
    

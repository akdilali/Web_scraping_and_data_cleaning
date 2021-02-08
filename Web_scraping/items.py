# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titleRestaurant = scrapy.Field()
    adress = scrapy.Field()
    information = scrapy.Field()
    price = scrapy.Field()
    kitchens = scrapy.Field()
    special_types_of_diets = scrapy.Field()
    score = scrapy.Field()
    phoneNumber = scrapy.Field()
    number_of_comments = scrapy.Field()   

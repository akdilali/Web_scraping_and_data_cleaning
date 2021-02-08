import scrapy
import scrapy
from ..items import WebScrapingItem
from scrapy import Request
from urllib.parse import urlparse
from urllib.parse import urljoin


class ScrapingSpider(scrapy.Spider):
    name = 'scraping'
    #allowed_domains = ['https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html/']
    start_urls = ['https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html//']

    def parse(self, response):
        for href in response.css("._15_ydu6b::attr(href)").extract():
            url = response.urljoin(href)
            print(type(url))
            print(url)
            yield scrapy.Request(url, callback= self.parse_page)

        next_page = response.css("a.nav.next.rndBtn.ui_button.primary.taLnk::attr(href)").extract_first()
        next_page = f"https://www.tripadvisor.com.tr{next_page}"
        print(next_page)
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url= next_page_link, callback =self.parse) 

    def parse_page(self,response):
        item = WebScrapingItem()
        titleRestaurant= response.css("._3a1XQ88S::text").extract()
        adress=response.css("._15QfMZ2L::text").extract()
        information = response.css('._2mn01bsa::text').extract()
        price = response.css('._1XLfiSsv::text').extract_first()
        kitchens = response.css('._1XLfiSsv::text').extract()[1]
        special_types_of_diets = response.css('._1XLfiSsv::text').extract()[2]
        phoneNumber = response.css('span._2saB_OSe::text').extract()[3]
        score = response.css('span.r2Cf69qf::text').extract_first()
        number_of_comments = response.css('a._10Iv7dOs::text').extract_first()

        item['titleRestaurant'] = titleRestaurant  
        item['adress']=adress
        item["information"] = information
        item["price"] = price
        item["kitchens"] = kitchens
        item["special_types_of_diets"] = special_types_of_diets
        item["phoneNumber"] = phoneNumber
        item["score"] = score
        item["number_of_comments"] = number_of_comments

        yield item


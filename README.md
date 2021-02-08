# Web_scraping
 web scraping with python scrapy 

# Install scrapy

conda install -c conda-forge scrapy or pip install Scrapy 

# Proje oluşturma

scrapy startproject example 

# Spider oluşturma

scrapy genspider example2 https://www.website.com 

# Spider çalıştırma

scrapy crawl example2 

scrapy crawl Spidername -o Output.json

setting.py dosyasına çıkışta istenen dosya türü eklenebilir.

FEED_FORMAT = "csv"

FEED_URI = "Scraping.csv"

# Alınacak verileri bulmak için scrapy shell'de deneme yapılır

scrapy shell https://www.website.com

scrapy shell https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html/

fetch("https://www.website.com")

fetch("https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html/")

istenen dataları bulmak için css selector veya xpath kullanılabilir

response.css("._3a1XQ88S::text").extract() 
response.xpath('//p/strong/text()').extract()
#extra

print response.text  (website kaynak kodları)


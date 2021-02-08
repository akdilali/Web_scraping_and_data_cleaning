# Web_scraping
 web scraping with python scrapy 

#install scrapy
conda install -c conda-forge scrapy or pip install Scrapy 

#create scrapy project
scrapy startproject example 

#create spider
scrapy genspider example2 https://www.website.com 

#run spider
scrapy crawl example2 
scrapy crawl Spidername -o Output.json






#try to find data

scrapy shell https://www.website.com

scrapy shell https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html/

fetch("https://www.website.com")

fetch("https://www.tripadvisor.com.tr/Restaurants-g293974-Istanbul.html/")

response.css("._3a1XQ88S::text").extract() (find specific data)

#extra
view(response) (open website)
print response.text  (website source code)
exit = exit scrapy shell

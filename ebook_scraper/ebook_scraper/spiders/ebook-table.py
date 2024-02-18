import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader
from urllib.parse import urljoin


class EbookSpider(scrapy.Spider):
  name = "ebook-table"
  start_urls = ["https://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html"]

    
  def parse(self, response):
    table = response.css("table")
    product_details= {}
    for row in table.css("tr"):
      heading = row.css("th::text").get()
      data = row.css("td::text").get()
      
      product_details[heading] = data
      yield product_details


from typing import Iterable
import scrapy

class EbookSpider(scrapy.Spider):
  name = "ebook-login"
  
  def start_requests(self) :
    yield scrapy.FormRequest(
      "https://www.scrapethissite.com/pages/advanced/?gotcha=login", 
       formdata={
                 "user" : "Kyle", 
                 "pass":"really_strong"
                  },
                  callback = self.parse)
  
  
  def parse(self, response):
    print("Result",
      response.css("div.container div div::text").get())
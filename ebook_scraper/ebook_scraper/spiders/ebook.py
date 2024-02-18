from typing import Iterable
import scrapy

class EbookSpider(scrapy.Spider):
  name = "ebook"
  start_urls = ["http://www.scrapethissite.com/pages/advanced/?gotcha=csrf"]
  
  
  def parse(self, response):
    csrf_token = response.css("input[name='csrf']").attrib["value"]
    print("CSRF", csrf_token)
    yield scrapy.FormRequest(
      "http://www.scrapethissite.com/pages/advanced/?gotcha=csrf",
      formdata={
        "user":"John",
        "pass" : "strong",
        "csrf" : csrf_token
      },
      callback = self.parse_login)
    
  def parse_login(self, response):
    print("RESULT", response.css("div.row div::text").get().strip())
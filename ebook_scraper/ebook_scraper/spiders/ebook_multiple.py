import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader
from urllib.parse import urljoin


class EbookSpider(scrapy.Spider):
  name = "ebook-multiple"
  start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3"]
  cols = ["Title", "Price"]
  
  def __init__(self):
    super().__init__()
    self.page_count = 0
    self.total_pages =4
  
  
  #MULTIPLE PAGES
  def start_requests(self):
    base_url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5'
    
    while self.page_count <= self.total_pages:
      yield scrapy.Request(
        f"{base_url}/page-{self.page_count}.html"
      )
      self.page_count+=1
    
  def parse(self, response):
    # self.page_count+=1
    ebooks = response.css("article.product_pod")
    for ebook in ebooks:
      loader  = ItemLoader(item=EbookItem(), selector= ebook)
      loader.add_css("title", "h3 a::attr(title)")
      loader.add_css("price","p.price_color::text")
      yield loader.load_item()
    
  
 
    
    ### PAGINATION
    # print("[PAGE COUNT]:" , self.page_count)
    
    # next_btn   = response.css("li.next a")
    # if next_btn: 
    #   next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"
    #   print(next_page)
    #   yield scrapy.Request(url=next_page)

      
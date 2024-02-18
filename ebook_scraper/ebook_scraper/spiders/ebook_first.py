import scrapy

class EbookSpider(scrapy.Spider):
  name = "ebook_first"
  start_urls = ["https://books.toscrape.com/"]
  
  def parse(self, response):
    print("our response")
    # ebooks = response.css("article")
    # for ebook in ebooks:
    #   title = ebook.css("a::text").get()
    #   price = ebook.css("p.price_color::text").get()
    #   yield {"title":title, "price": price}
    
    # response.xpath("//h3/a/text()")
    # response.css(".price_color::text").get()
    # response.css("#messages").get()
    # response.css("a[title]").get()
    # response.css("a[title ='Soumission']")
    
    response.xpath("//a[@title]").get()
    response.xpath("//p[@class = 'price_color]").get()
    response.xpath("//h3/a/text()").get()
    response.xpath("//h3/a/@title").get()
    
    
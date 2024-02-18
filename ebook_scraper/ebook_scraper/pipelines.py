# from openpyxl import Workbook
# from pymongo import MongoClient
from itemadapter import ItemAdapter

class EbookScraperPipeline:
    def open_spider(self,spider):
      pass
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print(f"Processed Item - Title: {adapter['title']}, Price: {adapter['price']}")
        return item
    
    def close_spider(self, spider):
       pass
        
    
#### MONGODB 

#  class EbookScraperPipeline:
#     def open_spider(self,spider):
#         self.client = MongoClient(
#             host="mongodb+srv://sioanaseres:EEpD5uL1VPwjfm7j@cluster0.ze6xdy8.mongodb.net/?retryWrites=true&w=majority" ,
#             connect= False
#         )
#         self.collection = self.client.get_database("ebooks").get_collection("travel")
    
#     def process_item(self, item, spider):
#         item_dict = {
#              "title":item["title"],
#              "price" : item["price"]
#              }
    
#         # self.collection.insert_one(
#         #    ItemAdapter(item).asdict()
#         #    )
        
#         self.collection.insert_one(item_dict)
#         return item
    
#     def close_spider(self, spider):
#         self.client.close()
#### EXCEL

# class EbookScraperPipeline:
#     def open_spider(self, spider):
#         self.workbook = Workbook()
#         self.sheet = self.workbook.active
#         self.sheet.title = 'ebooks'
#         self.sheet.append(spider.cols)
    
#     def process_item(self, item, spider):
#         self.sheet.append([item["title"], item["price"]])

#     def close_spider(self, spider):
#         self.workbook.save("ebooks.xlsx")
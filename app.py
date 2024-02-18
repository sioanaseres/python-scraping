from tkinter import Tk, ttk
from scrapy.crawler import CrawlerProcess
from tracker import TrackerSpider

root = Tk()
root.title("Tracker")
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)
lbl = ttk.Label(frame, text="Search")
lbl.grid(row=0, column=0, padx=(0, 10))

keyword = ttk.Entry(frame)
keyword.grid(row = 0, column=1)

def run_spider():
  TrackerSpider.query = keyword.get()
  crawler = CrawlerProcess()
  crawler.crawl(TrackerSpider)
  crawler.start()
  
  
btn = ttk.Button(frame, text = "Run", command=run_spider)
btn.grid(row=1, column=0, pady=10, columnspan=2)
root.mainloop()

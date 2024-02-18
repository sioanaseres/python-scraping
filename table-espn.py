import scrapy

def fifth(lst):
   start = 0
   end = 5
   
   while end <= len(lst):
       yield lst[start:end]
       start +=5
       end +=5

class TableSpider(scrapy.Spider):
    name = "table"
    start_urls = ["https://www.espn.com/football/table/_/league/UEFA.CHAMPIONS/season/2021"]

    def parse(self, response):
        dt={}
        
        team_rows = response.css("table")[0].css("tr")
        details_rows = response.css("table")[1].css("tr")
        
        for group, group_detail in zip(fifth(team_rows), fifth(details_rows)):
            group_label = group[0].css("td span::text").get()
            
            dt[group_label] = {}
            
            for team, detail in zip(group[1:], group_detail[1:]):
                team_label = team.css("td span.hide-mobile a::text").get()
                tabel_details = detail.css("td span::text").getall()
                dt[group_label][team_label] = {
                    "wins" : tabel_details[1],
                    "draws" : tabel_details[2],
                    "loses" : tabel_details[3],
                    "points" : tabel_details[-1]
                }
        
        yield dt

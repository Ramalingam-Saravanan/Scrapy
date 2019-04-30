import scrapy
from scrapy.http import Request
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
from scrapy.item import Item, Field
import csv



class mastercard(scrapy.Spider):
    
    name = "mastercard_jobs"
  
    #start_request(inbuilt method) to get the main url to scrap       
    def start_requests(self):
        #opening a predifined urls for scrapping
        with open('jpmorghan_india.csv','r') as f:
            #opening the file using dict reader
            reader = csv.DictReader(f)
            for line in reader:
                #obtaining request using line.pop from the csv file
                request = Request(line.pop('url'))
                #placing request to scrape 
                yield request
       
                

    #parse(inbuilt method)    
    def	parse(self,	response):
            #opening the file and reading to get the xpath 
            reader = open('mastercard_india.csv','r')
            reader = csv.DictReader(reader)
            
            for line in reader:			
                urls=line.pop('url')
                #storing href attribute to go to the next page
                next_selector =	response.xpath(line.pop('nextpage_href')) 
                #extracting each href attribute and passing it to urljoin()
                for href in	next_selector.extract():
                    
                    #placing request ,getting main url by using urljoin 
                    request = Request(urljoin(response.url,href),callback=self.parse_item )
                    #assigning the line in csv to meta
                    request.meta['fields'] = line
                    yield request
                    #placing  request                            						
    def parse_item(self,response):
            #it has the response of joined url
            item = Item ()
            # manually declaring an item which has ordered dict format
            l = ItemLoader(item=item, response=response)
            
            for name,xpath in response.meta['fields'].items():
                #first row of a csv file will be treated as name and following rows as xpath
                if xpath:
                    #intializing the item fields manually
                    item.fields[name] = Field()
                    #adding an xpath to itemloader to obtain final result 
                    l.add_xpath(name,xpath)
                    
                #populating an item which has final response
            return l.load_item()
                #returns a dict format with headers and the scraped results
        
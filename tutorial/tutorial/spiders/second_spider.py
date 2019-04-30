# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 07:41:35 2019

@author: hash
"""

import csv 
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.item import Item, Field
from urllib.parse import urljoin





class	FromcsvSpider(scrapy.Spider):				
    
    name = "fine"
  
      
    
    
    def	start_requests(self):
        
            #declaring line in csv as  global
          
                request = Request('https://jobs.jpmorganchase.com/ListJobs/ByCountry/IN/Page-2')
                																									
                yield request 
                
                
                
   
    def	parse(self,	response):
        
        print('a')
        print(response.xpath('//*[@id="job-list"]/div/div[2]/table/tbody/tr[3]/td[2]/a'))
    '''
    def parse(self, response):
        item = Item ()
        l = ItemLoader(item=item, response=response)
        for name,xpath in response.meta['fields'].items():
            if xpath:
                #intializing the item fields manually
                item.fields[name] = Field()
                #adding an xpath to itemloader to obtain final result 
                l.add_xpath(name,xpath)
        url = l.load_item()
        for link in url['xpath']:
            req= urljoin(response.url,link)
            self.writer.writerow({'first_name': req})
          
            
       
        
            
     
    
        '''
    '''    
       my=[]
       request = response.xpath('//*[@id="button_moreJobs"]/@href').extract()
       fine1 = Request(request)
       yield fine1
       https://mastercard.jobs/jobs/ajax/joblisting/?location=india&num_items=15&offset=45
       print(fine1)
       b= response.meta['fields'].items()
       print(b)
       for name,xpath in response.meta['fields'].items():
           a = response.xpath(xpath)
       for url in a.extract():
           request = urljoin(response.url,url)
           my.append(request)
       print(my)
      
       with open("outputre.csv", "w") as f:
           writer = csv.DictWriter(f,fieldnames = ["url"])
           writer.writeheader()
           for item in my:
               writer.writerow([item])
           f.close()
 
          
           
               #if xpath:
               #nex[name] = response.xpath(xpath) 
                  # for	url	in	next_selector.extract():
                  # request = urljoin(response.url,url)
                   #print(request)
        
        item = Item()				
        l = ItemLoader(item=item,response=response)				
        for	name,xpath	in	response.meta['fields'].items():								
            if	xpath:	
                item.fields[name]	=	Field()																				
                l.add_xpath(name,xpath)
        urls = l.load_item()	
        for url in urls.extract():
            a=urljoin(response.url,url)
        print(a)
       
        '''
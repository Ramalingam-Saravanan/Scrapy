'''import scrapy
import logging
from ford.items import jobItem
class fordspider(scrapy.Spider):
    name='ford_jobs'
    start_urls=[
        'https://sjobs.brassring.com/TGWebHost/home.aspx?partnerid=25385&siteid=5283'
        ]
    def parse(self,response):
        jobs_india_Homepage=response.xpath('//span[@id="ctl00_MainContent_spnNonLoginLandingPageCustomText"]//a/@href').extract_first()
        print('Hello')
        print(jobs_india_Homepage)
        jobs_india=response.follow(jobs_india_Homepage)  #Couldnt click on a link.. 
        #jobs_india_req=scrapy.Request(url=jobs_india)
        a=response.xpath("//a[starts-with(@id,'viewjobdetails')]/@href").extract()
        print(a) #Getting Empty List
        
        for jobid in a :
            print('inside for loopp')
            print(jobid)
            job_description=response.follow(jobid)
            items= jobItem()

            jobdesc=response.xpath('Job_desc',"//span[@id='Job Description & Qualifications']").extract()
            items['Job_desc']=jobdesc
            yield items
            search_results=response.xpath("//a[@id='Search__results']/@href")
            response.follow(search_results)'''
          
          
'''for joke in response.xpath("//div[@class='jokes']"):
            l=ItemLoader(item=JokeItem(),selector=joke)
            l.add_xpath('joke_anytext',".//div[@class='joke-text']/p")
            yield l.load_item()
        
        next_page=response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)'''
            
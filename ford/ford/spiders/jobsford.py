import scrapy
import re, json
from ford.items import jobItem
class ford(scrapy.Spider):
    name='jobs'
    start_urls=[
        'https://sjobs.brassring.com/TGWebHost/home.aspx?partnerid=25385&siteid=5283'
        ]
    def parse(self, response):
         jobs_india_Homepage=response.xpath("//span[@id='ctl00_MainContent_spnNonLoginLandingPageCustomText']//a/@href").extract_first()
         yield response.follow(jobs_india_Homepage, self.parse_homepage)
         
    def parse_homepage(self, response):
        #a=response.xpath("//table//tbody[@class='yui-dt-data']//a/@href").extract()
        #a=response.xpath("//a[@id='viewjobdetails0']").extract()
        #a=response.xpath("//h1[@class='PAGEtitle h1Title']/span/text()").extract()
        #a=response.xpath("//tbody[@id='idSearchresults_dataBody']").extract()
        #a=response.xpath("//table[@title='Search results']").extract()
        a=response.xpath("//table[@title='Search results']//input[@id='ctl00_MainContent_GridFormatter_json_tabledata']/@value").extract()
        #a=response.xpath("//table[@id='idSearchresults']").extract()
        #a=response.xpath("//table[4]//a[starts-with(@id,'viewjobdetails')]/@href").extract()
        
        print("Hai homepage")
        print(a)
        
        
        items= jobItem()
        items['Job_desc']=a
        yield items
        
        '''for jobid in a:
            yield response.follow(jobid, self.parse_jobdesc)
            
    def parse_jobdesc(self,response):
        items= jobItem()

        jobdesc=response.xpath('Job_desc',"//span[@id='Job Description & Qualifications']").extract()
        items['Job_desc']=jobdesc
        yield items'''

import scrapy
import re
import json
from w3lib.html import remove_tags
from scrapy.http import Request
import mechanize

class jsonford(scrapy.Spider):
    def __init__(self):
        #self.br = mechanize.Browser()
        self.numJobsSeen = 0
        self.br=mechanize.Browser()
        

    name='job1'
    start_urls=[
        'https://sjobs.brassring.com/TGWebHost/home.aspx?partnerid=25385&siteid=5283'
        ]
    
    def parse(self, response):
         jobs_india_Homepage=response.xpath("//span[@id='ctl00_MainContent_spnNonLoginLandingPageCustomText']//a/@href").extract_first()
         yield response.follow(jobs_india_Homepage, self.parse_homepage)
         
    def parse_homepage(self, response):
         a=response.xpath("//table[@title='Search results']//input[@id='ctl00_MainContent_GridFormatter_json_tabledata']/@value").extract_first()
         print("Hai homepage")
         #print(a)
         k=json.loads(a)
         #j=k["value"]
         for x in k:
               
                #Creating a Dictionary to store values
                job = {}
                job['Job_ID'] = self.get_Joburl_from_job_dict(x)
                job['Company_Name'] = self.get_companyname_from_job_dict(x)
                job['Job_Title'] = self.get_JobTitle_from_job_dict(x)
                job['Skills'] = self.get_title_from_job_dict(x)
                job['location'] = self.get_location_from_job_dict(x)
                job['Positions_Remaining'] = self.get_PositionsRemaining_from_job_dict(x)
                job['LastUpdated'] = self.get_LastUpdated_from_job_dict(x)
                
                
                
                
                yield job
                
         
         
         
         self.numJobsSeen += len(k)
         
         print(self.numJobsSeen)
         jobseen=self.numJobsSeen+1
         self.Jobdesc_Url()
         self.jobDescription_scrape() 
         
         #b=response.xpath("//a[@class='yui-pg-next']").extract_first()
         #print(b)
         
         #scrapy.FormRequest.from_response(response,formname="frmMassSelect",
                                               #formdata={'recordstart':jobseen},callback=self.parse_homepage)
         #print(resp)
         #formdata={'recordstart':jobseen}
         #r=resp.meta(formdata['recordstart'])
         #print(r)
         #self.parse_next_page(response.url)
         #self.goto_next_page()
         
         
                
    def get_title_from_job_dict(self, job_dict):
        t = job_dict['FORMTEXT19']
        return t
        
    def get_PositionsRemaining_from_job_dict(self, job_dict):
        t = job_dict['PositionsRemaining']    
       
        return t
    def get_location_from_job_dict(self, job_dict):
        l = job_dict['FORMTEXT12'] + ', ' + job_dict['FORMTEXT7']
        l = l.strip()
        return l
    def get_companyname_from_job_dict(self, job_dict):
        t = job_dict['FORMTEXT8']
        return t
                
    def get_JobTitle_from_job_dict(self, job_dict):
        t = job_dict['JobTitle']
        return t
    def get_LastUpdated_from_job_dict(self, job_dict):
        t = job_dict['LastUpdated']
        t= remove_tags(t).strip()
        
        return t
    
    def get_Joburl_from_job_dict(self, job_dict):
        t = job_dict['AutoReq']
        jobid=re.search("(?:jobId\=)[0-9]*",t)
        jobid=jobid.group()
        self.jobidlist.append(jobid)
        #print("jobidfind")
        #print(self.jobidlist)
        t= remove_tags(t).strip()
        
        return t
    
    def Jobdesc_Url(self):
        for x in self.jobidlist:
             descUrl=self.modified_url +'&' + x
             self.jobdescUrl.append(descUrl)
        return     
        
    def jobDescription_scrape(self):
          for x in self.jobdescUrl:
            linkss=x
            print(linkss)
            yield scrapy.Request(url=linkss,callback=self.descrip)
            
            
              
    def descrip(self,response):
        b=response.xpath("//span[@id='Job Description & Qualifications']").extract_first()
        print("description")
        print(b)
        return b
        
    #try    
    '''def seen_all_jobs(self):
        
        self.br.select_form('frmMassSelect')
        return self.numJobsSeen >= int(self.br.form['totalrecords'])'''

    '''def goto_next_page(self):
        print("Inside mechanize")
        self.br.select_form('frmMassSelect')
        print("form selection")
        self.br.form.set_all_readonly(False)
        self.br.form['recordstart'] = '%d' % (self.numJobsSeen + 1)
        self.br.submit()
        readresponse=self.br.response().read()       
        return readresponse'''
    
    '''def parse_next_page(self,response):
        print("Inside Funcgion")
        print(response)
        jobseen=self.numJobsSeen+1
        #formdata=json.loads(frmMassSelect)
        ass=scrapy.FormRequest.from_response(response.encoding, method = 'POST',formname="frmMassSelect",
                                               formdata={'recordstart':jobseen},callback=self.parse_homepage)'''
         

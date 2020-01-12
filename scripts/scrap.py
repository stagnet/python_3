import scrapy

class DevMedical_Spider(scrapy.Spider): #! every spider is basically a class...
    # *identify
    name = '2019_laptops'

    # *Requests
    def start_requests(self):
        urls = [
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=1',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=2',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=3',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=4',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=5',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=6',
            'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india?page=7',
            
        ]
        for url in urls:

            yield scrapy.Request(url= url,callback= self.parse)

    # *Response  
    def parse(self, response):
        page_name = response.url.split('=')[1]
        _file = "{0}.html".format(page_name)
        with open(_file,'wb') as file:
            file.write(response.body)
            
#todo { this script isn't working at all with dev-medical}
#*  {but working fine with sites which having 'page' keyword in their url}

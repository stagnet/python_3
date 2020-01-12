import scrapy
class Price_baba(scrapy.Spider):

    #? identify
    name = 'laptop_price'

    #? Request
    def start_requests(self):
        url = 'https://pricebaba.com/laptop/pricelist/all-laptops-sold-in-india'
        yield scrapy.Request(url= url,callback= self.parse) #* here 'yield' function used to command scrapy to do desired task {which is request url in this case...}

    #* Response
    def parse(self, response):
        for specs in response.selector.xpath("//div[@class='prd-crd prd-crd-v p-b-xs p-h-s pos-rel ']"):
            yield{
                'Product_NAME': specs.xpath(".//div[@class= 'col-12 v-al-mdl p-h-xs']/a/text()[1]").extract_first(),
                'Price': specs.xpath(".//div[@class='d-block']/span/text()[1]").extract_first(),
                'Detail': specs.xpath(".//ul[@class='flex-grid']/li/child::span/text()").extract()  #* that's perfect ;)
            }
        #! here we try to extract multiple webpages....

        next_page = response.selector.xpath("//ul[@class= 'stack-inline pgntn-lnks d-inline-block']/li[6]/a/@href").extract_first()
        #todo so now we create logic that will check the web pages until we land on the last webpage of the product...

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_link, callback=self.parse)

import scrapy
from scrapy_splash import SplashRequest

import json

from ..items import WallmartItem

import logging


class GetinfoSpider(scrapy.Spider):
    name:str = 'GetinfoSpider'
    allowed_domains = ['www.walmart.com']

    script1:str = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end
    '''
    

    def start_requests(self, request):
        url = request.url
        return SplashRequest(
                url=str(url),
                callback=self.parse_item, 
                endpoint='execute',
                args = {
                    'lua_source': self.script1
            }
        )

    def parse_item(self, response):
        
        item = WallmartItem()
        #specs = response.css
        
        
        item['title'] = response.xpath('//*[@id="product-overview"]/div/div[3]/div/h1//text()').get(),
        item['price'] = response.css('span.price-characteristic::attr(content)').getall(),
        item['deliveryDate'] = response.css('p.no-margin::text').get(),
        item['pictures'] = response.css('img.prod-alt-image-carousel-image--left::attr(src)').getall(),
        item['description'] = response.css('div.about-desc ::text').getall(),


        yield item

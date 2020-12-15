import scrapy
from scrapy_splash import SplashRequest

import numpy as np

import json

from ..items import WallmartItem

import logging


class GetVariationsSpider(scrapy.Spider):
    name:str = 'GetVariationsSpider'
    allowed_domains:list = ['www.walmart.com']

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

    url:str = ''
    

    def start_requests(self, request):
        self.url = request.url
        return SplashRequest(
                url=str(self.url),
                callback=self.parse_item, 
                endpoint='execute',
                args = {
                    'lua_source': self.script1
            }
        )

    def parse_item(self, response):
        item = WallmartItem()
        #specs = response.css
        
        
        item['title'] = response.xpath('//*[@id="product-overview"]/div/div[3]/div/h1//text()').get()
        item['price'] = response.css('span.price-characteristic::attr(content)').getall()
        item['deliveryDate'] = response.css('p.no-margin::text').get()
        item['pictures'] = response.css('img.prod-alt-image-carousel-image--left::attr(src)').getall()
        item['description'] = response.css('div.about-desc ::text').getall()
        item['variations'] = []


        return response.follow(self.url, self.variations, cb_kwargs=dict(item=item))


    def variations(self, response, item):
        variations:list = []

        #variations = response.css('div.variants__contain').getall()

        colorAvailability = response.css('div.variants__contain')[0]
        ids = colorAvailability.css('input.var__radio::attr(id)').getall()
        imgs = colorAvailability.css('img.tile__img::attr(src)').getall()
        variationAvailability = colorAvailability.css('label.var__contain::attr(availabilitystatus)').getall()

        variations = [
            ids,
            imgs,
            variationAvailability
        ]

        multiDimentionalArray = np.array(variations)
        
        testArray:list = []

        for i in range(0,len(ids)):
            testArray.append(multiDimentionalArray[0:, i])
        

        variationsList:list = []

        for j in testArray:
            placeholder = j.tolist()
            variationDict:dict = {
                'iD' : placeholder[0],
                'img' : placeholder[1],
                'availability' : placeholder[2]
            }
            variationsList.append(variationDict)
            
        item['variations'] = variationsList

        yield item
            

    
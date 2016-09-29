# -*- coding: utf-8 -*-

import scrapy
from pyquery import PyQuery as q

'''
链家二手房
'''


class SecondHandHouseSpilder(scrapy.Spider):
    name = "second_hand_house"

    start_urls = ['http://sh.lianjia.com/ershoufang']
    count = 0

    def parse(self, response):
        d = q(response.body)
        for url in response.css('h2 a::attr(href)').extract():
            print(url)
            yield scrapy.Request(response.urljoin(url), callback=self.parse_house)

        next_pages = response.css('div.page-box.house-lst-page-box a::attr(href)').extract()
        if (next_pages is not None) and (len(next_pages) > 0):
            next_page = next_pages[-1]
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_house(self, response):

        d = q(response.body)

        def process(selection):
            text = d(selection).text()
            if ':' in text:
                text = d(selection).text().split(":")[1]
            return text.strip()
        print(process('#introduction div.base ul li:first-child'))
        
        yield {
            'housing_units': process('#introduction div.base ul li:first-child'),
            'area': process('#introduction div.base ul li:nth-child(5)'),
            'proportion': process('#introduction div.base ul li:nth-child(5)'),
            'level': process('#introduction div.base ul li:nth-child(2)'),
            'direction': process('#introduction div.base ul li:nth-child(4)'),
            'decoration': process('#introduction div.base ul li:nth-child(6)'),
            'last_transaction': process('#introduction div.transaction ul li:nth-child(1)'),
            'age_limit': process('#introduction div.transaction ul li:nth-child(3)'),
            'type': process('#introduction div.transaction ul li:nth-child(2)'),
            'only': process('#introduction div.transaction ul li:nth-child(4)'),
            'address': process('table.aroundInfo tr:nth - child(6)'),
            'decade': process('table.aroundInfo tr:nth - child(2) td:nth - child(2)'),
            'first_payment': process('table.aroundInfo tr:nth - child(4) td:first - child'),
            'monthly_supply': process('table.aroundInfo tr:nth - child(4) td:nth - child(2)'),
            'unit_price': process('table.aroundInfo tr:first - child'),
            'community': process('table.aroundInfo tr:nth - child(5)'),
            'id': process('table.aroundInfo tr:nth - child(7) td:nth - child(1)'),
            'price': process('div.content div.houseInfo div.price div.mainInfo.bold'),
            'url': response.url
        }

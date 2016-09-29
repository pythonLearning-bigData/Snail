# -*- coding: utf-8 -*-

import scrapy


class QuotesSpilder(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://sh.lianjia.com/ershoufang/sh4199747.html',
            'http://sh.lianjia.com/ershoufang/sh4207627.html'
        ]
        for url in urls:
            yield  scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s " % filename)



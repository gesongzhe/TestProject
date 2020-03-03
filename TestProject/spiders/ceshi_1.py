# -*- coding: utf-8 -*-
import scrapy
import logging

class Ceshi1Spider(scrapy.Spider):
    name = 'ceshi_1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        response.xpath()
        for quote in response.css('div.quote')[:1]:
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }
        self.log('测试的log信息', level=logging.INFO)
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
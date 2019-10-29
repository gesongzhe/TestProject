# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestprojectItem(scrapy.Item):
    article_title = scrapy.Field()
    article_id = scrapy.Field()
    article_summary = scrapy.Field()
    banner_url = scrapy.Field()
    author_name = scrapy.Field()
    author_id = scrapy.Field()
    author_url = scrapy.Field()

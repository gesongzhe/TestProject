# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import json
from TestProject.items import TestprojectItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['api.bilibili.com']
    base_url = 'https://api.bilibili.com/x/article/recommends?cid=0&pn={}&ps=20&jsonp=jsonp&sort=0'
    base_author_url = 'https://space.bilibili.com/{}'
    base_article_url = 'https://www.bilibili.com/read/cv{}'

    def start_requests(self):
        page_count = 1
        yield Request(url=self.base_url.format(page_count), meta={'page_count': page_count})

    def parse(self, response):
        page_count = response.meta.get('page_count')
        item = TestprojectItem()
        result_dic = json.loads(response.text)
        item_list = result_dic.get('data', [])
        for item in item_list:
            # 文章标题
            article_title = item.get('title')
            if not article_title:
                continue
            item['article_title'] = article_title
            # 文章id
            article_id = item.get('id')
            item['article_id'] = article_id
            article_url = self.base_article_url.format(article_id)
            item['article_url'] = article_url
            # 文章简介
            article_summary = item.get('summary')
            item['article_summary'] = article_summary
            # 封面链接
            banner_url = item.get('banner_url')
            item['banner_url'] = banner_url
            author_name = item.get('author').get('name')
            item['author_name'] = author_name
            author_id = item.get('author').get('id')
            item['author_id'] = author_id
            author_url = self.base_author_url.format(author_id)
            item['author_url'] = author_url
            yield item
        total_page = self.get_total_page(response)
        if not total_page or page_count >= total_page:
            return
        yield Request(url=self.base_url.format(page_count), meta={'page_count': page_count})

    def get_total_page(self, response):
        # 这个方法用来获取最大页，不过这里没有，所以直接写死了
        if response.text:
            total_page = 1000
            return total_page
        else:
            return 0

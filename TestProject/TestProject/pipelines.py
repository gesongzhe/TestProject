# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

dbconfig = {
    'user': '',
    'password': '123456',
    'database': 'test_bilibili',
    'host': '127.0.0.1'
}


class TestprojectPipeline(object):
    def process_item(self, item, spider):
        return item


# 关于item pipeline的学习文章：https://juejin.im/post/5af95280f265da0ba17ca1ba （崔大佬掘金文章）
class MysqlPipeline(object):
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig

    def open_spider(self, spider):
        """
        在spider启动的时候运行，做一些数据库的初始化方面的事情，如开启数据库连接。
        :return:
        """
        self.cnx = mysql.connector.connect(**self.dbconfig)
        # 向数据库中插入表，没有就创建表
        self.cursor = self.cnx.cursor()

    def close_spider(self, spider):
        """
        在spider关闭的时候自动调用，在这里可以做一些收尾性的工作，如关闭数据库连接。参数spider就是被关闭despider对象
        :param spider:
        :return:
        """
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        """
        这是item pipeline必定会实现的方法，默认去调用这个方法。我们在这里进行数据处理或者将数据存储到数据库中等操作。它必须返回一个item或者抛出一个DropItem异常。
        :param response:
        :return:
        """
        self.cursor.execute('insert into ')

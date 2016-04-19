# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import Selector
from tutorial.items import DmozItem
import sys
import string

add = 0
class DmozSpider(CrawlSpider):

    name = "bajdcc"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/bajdcc",
    ]

    
    rules = (
        # 提取匹配 bajdcc/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('bajdcc/default.html\?page\=([\w]+)', ),)),

        # 提取匹配 'bajdcc/p/' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('bajdcc/p/', )), callback='parse_item'),
        #Rule(LinkExtractor(allow=('bajdcc/archive/', )), callback='parse_item'), #以前的一些博客是archive形式的所以
    )

    def parse_item(self, response):        
        items = []

        item = DmozItem()
        item['title'] = response.xpath('//title/text()').extract()
        item['desc'] = response.xpath('//meta[name="description"]').extract()
        item['link'] = response.url
        print item
        items.append(item)
        return items
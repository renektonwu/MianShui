# -*- coding: utf-8 -*-
import scrapy


class CdfsanyaSpider(scrapy.Spider):
    name = 'cdfgsanya'
    allowed_domains = ['http://www.cdfgsanya.com']
    start_urls = ['http://www.cdfgsanya.com/']

    headers ={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "apiVersion": "2.0",
        "Appkey": "850226",
        "channel": "pc",
        "Connection": "keep-alive",
        "Cookie": "DISTRIBUTED_JSESSIONID=B480C0EA033849B8A9475F233A143EB4; Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593565829,1593657063; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1593657063",
        "language": "zh-CN",
        "Referer": "http://www.cdfgsanya.com/",
        "subsiteId": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.44 Safari/537.36",
        "Host":"www.cdfgsanya.com"
    }

    def parse(self, response):
        all_urls = response.css("a::attr(href)").extract()
        print(all_urls)
        pass

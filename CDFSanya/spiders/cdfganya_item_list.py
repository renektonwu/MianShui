# -*- coding: utf-8 -*-
import base64

import scrapy
import time
import re, json
import requests
from scrapy.http import Request
from CDFSanya.items import CdfProductItem, CdfProductItemLoader, CdfProductItem_list
import requests

import importlib,sys
importlib.reload(sys)

# reload(sys)
# sys.setdefaultencoding('gbk')

PYTHONIOENCODING="utf-8"
LC_ALL="en_US.UTF-8"



class CdfsanyaSpider(scrapy.Spider):
    name = 'cdfganya_item_list'
    allowed_domains = ['http://www.cdfgsanya.com']
    start_urls = ['http://www.cdfgsanya.com/']

    headers = {
        "Host": "www.cdfgsanya.com",
        "Connection": "keep-alive",
        "apiVersion": "2.0",
        "language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.44 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "subsiteId": "1",
        "channel": "pc",
        "Appkey": "850226",
        "Referer": "http://www.cdfgsanya.com/product-list.html?c=225510",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": "Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593672862,1593673028,1593674870,1593854234; DISTRIBUTED_JSESSIONID=1F7D493874F54A86B4DF597D753BBA42; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1594219157"

    }

    headers_three = {
        "Host": "www.cdfgsanya.com",
        "Connection": "keep-alive",
        "apiVersion": "2.0",
        "language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.44 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "subsiteId": "1",
        "channel": "pc",
        "Appkey": "850226",
        "Referer": "http://www.cdfgsanya.com/product.html?productId=400177&goodsId=400178&warehouseId=1&brandId=248152",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": "Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593672862,1593673028,1593674870,1593854234; DISTRIBUTED_JSESSIONID=1F7D493874F54A86B4DF597D753BBA42; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1594219157"}

    headers_for_get = {
        "Host": "www.cdfgsanya.com",
        "Connection": "keep-alive",
        "apiVersion": "2.0",
        "language": "zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.44 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "subsiteId": "1",
        "channel": "pc",
        "Appkey": "850226",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": "Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593672862,1593673028,1593674870,1593854234; DISTRIBUTED_JSESSIONID=1F7D493874F54A86B4DF597D753BBA42; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1594219157"
    }


    def start_requests(self):
        from selenium import webdriver
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.chrome.options import Options

        chrome_option = Options()
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # browser = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_option)
        browser = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_option)
        try:
            browser.maximize_window()
        except:
            pass

        #商品种类列表
        # 批量1111
        item_list_map=["http://www.cdfgsanya.com/product-list.html?c=225510","http://www.cdfgsanya.com/product-list.html?c=225509","http://www.cdfgsanya.com/product-list.html?c=225511","http://www.cdfgsanya.com/product-list.html?c=225512","http://www.cdfgsanya.com/product-list.html?c=225513","http://www.cdfgsanya.com/product-list.html?c=225514","http://www.cdfgsanya.com/product-list.html?c=225515"]
        # 单步单个调试2221
        # item_list_map=["http://www.cdfgsanya.com/product-list.html?c=225510"]

        for item in item_list_map:
            browser.get(item)
            # max_page 列表页最大显示页数
            max_page = int(browser.find_element_by_xpath('//li[@class="cm-pagination-next"]/preceding-sibling::li[1]').text)
            # for item in item_list_map:
            # response = browser.get(item_list_map[0])
            # self.headers["Referer"] = item_list_map[0]
            # c_num 品类编号
            c_num = re.findall("([+-]?\d+(\.\d+)?)", item)[0][0]
            # 在商品列表页上，通过凭借此接口，获得每个商品的详情页接口
            # request_url = "http://www.cdfgsanya.com/api/overseas/products/search?c=225510&hs=false&pn=138&ps=20&s=0"
            # 批量1112
            for pn in range(1,max_page+1):

            # 单个2222
            # for pn in range(1, 2):
                request_url = "http://www.cdfgsanya.com/api/overseas/products/search?c={}&hs=false&pn={}&ps=20&s=0".format(c_num, pn)
                yield Request(request_url, headers=self.headers, callback=self.parse_two)

    def parse_two(self, response):
        j_data = json.loads(response.text)
        # 示例： http://www.cdfgsanya.com/api/overseas/products/400177?warehouseId=1
        # 通过response 获得第三个页面详情页的接口参数 productId 即 detail_page_api = "http://www.cdfgsanya.com/api/overseas/products/{}?warehouseId=1".format(productId)
        # 批量1113
        items = j_data["items"]
        # 单步单个调试2223
        # item = j_data["items"][0]
        # 构造refer需要的参数
        # 示例 "Referer": "http://www.cdfgsanya.com/product.html?productId=400177&goodsId=400178&warehouseId=1&brandId=248152",


        # 批量1113 #去掉则为单步单个调试 批量1113
        for item in items:
            productId = item["id"]
            goodsId = item["goodsId"]
            warehouseId = item["warehouseId"]
            brandId = item["brandId"]
            styleId = item["styleId"]

            product_url = "http://www.cdfgsanya.com/product.html?productId={}&goodsId={}&warehouseId={}&brandId={}".format(productId, goodsId, warehouseId, brandId)

            item_loader = CdfProductItemLoader(item=CdfProductItem_list(), response=response)
            item_loader.add_value("productid", productId)
            item_loader.add_value("goodsId", goodsId)
            item_loader.add_value("warehouseId", warehouseId)
            item_loader.add_value("brandId", brandId)
            item_loader.add_value("styleId", styleId)
            item_loader.add_value("product_name", item["name"])
            item_loader.add_value("brand", item["brand"])
            item_loader.add_value("brandEN", item["brandEN"])
            item_loader.add_value("product_url", product_url)
            item_loader.add_value("dutyfee_price", item["salesPrice"]["value"])
            # print(1111, item["contrastPrice"])
            # print(1111, type(item["contrastPrice"]))
            if item["contrastPrice"] == None:
                market_price = ''
            else:
                market_price = item["contrastPrice"]["value"]
            item_loader.add_value("market_price", market_price)

            product_item = item_loader.load_item()
            yield product_item





            # 商品详情链接
            # detail_page_api = "http://www.cdfgsanya.com/api/overseas/products/{}?warehouseId=1".format(productId)

            # 调整333
            # 示例 http://www.cdfgsanya.com/product.html?productId=414740&goodsId=414734&warehouseId=1&brandId=248209
            # 示例 http://www.cdfgsanya.com/product.html?productId=403932&goodsId=403933&warehouseId=1&brandId=248151
            # 示例 http://www.cdfgsanya.com/product.html?productId=275785&goodsId=275785&warehouseId=1&brandId=248326
            # 示例 http://www.cdfgsanya.com/product.html?productId=347557&goodsId=347557&warehouseId=1&brandId=249511
            # 调试某个出错的商品
            # productId = 347557
            # goodsId = 347557
            # styleId = 347557
            # warehouseId = 1
            # brandId = 249511
            # # # 商品详情链接
            # detail_page_api = "http://www.cdfgsanya.com/api/overseas/products/{}?warehouseId=1".format(productId)
            # 调试某个出错的商品

            # self.headers_three["Referer"] = "http://www.cdfgsanya.com/product.html?productId=400177&goodsId=400178&warehouseId=1&brandId=248152".

            # 分类接口
            # 示例 "http://www.cdfgsanya.com/api/overseas/crumbs?productId=400177&goodsId=400178"
            # clasification_api = "http://www.cdfgsanya.com/api/overseas/crumbs?productId={}&goodsId={}".format(productId,goodsId)




    # def parse_three(self, response):
    #     # f2.write(line.decode('utf-8').encode('gbk'))
    #     # j_product_data = json.loads(response.text.decode('utf-8').encode('gbk'))
    #     # base64.encode(response.body)
    #     # json.loads(response.content.decode('utf-8'))
    #     # j_product_data = json.loads(response.text)
    #     # j_product_data = json.loads(response.text, encoding='utf-8')
    #     j_product_data = json.loads(response.text, encoding='utf-8')
    #
    #     # 20200706 todo 写item 入库一条详情数据到数据库中
    #     item_loader = CdfProductItemLoader(item=CdfProductItem(), response=response)
    #     item_loader.add_value("productid", response.meta.get("productid", ""))
    #     item_loader.add_value("goodsid", response.meta.get("goodsid", ""))
    #     item_loader.add_value("styleid", response.meta.get("styleid", ""))
    #     item_loader.add_value("warehouseid", response.meta.get("warehouseid", ""))
    #     item_loader.add_value("product_url", response.meta.get("product_url", ""))
    #
    #     item_loader.add_value("product_name", j_product_data["name"])
    #     item_loader.add_value("product_en_name", j_product_data["nameEN"])
    #     item_loader.add_value("product_pics", j_product_data["pics"])
    #     item_loader.add_value("product_description", j_product_data["description"])
    #     item_loader.add_value("produ_details", j_product_data["details"])
    #
    #     item_loader.add_value("smallpics", j_product_data["smallPics"])
    #     item_loader.add_value("largepics", j_product_data["largePics"])
    #     item_loader.add_value("brand_id", j_product_data["brand"]["id"])
    #     item_loader.add_value("brand_initial", j_product_data["brand"]["initial"])
    #     item_loader.add_value("brand_name", j_product_data["brand"]["name"])
    #     item_loader.add_value("brand_nameen", j_product_data["brand"]["nameEN"])
    #     item_loader.add_value("brand_log", j_product_data["brand"]["log"])
    #     item_loader.add_value("brand_country_name", j_product_data["brand"]["country"]["name"])
    #     item_loader.add_value("brand_country_name_en", j_product_data["brand"]["country"]["nameEN"])
    #     item_loader.add_value("brand_country_log", j_product_data["brand"]["country"]["log"])
    #     item_loader.add_value("productCount", j_product_data["brand"]["productCount"])
    #     item_loader.add_value("brand_description", j_product_data["brand"]["description"])
    #     # j_product_data["faqs"] = 'wgy'
    #     item_loader.add_value("aft_ques_service", j_product_data["faqs"])
    #     item_loader.add_value("product_properties", j_product_data["properties"])
    #     item_loader.add_value("styles", j_product_data["styles"])
    #     item_loader.add_value("styleDefines", j_product_data["styleDefines"])
    #     item_loader.add_value("productCode", j_product_data["productCode"])
    #     item_loader.add_value("product_classification", response.meta.get("clasi_response", ""))
    #     product_item = item_loader.load_item()
    #
    #     yield product_item


import scrapy
import time
import re
import requests



class CdfsanyaSpider(scrapy.Spider):
    name = 'cdfgsanya_sel'
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
        "Cookie": "Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593661868,1593672862,1593673028,1593674870; DISTRIBUTED_JSESSIONID=27C8AAE8DA074D1B8E55833EFFB47FA4; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1593678084"
    }

    def start_requests(self):
        from selenium import webdriver
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.chrome.options import Options

        chrome_option = Options()
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        browser = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_option)
        try:
            browser.maximize_window()
        except:
            pass

        # browser.get("http://www.cdfgsanya.com")

        header1={
            "Host": "www.cdfgsanya.com",
            "Connection": "keep-alive",
            "apiVersion": "2.0",
            "language": "zh-CN",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.44 Safari/537.36",
            "subsiteId": "1",
            "channel": "pc",
            "Appkey": "850226",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "Cookie": "Hm_lvt_99acc7258c46631a07bd9df8e3b3747f=1593661868,1593672862,1593673028,1593674870; DISTRIBUTED_JSESSIONID=27C8AAE8DA074D1B8E55833EFFB47FA4; Hm_lpvt_99acc7258c46631a07bd9df8e3b3747f=1593851655"
        }

        #商品种类列表
        item_list_map=["http://www.cdfgsanya.com/product-list.html?c=225510", "http://www.cdfgsanya.com/product-list.html?c=225509", "http://www.cdfgsanya.com/product-list.html?c=225511", "http://www.cdfgsanya.com/product-list.html?c=225512", "http://www.cdfgsanya.com/product-list.html?c=225513", "http://www.cdfgsanya.com/product-list.html?c=225514"]
        for item in item_list_map:
            browser.get(item)
            max_page = int(browser.find_element_by_xpath('//li[@class="cm-pagination-next"]/preceding-sibling::li[1]').text)
            # for item in item_list_map:
            # response = browser.get(item_list_map[0])
            # self.headers["Referer"] = item_list_map[0]
            c_num = re.findall("([+-]?\d+(\.\d+)?)", item)[0][0]
            b = 2



            # 在商品列表页上，通过凭借此接口，获得每个商品的详情页接口
            # request_url = "http://www.cdfgsanya.com/api/overseas/products/search?c=225510&hs=false&pn=138&ps=20&s=0"
            for pn in range(1,max_page+1):
                request_url = "http://www.cdfgsanya.com/api/overseas/products/search?c={}&hs=false&pn={}&ps=20&s=0".format(c_num, pn)
                yield scrapy.Request(request_url, headers=self.headers, callback=self.parse_two)
        #
        #
        # try:
        #     yield scrapy.Request(request_url, headers=self.headers, callback=self.parse_question)
        # except BaseException as e:
        #     print("111", e)

        # with open("sanya.html", "w+") as f:
        #     f.writelines(browser.page_source)

        # with open("sanya.html", "w+") as f:
            # f.writelines(browser.page_source)

    def parse_two(self, response):
        items = response["items"]
        for item in items:


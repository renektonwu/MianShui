# -*- coding: utf-8 -*-
__author__ = 'wgy'

from scrapy.cmdline import execute

import sys
import os

# todo 直接在一个程序里，入库2个表
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "cdfgsanya"])
# execute(["scrapy", "crawl", "cdfgsanya_sel"])
execute(["scrapy", "crawl", "cdfganya_item_list"])

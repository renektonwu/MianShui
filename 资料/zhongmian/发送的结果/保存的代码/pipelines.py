# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 可行的简单版本
import MySQLdb
import MySQLdb.cursors

class CdfsanyaPipeline:
    def process_item(self, item, spider):
        return item



class MysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        # self.conn = MySQLdb.connect('172.16.26.12', 'root', 'netpolice0810', 'spider_cdf', charset="utf8", use_unicode=True)
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '123456', 'spider_cdf', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # insert_sql = """
        #     insert into cdf_product_info(productid,goodsid,styleid,warehouseid,product_url,product_name,product_en_name,product_pics,product_description,produ_details,smallpics,largepics,brand_id,brand_initial,brand_name,brand_nameen,brand_log,brand_country_name,brand_country_name_en,brand_country_log,productCount,brand_description,aft_ques_service,product_properties,styles,styleDefines,productCode)
        #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \'\'\'%s\'\'\', %s, %s, %s, %s)  ON DUPLICATE KEY UPDATE productid=VALUES(productid),goodsid=VALUES(goodsid),styleid=VALUES(styleid),warehouseid=VALUES(warehouseid),product_url=VALUES(product_url),product_name=VALUES(product_name),product_en_name=VALUES(product_en_name),product_pics=VALUES(product_pics),product_description=VALUES(product_description),produ_details=VALUES(produ_details)
        # """
        a = MySQLdb.escape_string(item.get("aft_ques_service", ""))
        c = item.get("aft_ques_service", "")
        b = item.get("productid", "")
        print(112, type(MySQLdb.escape_string(item.get("aft_ques_service", ""))))
        print(113, type(item.get("productid", "")))
        insert_sql = """
            insert into cdf_product_info(productid,aft_ques_service)
            VALUES (%s,'%s') ON DUPLICATE KEY UPDATE productid=VALUES(productid)
        """ % (item.get("productid", ""), item.get("aft_ques_service", ""))
        print(153321, insert_sql)
        # params = list()
        # params.append(item.get("productid", ""))
        # # params.append(item.get("goodsid", ""))
        # # params.append(item.get("styleid", ""))
        # # params.append(item.get("warehouseid", ""))
        # # params.append(item.get("product_url", ""))
        # # params.append(item.get("product_name", ""))
        # # params.append(item.get("product_en_name", ""))
        # # params.append(item.get("product_pics", ""))
        # # params.append(item.get("product_description", ""))
        # # params.append(item.get("produ_details", ""))

        # # params.append(item.get("smallpics", ""))
        # # params.append(item.get("largepics", ""))
        # # params.append(item.get("brand_id", ""))
        # # params.append(item.get("brand_initial", ""))
        # # params.append(item.get("brand_name", ""))
        # # params.append(item.get("brand_nameen", ""))
        # # params.append(item.get("brand_log", ""))
        # # params.append(item.get("brand_country_name", ""))
        # # params.append(item.get("brand_country_name_en", ""))
        # # params.append(item.get("brand_country_log", ""))
        # # params.append(item.get("productCount", ""))
        # # params.append(item.get("brand_description", ""))
        # # print(999, item.get("aft_ques_service", ""))
        # params.append(item.get("aft_ques_service", ""))
        # # params.append(item.get("product_properties", ""))
        # # params.append(item.get("styles", ""))
        # # params.append(item.get("styleDefines", ""))
        # # params.append(item.get("productCode", ""))
        # print("insert_sql:",insert_sql, tuple(params))
        print(insert_sql)
        self.cursor.execute(insert_sql)
        self.conn.commit()
        return item












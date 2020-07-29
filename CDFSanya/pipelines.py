# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi

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
        # a = MySQLdb.escape_string(item.get("aft_ques_service", ""))
        # c = item.get("aft_ques_service", "")
        # b = item.get("productid", "")
        # print(112, type(MySQLdb.escape_string(item.get("aft_ques_service", ""))))
        # print(113, type(item.get("productid", "")))
        insert_sql = """
            insert into cdf_product_info(productid,goodsid,styleid,warehouseid,product_url,product_name,product_en_name,product_pics,product_description,produ_details,smallpics,largepics,brand_id,brand_initial,brand_name,brand_nameen,brand_log,brand_country_name,brand_country_name_en,brand_country_log,productCount,brand_description,aft_ques_service,product_properties,styles,styleDefines,productCode,product_classification)
            VALUES (%s,%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s') ON DUPLICATE KEY UPDATE productid=VALUES(productid)
        """ % (
            item.get("productid", ""),
            item.get("goodsid", ""),
            item.get("styleid", ""),
            item.get("warehouseid", ""),
            item.get("product_url", ""),
            item.get("product_name", ""),
            item.get("product_en_name", ""),
            item.get("product_pics", ""),
            item.get("product_description", ""),
            item.get("produ_details", ""),
            item.get("smallpics", ""),
            item.get("largepics", ""),
            item.get("brand_id", ""),
            item.get("brand_initial", ""),
            item.get("brand_name", ""),
            item.get("brand_nameen", ""),
            item.get("brand_log", ""),
            item.get("brand_country_name", ""),
            item.get("brand_country_name_en", ""),
            item.get("brand_country_log", ""),
            item.get("productCount", ""),
            item.get("brand_description", ""),
            item.get("aft_ques_service", ""),
            item.get("product_properties", ""),
            item.get("styles", ""),
            item.get("styleDefines", ""),
            item.get("productCode", ""),
            item.get("product_classification", ""))
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
        # #
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
        self.cursor.execute(insert_sql)
        self.conn.commit()
        return item

class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常
        return item

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(111,failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql = item.get_insert_sql()
        insert_sql = item.itemlist_get_insert_sql()
        print(2222, insert_sql)
        cursor.execute(insert_sql)












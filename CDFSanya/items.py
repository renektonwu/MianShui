# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity
import json

class CdfsanyaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CdfProductItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

def to_json(value):
    mysql_type = json.dumps(value, ensure_ascii=False)
    mysql_type = mysql_type.replace('\'', '\"')
    return mysql_type

def become_set(value):
    be_set = set()
    be_set.add(value)
    return be_set

def insert_single_quoto(value):
    single_quoto = value.replace('\'', '\'\'')
    return single_quoto




class CdfProductItem(scrapy.Item):
    productid = scrapy.Field()
    goodsid = scrapy.Field()
    styleid = scrapy.Field()
    warehouseid = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    product_en_name = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    product_pics = scrapy.Field()
    product_description = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    produ_details = scrapy.Field(input_processor=MapCompose(insert_single_quoto))

    smallpics = scrapy.Field()
    largepics = scrapy.Field()
    brand_id = scrapy.Field()
    brand_initial = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand_name = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand_nameen = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand_log = scrapy.Field()
    brand_country_name = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand_country_name_en = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand_country_log = scrapy.Field()
    productCount = scrapy.Field()
    brand_description = scrapy.Field(
        input_processor=MapCompose(insert_single_quoto)
    )
    aft_ques_service = scrapy.Field(
        input_processor = MapCompose(to_json),
        output_processor = Join(separator=",")
    )
    product_properties = scrapy.Field(
        input_processor=MapCompose(to_json),
        output_processor=Join(separator=",")
    )
    styles = scrapy.Field(
        input_processor=MapCompose(to_json),
        output_processor = Join(separator=",")
    )
    styleDefines = scrapy.Field(
        input_processor = MapCompose(to_json),
        output_processor = Join(separator=",")
    )
    productCode = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    product_classification = scrapy.Field(
        input_processor=MapCompose(insert_single_quoto),
        output_processor=Join(separator=",")
    )

    def get_insert_sql(self):
        # insert_sql = """
        #      insert into jobbole_article
        #      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
        #  """
        # params = (
        #     self.get("title", ""),
        #     self.get("url", ""),
        #     self.get("url_object_id", ""),
        #     self.get("front_image_path", ""),
        #     self.get("front_image_url", ""),
        #     self.get("parise_nums", 0),
        #     self.get("comment_nums", 0),
        #     self.get("fav_nums", 0),
        #     self.get("tags", ""),
        #     self.get("content", ""),
        #     self.get("create_date", "0000-00-00"),
        # )
        # return insert_sql, self

        # 自定义的insert_sql
        insert_sql = """
                    insert into cdf_product_info(productid,goodsid,styleid,warehouseid,product_url,product_name,product_en_name,product_pics,product_description,produ_details,smallpics,largepics,brand_id,brand_initial,brand_name,brand_nameen,brand_log,brand_country_name,brand_country_name_en,brand_country_log,productCount,brand_description,aft_ques_service,product_properties,styles,styleDefines,productCode,product_classification)
                    VALUES (%s,%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s') ON DUPLICATE KEY UPDATE productid=VALUES(productid)
                """ % (
            self.get("productid", ""),
            self.get("goodsid", ""),
            self.get("styleid", ""),
            self.get("warehouseid", ""),
            self.get("product_url", ""),
            self.get("product_name", ""),
            self.get("product_en_name", ""),
            self.get("product_pics", ""),
            self.get("product_description", ""),
            self.get("produ_details", ""),
            self.get("smallpics", ""),
            self.get("largepics", ""),
            self.get("brand_id", ""),
            self.get("brand_initial", ""),
            self.get("brand_name", ""),
            self.get("brand_nameen", ""),
            self.get("brand_log", ""),
            self.get("brand_country_name", ""),
            self.get("brand_country_name_en", ""),
            self.get("brand_country_log", ""),
            self.get("productCount", ""),
            self.get("brand_description", ""),
            self.get("aft_ques_service", ""),
            self.get("product_properties", ""),
            self.get("styles", ""),
            self.get("styleDefines", ""),
            self.get("productCode", ""),
            self.get("product_classification", ""))

        return insert_sql

class CdfProductItem_list(scrapy.Item):
    productid = scrapy.Field()
    goodsId = scrapy.Field()
    warehouseId = scrapy.Field()
    brandId = scrapy.Field()
    styleId = scrapy.Field()
    product_name = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brand = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    brandEN = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    product_url = scrapy.Field(input_processor=MapCompose(insert_single_quoto))
    dutyfee_price = scrapy.Field(
        output_processor=Join(separator=",")
    )
    market_price = scrapy.Field(output_processor=Join(separator=",")
    )

    def itemlist_get_insert_sql(self):
        # 自定义的insert_sql
        insert_sql = """
                    insert into item_list(productid,goodsId,warehouseId,brandId,styleId,product_name,brand,brandEN,product_url,dutyfee_price,market_price)
                    VALUES (%s,%s,%s,%s,%s,'%s','%s','%s','%s','%s','%s') ON DUPLICATE KEY UPDATE productid=VALUES(productid)
                """ % (
            self.get("productid", ""),
            self.get("goodsId", ""),
            self.get("warehouseId", ""),
            self.get("brandId", ""),
            self.get("styleId", ""),
            self.get("product_name", ""),
            self.get("brand", ""),
            self.get("brandEN", ""),
            self.get("product_url", ""),
            self.get("dutyfee_price", ""),
            self.get("market_price", ""),
            )

        return insert_sql












    # def get_insert_sql(self):
    #     insert_sql = """
    #         insert into cdf_product_info
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
    #     """
    #     params = (
    #         self.get("productid", ""),
    #         self.get("goodsid", ""),
    #         self.get("styleid", ""),
    #         self.get("warehouseid", ""),
    #         self.get("product_url", ""),
    #         self.get("product_name", 0),
    #         self.get("product_en_name", 0),
    #         self.get("product_pics", 0),
    #         self.get("product_description", ""),
    #         self.get("produ_details", ""),
    #     )
    #
    #     return insert_sql, params



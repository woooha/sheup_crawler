# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

class SheupPipeline(object):
    def open_spider(self, spider):
        f = open('results.csv', 'wb')
        self.exporter = CsvItemExporter(f)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

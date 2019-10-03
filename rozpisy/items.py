# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field



class RozpisyItem(Item):
    termin=Field()
    cas=Field()
    soutez=Field()
    souper1=Field()
    souper2=Field()
    odkaz=Field()
    
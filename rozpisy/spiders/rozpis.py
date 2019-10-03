# -*- coding: utf-8 -*-
import scrapy
from rozpisy.items import RozpisyItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class RozpisSpider(scrapy.Spider):
    name = 'rozpis'
    allowed_domains = ['https://www.fotbalpraha.cz/']
    start_urls = [	"https://www.fotbalpraha.cz/souteze/zapasy/153-a2b-1-a-trida-skupina-b-muzu?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/154-a3a-1-b-trida-skupina-a-muzu?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/158-a4c-2-trida-skupina-c-muzu?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/162-c2a-1-trida-starsiho-dorostu?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/165-d4a-2-trida-mladsiho-dorostu?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/168-e2b-1-trida-skupina-b-starsich-zaku?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/171-f1a-prebor-mladsich-zaku?id_season=2019&id_team=26&id_round=999",
    				"https://www.fotbalpraha.cz/souteze/zapasy/173-f2b-1-trida-skupina-b-mladsich-zaku?id_season=2019&id_team=26&id_round=999",
                    "https://www.fotbalpraha.cz/souteze/zapasy/174-f3a-2-trida-skupina-a-mladsich-zaku?id_season=2019&id_team=26&id_round=999"]

    def parse(self, response):
         l=ItemLoader(item=RozpisyItem(), response=response)
         l.add_xpath("termin", '//*[@class="date"]/text()')
         l.add_xpath("soutez",'//*[@class="game_number"]/text()')
         l.add_xpath("odkaz",'//*[@class="btn btn--white btn--no-margin"]//@href')
         final=l.load_item()
         finalni_slovnik={}
         ind=0
         for i in final["soutez"]:
         	list_final=[]
         	list_final.append(final["termin"][ind])
         	list_final.append(final["soutez"][ind])
         	finalni_slovnik[ind+1]=list_final
         	list_final=[]
         	list_final.append("'https://www.fotbalpraha.cz"+final["odkaz"][ind]+"'")
         	indexis="url"+str(ind+1)
         	finalni_slovnik[indexis]=list_final
         	ind+=1
         return finalni_slovnik


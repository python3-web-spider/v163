# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class VideoSpider(scrapy.Spider):
    name = 'video'
    url = 'http://m.open.163.com/movie?plid=M6SGF6VB4&rid=M6SGHFBMC'

    def start_requests(self):
        yield SplashRequest(self.url, self.parse)

    def parse(self, response):
        print(response.css('video::attr(src)').extract_first())
        print(response.text)


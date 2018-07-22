# -*- coding: utf-8 -*-

'下载网易公开课的全部视频'

__author__ = 'toyourheart'

import os

import scrapy
from scrapy_splash import SplashRequest


class AllVideoSpider(scrapy.Spider):
    name = 'allvideo'
    url = 'https://c.open.163.com/search/search.htm?query=&enc=%E2%84%A2#/search/video'

    def start_requests(self):
        yield SplashRequest(self.url, self.parse)

    def parse(self, response):
        titles = response.css('p.tit.nowrp')
        for title in titles:
            video_url = title.css('a.f-c3.f-f0::attr(\'href\')').extract_first()
            print('正在下载 ' + video_url)
            os.system('you-get ' + video_url) # 使用 you-get 下载视频

        print(response.url)
        next_page = response.css('a.znxt')
        if next_page:
            yield SplashRequest(
                response.url,
                self.parse,
                endpoint='render.html',
                args={'js_source': "document.getElementsByClassName('znxt')[0].click()"},
                dont_filter=True
            )

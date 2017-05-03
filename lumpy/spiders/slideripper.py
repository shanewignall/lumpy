# -*- coding: utf-8 -*-
import scrapy
import html2text


class SlideripperSpider(scrapy.Spider):
    name = "slideripper"

    start_urls = [
    'https://media.pearsoncmg.com/pls/products/coco/statistics/1256888370/presentations/ge_stat_06_overview.html'
    ]

    def parse(self, response):
        converter = html2text.HTML2Text()
        converter.ignore_links = True

        header = response.css('h2.title::text').extract_first()
        for section in response.xpath('.//p//text()'):
            with open('output.txt', 'a') as f:
                f.write(section.extract().encode('utf-8') + '\n\n')

        next_page = response.css('a.nextButton::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

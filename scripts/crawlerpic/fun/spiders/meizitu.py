# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from fun.items import MeizituItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class MeizituSpider(CrawlSpider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://www.meizitu.com/',
    )
    rules = (

        Rule(SgmlLinkExtractor(allow=(r'http://www.meizitu.com/tag/[a-zA-z]+_\d+_\d+.html'))),
        Rule(SgmlLinkExtractor(allow=(r'http://www.meizitu.com/a/\d+.html')), callback="parse_item"),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = MeizituItem()
        item['url'] = response.url
        item['name'] = hxs.select('//h2/a/text()').extract()
        item['tags'] = hxs.select("//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p").extract()
        image_urls =hxs.select("//div[@id='picture']/p/img/@src").extract()
        item['image_urls'] = image_urls
        print item
        #item['images'] = '_'.join(image_urls.split('/')[3:])
        return item
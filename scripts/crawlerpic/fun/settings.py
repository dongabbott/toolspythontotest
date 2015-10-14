# -*- coding: utf-8 -*-

# Scrapy settings for fun project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fun'

SPIDER_MODULES = ['fun.spiders']
NEWSPIDER_MODULE = 'fun.spiders'

ITEM_PIPELINES = {'fun.pipelines.ImageDownloadPipeline': 1}

IMAGES_STORE = './tmp/images'


DOWNLOAD_DELAY = 0.25    # 250 ms of delay

IMAGES_MIN_HEIGHT = 768
IMAGES_MIN_WIDTH  = 1024
DOWNLOAD_TIMEOUT = 1200
CONCURRENT_ITEMS = 128
CONCURRENT_REQUEST = 64
CONCURRENT_REQUEST_PER_DOMAIN = 64
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False
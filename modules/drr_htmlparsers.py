#!/usr/bin/env python

import json
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as bs
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
import re
from itertools import compress

def unddr_parser(html):
    
    selector = Selector(text = html)
    
    try:
        page_text = '\n'.join([line.strip() for line in selector.css('div#main-content ::text').extract()])
    except:
        ''
        
    try:
        page_links = selector.css('div#main-content a::attr(href)').extract()
    except:
        page_links = []
    
        
    return(page_text, page_links)


def drmkc_parser(html):
    
    selector = Selector(text = html)
    
    try:
        page_text = '\n'.join([line.strip() for line in selector.css('body > form > div ::text').extract()])
    except:
        ''
    
    try:
        page_links = selector.css('body > form > div a::attr(href)').extract()
    except:
        page_links = []
    
    return(page_text, page_links)
    
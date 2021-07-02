#!/usr/bin/env python

import os
import logging
import json

import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as bs
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
import re

from datetime import datetime
from itertools import compress

logger = logging.getLogger(__name__)

main_dir = os.path.join("/home", "ubuntu", "keyword_crawler")
data_dir = os.path.join(main_dir, "data")
mat_dir = os.path.join(main_dir, "materials")
log_dir = os.path.join(main_dir, "logs")

# Define scraper starting point
start_url = 'https://www.unddr.org/', 'https://drmkc.jrc.ec.europa.eu/']

# Create dirs
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

if not os.path.isdir(log_dir):
    os.mkdir(log_dir)

# Define scraper function
def main(start_urls = start_urls, keywords = keywords):
    # Create class
    class drr_spider (scrapy.Spider):
        name = "drr_spider"

        def start_requests(self, start_urls = start_urls):
            for start_url in start_urls:
                self.start_url = start_url
                if start_url not in scraped_urls:
                    logger.info("Starting scrape for {start_url}...".format(start_url = start_url))
                    yield scrapy.Request(url = start_url, callback = self.parse)
                else:
                    continue

        #Parsing
        def parse(self, response):
            logger.info("Scraping {}...".format(response.url))

            site_dict = {}

            page_url = response.url
            domain_url = "https://" + urlparse(page_url).netloc
            start_domain_url = "https://" + urlparse(self.start_url).netloc

            if domain_url != start_domain_url:
                return

            page_html = response.body
            page_soup = bs(page_html, 'html.parser')

            page_text = page_soup.get_text().lower()

            try:
                page_links = list(set([re.sub(r'\/$', '', tag['href']) for tag in page_soup.find_all('a') if tag.has_attr('href')]))
                page_links = list(compress(page_links, [len(link) > 1 for link in page_links]))

                if any(word in page_text for word in keywords):
                    matches = list(compress(keywords, [keyword in page_text for keyword in keywords]))

                    site_dict['url'] = page_url
                    site_dict['links'] = page_links
                    site_dict['date-of-access'] = str(datetime.now().date())
                    site_dict['keywords_matched'] = matches

                    site_list.append(site_dict)

                scraped_urls.append(page_url)

                internal_urls = list(compress(page_links, [(domain_url in link or link.startswith('/')) for link in page_links]))

                new_urls = list(set(internal_urls) - set(scraped_urls)) # Extracted URLs from pages - should be on same domain

                if len(new_urls)>0:
                    more_pages = True # Test for whether there are more pages
                else:
                    more_pages = False

            except:
                more_pages = False       

            if more_pages:
                for url in new_urls:
                    yield scrapy.Request(url = urljoin(page_url, url), callback=self.parse)
                        
            
            # Save scraped data
            outname = "drr_scrape{}.json".format(str(datetime.now().date()))
            with open(os.path.join(data_dir, outname), 'w') as f:
                json.dump(site_list, f)
                
    #Initiatlize lists
    site_list = list()
    scraped_urls = list()

    # Set parameters
    start_urls = start_urls # start URLs

    #Run spider
    process = CrawlerProcess()
    process.crawl(drr_spider)
    process.start()
    
    return(site_list)
    

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(message)s'
    logout = os.path.join(log_dir, 'scraper.log')
    logging.basicConfig(filename=logout, filemode='a', level=logging.INFO, format = FORMAT)
    main()

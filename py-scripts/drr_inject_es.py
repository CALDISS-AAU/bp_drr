#!/usr/bin/env python

import sys
sys.path.append('../modules')

import drr_es_inject
import json

with open("../data/drr_scrape2021-07-08_es.json.json", 'r') as f:
    data = json.load(f)

error_ids = ['drmkc00188']
    
docs = {}

for item in data:
    if not item['id'] in error_ids:
        docs[item['id']] = item

drr_es_inject.inject(docs, index='drr', host='130.226.98.70', port=9200, verbose=True, verify=False)
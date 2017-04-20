#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:01:14 2017

@author: andre
"""

from urllib.request import urlopen
import json

url = 'http://api.icndb.com/jokes/'
request = urlopen(url)
response = request.read()

data = json.loads(response)

# List comprehension - Identificada pelas colchetes
jokes = [v['joke'] for v in data['value']]

# Generator expressions - É o mesma sintaxe que o List comprehension, só que com parenteses.
jokes_iterator = (v['joke'] for v in data['value'])

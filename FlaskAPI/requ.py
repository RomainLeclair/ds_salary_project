# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:18:40 2020

@author: Leclair Romain
"""

import requests
from data_input import data_in

URL =  'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers = headers, json=data)

r.json()
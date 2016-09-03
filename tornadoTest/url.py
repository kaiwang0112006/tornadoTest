#!/usr/bin/env python
#coding:utf-8

import sys

#from handler.index import IndexHandler
#from handler.query import QueryGene
from views.hello import *
from views.music import *

url=[
    (r'/', helloworld),
    (r'/music', musicHome),
    (r'/musiclistjson', musiclistjson),
    (r'/music/([0-9]+)', musicOne),
    (r'/loadmusic/([0-9]+)', loadmusic)
    ]

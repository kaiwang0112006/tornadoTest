#!/usr/bin/env python
#coding:utf-8
from views.basehandle import BaseHandler
import tornado.web

import sys

class helloworld(BaseHandler):
    def get(self):
        self.render("home.html")

#-*- coding: utf-8 -*-
import tornado.web
import os.path
import tornado.ioloop
import mako.lookup
import tornado.httpserver
import mako.template

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        template_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories=[template_path], input_encoding='utf-8', output_encoding='utf-8')
        self.musiclist = []

    def render_string(self, filename, **kwargs):
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return template.render(**namespace)

    def render(self, filename, **kwargs):
        self.finish(self.render_string(filename, **kwargs))
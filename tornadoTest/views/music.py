#!/usr/bin/env python
#coding:utf-8
from views.basehandle import BaseHandler
import tornado.web
from views.server_paging import *
import sys
import os

import json

class musicHome(BaseHandler):
    def get(self):
        musiclist = []
        
        if sys.platform != 'win32':
            deeppath = r"/static/music/"
        else:
            # example for windows
            deeppath = r"\static\music\\"

        musicPath = os.getcwd() + deeppath
        listf = open(musicPath+'list.txt')
        for eachline in listf:
            line = eachline.split('\t')
            musiclist.append(line)
        listf.close()
        BaseHandler.musiclist = musiclist

        self.render("music.html")
        
class musiclistjson(BaseHandler):
    def get(self):
        request_values = self.request.arguments
        
        start, end = paging_index(request_values)

        try:
            musiclist = BaseHandler.musiclist
        except:
            musiclist = []
        
        if len(musiclist) == 0:
            if sys.platform != 'win32':
                deeppath = r"/static/music/"
            else:
                # example for windows
                deeppath = r"\static\music\\"
            musicPath = os.getcwd() + deeppath
            listf = open(musicPath+'list.txt')
            for eachline in listf:
                line = eachline.split('\t')
                musiclist.append(line)
            listf.close()
            BaseHandler.musiclist = musiclist   
            
        music = []
        
        for b in range(start, end):
            if b < len(musiclist):
                music.append([b,musiclist[b][0].decode("gbk"),musiclist[b][1]])
        
        cardinality = len(musiclist) 
        cardinality_filtered = cardinality
          
        output = {}
        output['sEcho'] = str(int(request_values['sEcho'][0]))
        output['iTotalRecords'] = str(cardinality)
        output['iTotalDisplayRecords'] = str(cardinality_filtered)
        output['aaData'] = music
        return self.write(json.dumps(output))

class musicOne(BaseHandler):
    def get(self,musicid):
        try:
            musiclist = BaseHandler.musiclist
        except:
            musiclist = []
        mresult = fetchmusic(musicid,musiclist)
        BaseHandler.musiclist = mresult['musiclist']

        self.render("musicOne.html",musicname=mresult['musicname'], musicid=musicid, musicfile=mresult['musicfile'])

class loadmusic(BaseHandler):        
    def get(self,musicid):
        try:
            musiclist = BaseHandler.musiclist
        except:
            musiclist = []
        mresult = fetchmusic(musicid,musiclist)
        print(mresult)
        BaseHandler.musiclist = mresult['musiclist']
        return self.write(mresult)
        
def fetchmusic(musicid,musiclist):

    if len(musiclist) == 0:
        if sys.platform != 'win32':
            deeppath = r"/static/music/"
        else:
            # example for windows
            deeppath = r"\static\music\\"
        musicPath = os.getcwd() + deeppath
        listf = open(musicPath+'list.txt',encoding='utf-8')
        for eachline in listf:
            line = eachline.strip().split('\t')
            musiclist.append(line)
        listf.close()

    try:
        musicname = musiclist[int(musicid)][0]
        musicfile = musiclist[int(musicid)][1]
    except:
        musicname = ''
        musicfile = ''
    print(musicname)
    return {'musicname':musicname, 'musicfile':musicfile,'musiclist':musiclist}
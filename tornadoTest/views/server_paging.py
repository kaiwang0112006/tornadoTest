# -*- coding: utf-8 -*- 
#coding:gbk

    
def paging_index(request_values):
    #print request_values
    if ( request_values[u'iDisplayStart'][0] != "" ) and ( int(request_values[u'iDisplayLength'][0]) != -1 ):
        start = int(request_values[u'iDisplayStart'][0])
        long = int(request_values[u'iDisplayLength'][0])
    else:
        start = 0 
        end = 0

    return start,start+long

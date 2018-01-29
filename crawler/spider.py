# -*- coding: UTF-8 -*-
import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

print html


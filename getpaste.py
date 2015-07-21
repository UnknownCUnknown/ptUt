#!/usr/bin/python
# coding=utf-8
import urllib2
import sys
import HTMLParser
import re

html_parser = HTMLParser.HTMLParser()

pattern = re.compile(r'<div class="paste"><pre>(.+?)</pre>', re.S)

def getpaste(url):
    res = urllib2.urlopen(url)
    txt = res.read()
    ans = pattern.findall(txt)[0];
    return html_parser.unescape(ans.decode("utf8"))#.decode("utf8")

if sys.argv[1].startswith('http'):
    url = sys.argv[1]
else :
    url = "http://paste.ubuntu.com/" + sys.argv[1] 
times = 0
while times < 5:
    try:
        print getpaste(url).encode('utf8')
    except Exception,e:
        times = times + 1
        continue
    break


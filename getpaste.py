#!/usr/bin/python
# coding=utf-8
import urllib2
import sys
import HTMLParser

html_parser = HTMLParser.HTMLParser()

def getpaste(url):
    res = urllib2.urlopen(url)
    txt = res.read()
    #ans = txt.split('91</pre></div></td><td class=\"code\"><div class=\"paste\"><pre>')
    ans = txt.split('<td class=\"code\"><div class=\"paste\"><pre>')
    ans = ans[1]
    ans = ans.split('</pre>')
    ans = ans[0]
    ans = ans.decode('utf8')
    ans = html_parser.unescape(ans) 
    return ans
if sys.argv[1].startswith('http'):
    url = sys.argv[1]
else :
    url = "http://paste.ubuntu.com/" + sys.argv[1] 
times = 0
while times < 5:
    try:
        print getpaste(url)
    except Exception,e:
        times = times + 1
        continue
    break


#!/usr/bin/python
# coding=utf-8
import cookielib
import urllib2
import urllib
import sys
import os

CookieJar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar));

def paste(txt,user="UCU",language="text"):
    url = "http://paste.ubuntu.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36"
    }
    data = {
        "poster" : user,
        "syntax" : language,
        "content" : txt
    }
    #print txt
    post_data = urllib.urlencode(data)
    #print post_data
    req = urllib2.Request(url,post_data,headers)
    res = opener.open(req);
    #print res.getcode()
    return res.geturl()

def readFromFile(filename):
    f = open(os.getcwd()+"/"+filename);
    str = "";
    for line in f.readlines():
        str = str + line
    return str

filename = ""
user = "UCU"
language = "text"
#print len(sys.argv)
if len(sys.argv) >= 2 :
    filename = sys.argv[1]
    if len(sys.argv) >= 3:
        user = sys.argv[2]
        if len(sys.argv) >= 4:
            language = sys.argv[3]

while True:
    try:
        print paste(readFromFile(filename),user,language)
    except Exception:
        continue


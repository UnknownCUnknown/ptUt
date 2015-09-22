#!/usr/bin/python
# coding=utf-8

import cookielib
import urllib2
import urllib
import requests
import re
import threading
import thread
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

def getNowId():
    url = paste("test")
    pattern = re.compile("[0-9]{8}")
    id = pattern.findall(url)[0]
    return id


def search(l,r):
    url = "http://paste.ubuntu.com/"
    cnt = 0
    pattern = re.compile('<div class="paste"><pre>(.+?)</pre>',re.S)
    for id in range(l,r):
        #print id
        #sys.stdout.flush()
        rurl = url + str(int(id)) + '/'
        res = requests.get(rurl)
        res.encoding = 'utf-8'
        #print rurl
        txt = res.text#.decode('utf8')
        try:
            ans = pattern.findall(txt)[0]
        except Exception:
            continue
        #print ans
        if '#include' in ans:
            file = '/tmp/'+str(id)+'.html'
            output = open(file,'w')
            output.write(txt.encode('utf8'))
            output.flush()
            #os.system('open '+file)
            print rurl
        cnt = cnt + 1
    #print '['+str(l)+','+str(r)+']'+'has complete'
    thread.exit()


class myThread(threading.Thread):
    def __init__(self,l,r):
        threading.Thread.__init__(self)
        self.l = l
        self.r = r
    def run(self):
        search(self.l,self.r)

def ishtmlin(dir):
    for file in dir:
        if file.endswith('html'):
            return True
    return False;


id = getNowId()

idfile = open('idfile','r')
l = int(idfile.readlines()[0][:-1])
idfile = open('idfile','w')
#l = int(idfile.readlines()[0])
print >>idfile,id
print id
threads = []
id = int(id)
r = id
print l,r
#l = r-100 
m = (r-l)/21
dir = os.listdir('/tmp')
if ishtmlin(dir):
    os.system('rm /tmp/*.html')
for i in range(0,20):
    threads.append(myThread(l+m*i,l+m*i+m))
threads.append(myThread(l+m*20,r))


for Thread in threads:
    Thread.start()

for Thread in threads:
    Thread.join()

print 'Exiting'
        

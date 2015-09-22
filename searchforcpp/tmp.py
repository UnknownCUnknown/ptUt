#!/usr/bin/python
# coding=utf-8
def ispa(n):
    a = []
    while n!=0 :
        a.append(n%10)
        n/=10
    size = len(a)
    for i in range(0,int(size/2)):
        if a[i] != a[size-i-1]:
            return False;
    return True

print(list(filter(ispa,range(1,1000))))

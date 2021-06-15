# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:38:17 2021

"""

testfile = open('test.txt', 'w')
testfile.write('TESTING TESTING')
testfile.close()


open('test.txt', 'r').read()

f = open('test.txt', 'a')
lst = [x * x for x in range(1, 11)]
for num in lst:
    f.write(str(num))
f.close()
open('test.txt', 'r').read()

f = open('test.txt', 'r')
for ch in f.readline():
    print(ch)
f.close()


f = open("pic.png", 'rb')
for bit in f.readline():
    print(ch)

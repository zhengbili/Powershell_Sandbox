#!/usr/bin/env python3
import os

filenames=os.listdir('Second-Stage')
infos=dict([line.split(', ') for line in open('result2.txt').read()[:-1].split('\n')])
f=open('result.txt','w')
for filename in filenames:
    if filename in infos:f.write('%s, %s\n'%(filename,infos[filename]))
    else:f.write('%s, %s\n'%(filename,'ip:0.0.0.0'))
f.close()

#!/usr/bin/env python3
import sys

info=open(sys.argv[1]).read().split('\n')
f=open(sys.argv[2],'w')
for i in range(len(info)):
    if 'ip:' not in info[i]:
        continue
    j=i-1
    while len(info[j])!=64:
        j-=1
    f.write('%s, %s\n'%(info[j],info[i].replace("'",'')))
f.close()

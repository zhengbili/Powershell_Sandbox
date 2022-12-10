#!/usr/bin/env python3
import os
import re
import subprocess

os.chdir('../sandbox')
resultFile = "../samples/result.txt"
if os.path.exists(resultFile):
    os.remove(resultFile)
f=open(resultFile,'wb')
g = os.walk("../samples/Second-Stage")
for path,dir_list,file_list in g:
    for file_name in file_list:
        os.system("python ../samples/preprocessing.py ../samples/Second-Stage/%s temp.ps1"%file_name)
        command = "../src/powershell-win-core/bin/Debug/net7.0/win7-x64/publish/pwsh -File temp.ps1"
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        try:
            result, stderr = p.communicate(timeout=60)
            result = result
        except:
            p.kill()
            result = b""

        if b"ip:" not in result:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, env={"IgnoreQuote": 'True'})
            try:
                result, stderr = p.communicate(timeout=60)
                result = result
            except:
                p.kill()
                result = b""

        print(file_name)
        pattern = re.compile(rb"ip:[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", re.I)
        match = pattern.search(result)
        print(match)
        if match != None :
            f.write(b"%s, %s\n"%(file_name.encode(),match.group()))
        else:
            f.write(b"%s, ip:0.0.0.0\n"%(file_name.encode(),))
f.close()

#!/usr/bin/env python3
import re
import base64
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile,'r') as f:
    string = f.read()

#Char
pattern = re.compile(r"\$[a-zA-Z0-9_]*\s*=\s*\[Char\[\]\]\((.*?)\)(\n)+(.*?)(\n)+(.*?)out-null", re.I)
matches = pattern.search(string)
if matches != None:
    o = open(outputFile, 'w')
    o.write(matches.group())
    exit(0)

#powershell -e
pattern = re.compile(r"powershell(.*?)-e(.*?)\"(.*?)\"", re.I)
matches = pattern.findall(string)
if len(matches) > 0:
    o = open(outputFile, 'w')
    o.write(base64.b64decode(matches[0][2]).decode("utf-16"))
    exit(0)

#anti
pattern = re.compile(r"if(.*?)(get-random|get-date|false)(.*?){", re.I)
matches = pattern.findall(string)
if len(matches) > 0:
    string = re.sub(pattern, "if($true){", string)

#iex
pattern = re.compile(r"(\.|\&)\s*\(\s*\$[a-zA-Z0-9_]*\[[0-9]*\]\s*\+\s*\$[a-zA-Z0-9_]*\[[0-9]*\]\s*\+\s*\'[x|X]\'+\s*\)", re.I)
matches = pattern.findall(string)
if len(matches) > 0:
    string = re.sub(pattern, "iex", string)
pattern = re.compile(r"(\.|\&)\s*\(\s*(.*?)\[[0-9,]*\]-join\'\'\)", re.I)
matches = pattern.findall(string)
if len(matches) > 0:
    string = re.sub(pattern, "iex", string)

#split
pattern = re.compile(r".([s|S][p|P][l|L][i|I][t|T])\s*\(\s*'([^']*)'\s*\)")
matches = pattern.findall(string)
new_string = ""
for match in matches:
    #variable_name = match[0]
    method_name = match[0]
    split_string = match[1]
    new_string = f""
    for char in split_string:
        new_string += f" -{method_name.lower()}"+ f" '{char}'"
    print(new_string)
if len(matches) > 0:
    string = re.sub(pattern, new_string, string)

o = open(outputFile, 'w')
o.write(string)

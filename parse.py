import sys
import re

script_file,log_file,output_file=sys.argv[1:4]
lines=open(script_file).read().split('\n')
logs=open(log_file).read().split('\n')
i=0
j=0
re_fun=r'([A-Za-z]+)\([^\(\)]+\)'
re_var=r'\$([A-Za-z]+)([\+\-\*\/]?)=[^=;]+'
re_iex=r'iex [\s\S]+'
f=open(output_file,'w')
for line in lines:
    if re.search(re_fun,line):
        info=logs[j].split(':');j+=1
        assert info[0]=='CallDotnetFunction'
        if info[2] and info[2].split(',')[0]=='System.String':
            line=re.sub(re_fun,r'\1(%s)'%str(bytes.fromhex(info[2].split(',')[1]))[1:],line)
            f.write('//'+line+'\n')
    if re.search(re_var,line):
        info=logs[j].split(':');j+=1
        assert info[0]=='SetVariableValue'
        if info[1]=='System.Int32':
            line=re.sub(re_var,r'$\1\2='+info[2],line)
        elif info[1]=='System.String':
            line=re.sub(re_var,r'$\1\2='+str(bytes.fromhex(info[2]))[1:],line)
    if re.search(re_iex,line):
        info=logs[j].split(':');j+=1
        assert info[0]=='CallCmdlet'
        if info[2] and info[2].split(',')[0]=='System.String':
            line=re.sub(re_iex,r'iex %s'%str(bytes.fromhex(info[2].split(',')[1]))[1:],line)
    f.write(line+'\n')
f.close()

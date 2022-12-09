import os

filenames=os.listdir('Second-Stage')
infos=dict([line.split(', ') for line in open('result2.txt').read()[:-1].split('\n')])
infos['0477e60c7bebf5a212a2cb11fffe9a73d944e7a54f0065164784a44a36449023']='ip:197.160.114.255'
infos['b0c5bc59cecf4dac640416a83ef9ff52d34cc38f6f37e19b5ee1cc8b2f64e51f']='ip:97.42.221.62'
infos['efc237e4c2278922f42db9c44ce54a509bdc7433bf192bc3e70e30b637bf45e9']='ip:138.93.153.70'
f=open('result.txt','w')
for filename in filenames:
    if filename in infos:f.write('%s, %s\n'%(filename,infos[filename]))
    else:f.write('%s, %s\n'%(filename,'ip:0.0.0.0'))
f.close()

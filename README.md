# powershell反混淆level2代码执行说明

> 由于环境差异及平台自身优化，linux下识别速度和准确率均高于windows下，建议使用linux平台测试。

## 环境要求
1. powershell
2. dotnet(核心编译环境)
3. git
4. python3(用于批量执行及预处理)

## 编译步骤
参见[PowerShell官方编译要求](https://github.com/PowerShell/PowerShell#building-the-repository)
注：为方便测试，打包程序已包含ubuntu22.04及win10Pro环境下编译结果。

## 自动化运行

### linux平台（可wsl）
- `./build.ps1`自动编译（确保已安装完整编译环境）
- `cd samples && ./test2.sh`自动进行level2反混淆检测，结果保存至`samples/result.txt`及`/home/datacon/answer/powershell/level02/result.txt`
- `./run.sh`自动调用以上步骤

### windows平台
- `./build.ps1`自动编译（确保已安装完整编译环境）
- `cd samples && python3 ./test2.py`自动进行level2反混淆检测，结果保存至`samples/result.txt`
- `./run.bat`自动调用以上步骤

## 相关代码处理解释
1. powershell源码修改点见git log。
2. preprocessing.py和postprocessing.py分别为预处理脚本及后处理脚本。前者用于处理混淆脚本中的反沙箱以及平台差异；后者仅提取输出。
3. 本项目完全使用动态分析，不做静态分析。

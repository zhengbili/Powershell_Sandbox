export PATH=$PWD:$PATH
rm temp1.txt
cd ../sandbox
for i in $(ls ../samples/First-Stage/);do
    echo $i | tee -a ../samples/temp1.txt
    ../samples/simple_preprocessing.py ../samples/First-Stage/$i temp.ps1
    res=$(timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh temp.ps1 2>/dev/null)
    if [[ $res != *"ip:"* ]];then
        res=$(IgnoreQuote=True timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh temp.ps1 2>/dev/null)
    fi
    echo "$res" | tee -a ../samples/temp1.txt
done
cd ../samples
./postprocessing.py temp1.txt result1.txt

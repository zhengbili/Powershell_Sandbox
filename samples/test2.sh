export PATH=$PWD:$PATH
rm temp2.txt
cd ../sandbox
for i in $(ls ../samples/Second-Stage/);do
    echo $i | tee -a ../samples/temp2.txt
    ../samples/preprocessing.py ../samples/Second-Stage/$i temp.ps1
    res=$(timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh temp.ps1 2>/dev/null)
    if [[ $res != *"ip:"* ]];then
        res=$(IgnoreQuote=True timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh temp.ps1 2>/dev/null)
    fi
    echo "$res" | tee -a ../samples/temp2.txt
done
cd ../samples
./postprocessing.py temp2.txt result2.txt

export PATH=$PWD:$PATH
cd ../sandbox
for i in $(ls ../samples/Second-Stage/);do
    echo $i
    res=$(timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh ../samples/Second-Stage/$i 2>/dev/null)
    if [[ $res != *"ip:"* ]];then
        res=$(IgnoreQuote=True timeout -k 20s 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh ../samples/Second-Stage/$i 2>/dev/null)
    fi
    echo "$res"
done

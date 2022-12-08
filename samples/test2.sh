for i in $(ls ./Second-Stage/)
    do echo $i
    timeout 10s ../src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh ./Second-Stage/$i 2>/dev/null
done

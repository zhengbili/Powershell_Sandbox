#!/usr/bin/env pwsh
Import-Module ./build.psm1
Start-PSBootstrap
Start-PSBuild
#./src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh

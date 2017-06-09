SET mypath=%~dp0
echo %mypath:~0,-1%
cd /d %mypath%

"E:\Program Files\Microsoft SDKs\Windows\v7.0\Bin\signtool.exe"  sign /fMyCert.pfx /t http://timestamp.verisign.com/scripts/timstamp.dll MyControl.exe
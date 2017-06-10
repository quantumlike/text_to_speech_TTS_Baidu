SET mypath=%~dp0
echo %mypath:~0,-1%
cd /d %mypath%

"E:\Program Files\Microsoft SDKs\Windows\v7.0\Bin\signtool.exe"  sign /a /s MY /t http://timestamp.verisign.com/scripts/timstamp.dll /v boy_voice.exe

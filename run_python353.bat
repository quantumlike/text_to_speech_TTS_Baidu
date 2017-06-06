SET mypath=%~dp0
echo %mypath:~0,-1%
cd /d %mypath%
rem set path=E:\python\baidu;%PATH%
set path=C:\Python\Python353-32\Scripts\;C:\Python\Python353-32\;%PATH%
"C:\Python\Python353-32\python.exe" %mypath%baidu_voice.py 

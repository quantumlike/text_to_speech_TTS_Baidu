SET mypath=%~dp0
echo %mypath:~0,-1%
cd /d %mypath%
rem set path=E:\python\baidu;%PATH%
"C:\Users\ywang\AppData\Local\Programs\Python\Python36-32\python.exe" %mypath%baidu_voice.py 

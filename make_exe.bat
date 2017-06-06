SET mypath=%~dp0
echo %mypath:~0,-1%
cd /d %mypath%
rem set path=C:\Users\ywang\AppData\Local\Programs\Python\Python36-32;%PATH%
set path=C:\Python\Python353-32\Scripts\;C:\Python\Python353-32\;%PATH%
"C:\Python\Python353-32\Scripts\pyinstaller.exe" -F %mypath%baidu_voice.py
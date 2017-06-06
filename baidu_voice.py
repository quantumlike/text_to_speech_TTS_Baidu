# -*- coding=gb2312 -*-

import urllib
import urllib.request
import urllib
import json
import urllib.parse
import base64
import os
import wave
import pyaudio
import struct
#import mp3play

#import time
#from subprocess import call
#from gtts import gTTS
#import os

#from pygame import mixer # Load the required library

# from yudong_package import vlc

import subprocess

import codecs

Api_Key='5z2KZOQn51RoQiHDR84OKF2U'
Secrect_Key='f1b1b5de59ece11c3353016b8a394fa9'
url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+Api_Key+'&client_secret='+Secrect_Key
ServerUrl='http://tsn.baidu.com/text2audio'
res = urllib.request.urlopen(url).read().decode('utf8')


data = json.loads(res)
token = data['access_token']    #got token
print('token get success:',token)

# text="hello world"
# text=u'\u4f60\u597d'
text = u'我是钰栋，我住在密歇根。我喜欢打篮球。我有一个iphone。'
text = text.encode('utf-8')
lan='zh'
cuid='YourCUID'
per='0'
date={'tex':text,'lan':lan,'cuid':cuid,'ctp':1,'tok':token,'per':per}
date_urlencode=urllib.parse.urlencode(date)
print(type(date_urlencode)) ##check date_urlencodede date type
r=urllib.request.urlopen(ServerUrl,str.encode(date_urlencode))
print(r.getcode())
result=r.read()
file=open(r"voice.mp3","wb")
file.write(result)
file.close()

# os.system("voice.mp3") #call sys app to play the voice
# call(["vlc", "test.mp3"])

# mixer.init()
# mixer.music.load('E:/python/baidu/voice.mp3')
# mixer.music.play()

# vlc.Instance()
# p=vlc.MediaPlayer('E:/python/baidu/voice.mp3')
# p.play()


# subprocess.call(['C:/Program Files/VideoLAN/VLC/vlc.exe', 'E:/python/baidu/voice.mp3'])
subprocess.call(['C:/Program Files (x86)/Windows Media Player/wmplayer.exe', 'E:/python/baidu/voice.mp3'])

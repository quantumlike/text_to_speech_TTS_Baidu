# -*- coding=gb2312 -*-

import urllib
import urllib.request
import json
import urllib.parse
import base64
import os
import wave
import pyaudio
import struct


import codecs

from tkinter import *
from tkinter import filedialog

def callback():
    filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    # print (root.filename)

    f = codecs.open(filename, 'r')
    text = f.read()
    f.close()
    
    Api_Key='5z2KZOQn51RoQiHDR84OKF2U'
    Secrect_Key='f1b1b5de59ece11c3353016b8a394fa9'
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+Api_Key+'&client_secret='+Secrect_Key
    ServerUrl='http://tsn.baidu.com/text2audio'
    res = urllib.request.urlopen(url).read().decode('utf8')


    data = json.loads(res)
    token = data['access_token']    #got token
    # print('token get success:',token)



    # text="hello world"
    # text=u'\u4f60\u597d'

    # text = u'我是欲动，我住在密歇根。我喜欢打篮球。我有一个iphone。'
    # text = text.encode('utf-8')

    lan='zh'
    cuid='YourCUID'
    per='0' # per: reader selection. 0 is boy, 1 is girl. 3 is boy with emotion. 4 is girl with emotion. default is 1. 1 and 3 is used in this project.
    date={'tex':text,'lan':lan,'cuid':cuid,'ctp':1,'tok':token,'per':per}
    date_urlencode=urllib.parse.urlencode(date)
    # print(type(date_urlencode)) ##check date_urlencodede date type
    r=urllib.request.urlopen(ServerUrl,str.encode(date_urlencode))
    # print(r.getcode())
    result=r.read()
    file=open(r"voice.mp3","wb")
    file.write(result)
    file.close()

    os.startfile('voice.mp3')  # good
    
# Define a main() function that prints a little greeting.
def main():

  root = Tk()
  root.withdraw() 
  mybutton = Button(root, text='select text file', command=callback())
  mybutton.pack() # etc

  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
    

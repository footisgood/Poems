from aip import AipSpeech
import pygame
import time



""" 你的 APPID AK SK """
APP_ID = '11162123'
API_KEY = '1aLVLZBgBu0js571O8i7TnbG'
SECRET_KEY = '6VoH8Sm4Wbd9qfhKnG6XEI2Zjt9zj9R5'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#vol音量，取值0-15，默认为5中音量 per:发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
#spd语速，取值0-9，默认为5中语速	pit	音调，取值0-9，默认为5中语调
result  = client.synthesis('春色满园关不住，一枝红杏出墙来', 'zh', 1, {
    'vol': 5, 'per' : 2 ,'spd': 5
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

pygame.mixer.init()
pygame.mixer.music.load("auido.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    #检查音乐流播放，有返回True，没有返回False
    #如果没有音乐流则选择播放
    time.sleep(0.3)

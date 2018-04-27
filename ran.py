import random
from aip import AipSpeech
import pygame
import time
import os

def speak(filename , str):
    result = client.synthesis(str, 'zh', 1, {
        'vol': 5, 'per': 2, 'spd': 4
    })
    filename = 'audio\\' + filename
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        while True:
            try:
                with open(filename, 'wb') as f:
                    f.write(result)
                break
            except IOError:
                print('Error:文件写入失败，再一次尝试...')
    f.close()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.3)
    pygame.mixer.music.stop()

def chuti(now_list,hide):
    k=len(now_list)
    no=random.randrange(k-1)
    s_timu = ''
    for i in range(k-1):
        if i != no :
            print (now_list[i] , end='   ')
            s_timu = s_timu + now_list[i]
        else:
            print (hide*k ,  end='   ')
            s_timu = s_timu + '什么'
    time.sleep(1)
    filename=str(time.time())
    filename=filename.replace('.','k')
    filename += 'audio.mp3'
    speak(filename , s_timu)

if __name__ == '__main__':
    APP_ID = '11162123'
    API_KEY = '1aLVLZBgBu0js571O8i7TnbG'
    SECRET_KEY = '6VoH8Sm4Wbd9qfhKnG6XEI2Zjt9zj9R5'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    a=open(r'1.txt','r',encoding='gbk').read()
    data=a.split('\n')
    n=len(data)
    print ('-'*100)
    print ('|                       总载入著名诗句%d句'%(n) + ' '*60 + '|')
    print ('-'*100)
    weak=[]
    for i in range(1):
        num=random.randrange(len(data))
        now_s=data[num].replace('。','，')
        now_s=data[num].replace('？','，')
        now_list=now_s.split('，')
        print ('No.%d :'%(i+1) , end='')
        chuti(now_list , '__')
        state=input('...')
        if state == 'x':
            weak += [now_s]
    print (u'刚才发现你掌握不好的诗句共有 %d 句，分别是：'%(len(weak)))
    for i in range(len(weak)):
        print (weak[i])
    pygame.quit()
    path = 'audio\\'
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
            print('deleted ' + path_file)

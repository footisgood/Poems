import random
from aip import AipSpeech
import pygame
from pygame.locals import *
import time
import os

def speak(filename , str):
    result = client.synthesis(str, 'zh', 1, {
        'vol': 5, 'per': 1, 'spd': 4 , 'pit' :4
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
    k=len(now_list)  #有几句
    n=len(now_list[0])  #一句有几个字
    no=random.randrange(k-1)
    s_timu = ''
    s_out=''
    for i in range(k-1):
        if i != no :
            s_out=s_out + now_list[i] + '  '
            s_timu = s_timu + now_list[i]
        else:
            s_out = s_out + hide*k + '  '
            s_timu = s_timu + '什么'
    print (s_out)
    text_surface = font.render(s_out, True, (0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (100, 200))
    pygame.display.update()

    filename=str(time.time())
    filename=filename.replace('.','k')
    filename += 'audio.mp3'
    speak(filename , s_timu)

def show_the_question(no):
    global now_s , now_list ,data
    num = random.randrange(len(data))
    now_s = data[num].replace('。', '，')
    now_s = data[num].replace('？', '，')
    now_list = now_s.split('，')
    print('No.%d :' % (no), end='')
    chuti(now_list, '____')

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

    pygame.init()
    screen = pygame.display.set_mode((985 , 696), 0, 32)
    font = pygame.font.Font("msyhbd.ttc", 30)
    text_surface = font.render(u"准备开始啦", True, (0, 0, 255))
    background = pygame.image.load("background1.jpg").convert()
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (100, 110))
    pygame.display.update()
    weak=[]
    no=0
    goon = True
    while goon :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.exit()
            if event.type == KEYDOWN :
                if event.key == K_RIGHT:  # 获取键盘字母a
                    no +=1
                    show_the_question(no)
                elif event.key == K_LEFT:  # 获取键盘空格键
                    pass
                elif event.key == K_SPACE:  # 获取键盘左键
                    goon = False

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

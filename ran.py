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

def ShowIt(no , s_out,s_speak):
    text_surface = font.render(str(no) + '.' + s_out, True, (0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (100, 260))
    pygame.display.update()

    filename=str(time.time())
    filename=filename.replace('.','k')
    filename += 'audio.mp3'
    speak(filename , s_speak)

def ChuTiMu(no):  #出第no题，挑选进入now_list的列表
    global now_s , now_list , data , all
    num = random.randint(0,len(data))
    now_s = data[num].replace('。', '，')
    now_s = data[num].replace('？', '，')
    now_list = now_s.split('，')
    k=len(now_list)  #有几句
    n=len(now_list[0])  #一句有几个字
    hiddenno=random.randrange(k-1)     #要隐藏的是第几句
    s_speak = ''  #s_speak是读出来的，s_out是显示出来的
    s_out=''
    hide='_'
    for i in range(k-1):
        if i != hiddenno :
            s_out=s_out + now_list[i] + '  '
            s_speak = s_speak + now_list[i]
        else:
            s_out = s_out + hide*n + '  '
            s_speak = s_speak + '什么'
    all.setdefault(no, ['' , '' , 0])
    all[no] = [s_out , s_speak , num]   #all={1:['第一题的显示','第一题的读音' , 在题库data中的序号]
    print('No.%d :' % (no), s_out)
    ShowIt(no , s_out , s_speak)

if __name__ == '__main__':
    APP_ID = '11162123'
    API_KEY = '1aLVLZBgBu0js571O8i7TnbG'
    SECRET_KEY = '6VoH8Sm4Wbd9qfhKnG6XEI2Zjt9zj9R5'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    a=open(r'1.txt','r',encoding='gbk').read()
    data=a.split('\n')   #data就是所有的古诗词，一首一行
    n=len(data)
    print ('-'*100)
    print ('|                       总载入著名诗句%d句'%(n) + ' '*60 + '|')
    print ('-'*100)

    pygame.init()
    screen = pygame.display.set_mode((985 , 696), 0, 32)
    font = pygame.font.Font("msyhbd.ttc", 30)
    text_surface = font.render(u"按→就可以开始啦……", True, (200, 0, 255))
    background = pygame.image.load("background1.jpg").convert()
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (100, 210))
    pygame.display.update()
    all={}  #所有出的题目
    #all的数据结构为：all={1:['第一题的显示','第一题的读音'，该题目在题库data中的序号]
    weak=[]   #weak记录掌握不好的序号就可以了
    no=0
    goon = True
    while goon :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.exit()
            if event.type == KEYDOWN :
                if event.key == K_RIGHT:  # 获取键盘字母a
                    no = len(all)
                    no +=1
                    ChuTiMu(no)  #出题no，并把这个题目append到all
                elif event.key == K_LEFT:
                    if no>1 :
                        no -= 1
                        ShowIt(no , all[no][0] , all[no][1])
                elif event.key == K_x:
                    weak.append(all[no][2])
                elif event.key == K_SPACE:
                    goon = False
    for i in range(3):
        print ('*'*100)
    print ('*************结束游戏************')
    print (u'刚才发现你掌握不好的诗句共有 %d 句，分别是：'%(len(weak)))

    for i in range(len(weak)):
        print (data[weak[i]])
    pygame.quit()
    path = 'audio\\'
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
            # print('deleted ' + path_file)

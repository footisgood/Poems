import random
import time

def chuti(now_list,hide):
    k=len(now_list)
    no=random.randrange(k-1)
    # print (k,no)
    for i in range(k-1):
        if i != no :
            print (now_list[i] , end='   ')
        else:
            print (hide*k ,  end='   ')


a=open(r'1.txt','r',encoding='gbk').read()
data=a.split('\n')
n=len(data)
print ('-'*100)
print ('|                       总载入著名诗句%d句'%(n) + ' '*60 + '|')
print ('-'*100)
weak=[]
for i in range(3):
    num=random.randrange(len(data))
    now_s=data[num].replace('。','，')
    now_s=data[num].replace('？','，')
    now_list=now_s.split('，')
    print ('No.%d :'%(i+1) , end='')
    chuti(now_list,'__')
    state=input('...')
    if state == 'x':
        weak += [now_s]
print ('刚才发现你掌握不好的诗句是：')
for i in range(len(weak)):
    print (weak[i])

import numpy as np
import langid
import re
import emoji
import os
from emoji import UNICODE_EMOJI

def is_emoji(s):
    count = 0
    for emoji in UNICODE_EMOJI:
        count += s.count(emoji)
        if count > 1:
            return False
    return bool(count)

pathin = 'F:/program/data/data1'
pathout = 'F:\program\dialog_data2\data1\\'
path_list = os.listdir(pathin)
#print(path_list)
for filename in path_list:
    test0 = np.load(os.path.join(pathin,filename))
    num=test0[-1]
    m={}
    emo=[]
    
    for i in range(num):
        item=test0[i]
        length=1
        fn=item['id']
        for it in item['dialogues']:
            di=it[2]
            #di2=filter_emoji()
            di2=emoji.emoji_count(di)
            #print(di2)#统计表情的个数
            #print(di)#显示对话
            m=dict([(i,di.split().count(i)) for i in di.split()])
            #print(m)#统计单词个数
            arr=di.split()#切分出单词
            en=0
            arr1=[]
            arr_emo=[]#存储表情
            for a in arr:#遍历每个单词，看是否是表情
                if(not is_emoji(a)):#不是表情
                    en=1#表示可以存入对话list
                if(en==1):
                    arr1.append(a)
                else :
                    arr_emo.append(a)
            #print(len(arr1))
            if(len(arr1)>100 or len(arr1)<2 or item['turns_number']<3):
                length=0
        if(length==1):
            np.save(os.path.join(pathout+str(fn)+".npy"),item)
            print("done!!")

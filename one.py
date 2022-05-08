
# -*- coding:utf-8 -*-
from tkinter import dialog
import langid
import numpy as np
import json
import os

#dialogues里有至少三个人的对话，它的值是一个二维的array，每一个包括id，name，和具体的对话
def lang_by_langid(para_text):
    '''
    语种识别,根据langid包
    '''
    ret = langid.classify(para_text)
    #print(f"langid:{ret}")
    return ret[0]

pathin = 'F:/program/dialog_data/json'
pathout = 'F:\program\data\data1\\'
path_list = os.listdir(pathin)

for filename in path_list:   
    with open(os.path.join(pathin,filename),'r',encoding="utf8") as fp:
        json_data = json.load(fp)#依次读取文件

    fin=[]
    k=0
    num=json_data[-1]
    for i in range(num):
        item=json_data[i]
        en=1
        for it in item['dialogues']:
        #for i in range(len(item['dialogues'])):
            #print(len(item['dialogues']))#得到每个对话的人数是多少个
            #print(it[2])#打印出每句对话
            temp=lang_by_langid(it[2])#识别语言类别
            if(temp != 'en'):#不是英文对话的话，则删除
                en=0
        if(en==1):
            fin.append(item)
            k=k+1
    filename=filename.split('.')[0]
    fin.append(k)
    np.save(os.path.join(pathout+filename+".npy"),fin)
    print("done!!!")

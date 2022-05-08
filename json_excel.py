# -*- coding:utf-8 -*-
import os
import csv
import json
import pandas as pd
import numpy as np
#---------用pandas库，filename写你自己的--------------

pathin = 'F:/program/dialog_data/json'
pathout = 'F:\program\excel\\'
path_list = os.listdir(pathin)

for filename in path_list:   
    pd.read_json(os.path.join(pathin,filename)).to_excel(os.path.join(pathout+filename.split('.')[0]+".excel")) 
    '''with open(os.path.join(pathin,filename),'r',encoding="utf8") as fp:
        json_data = json.load(fp)#依次读取文件
    frame=pd.DataFrame(json_data)
    #print(frame)
    filename=filename.split('.')[0]
    frame.to_excel(os.path.join(pathout+filename+".excel"))'''
    print("done!!!")

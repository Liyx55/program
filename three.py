import numpy as np
import langid
test0=np.load("F:/program/dialog_data2/data1/16978748.npy")
print(test0)

#print(langid.classify("💖"))

"""
#with open("F:/program/data/data1/500.npy") as fp:
test0 = np.load("F:/program/data/data1/500.npy")
num=test0[-1]
m={}
fin=[]
emo=[]

for i in range(num):
    item=test0[i]
    length=1

    for it in item['dialogues']:
        di=it[2]#取具体的对话
        #di2=filter_emoji()
        #di2=emoji.emoji_count(di)
        #print(di2)#统计表情的个数
        #print(di)#显示对话
        #di_no_emoji=emoji.demojize(di)
        m=dict([(i,di.split().count(i)) for i in di.split()])
        print(m)#统计单词个数
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
        print(len(arr1))
        if(len(arr1)>100 or len(arr1)<2 or item['turns_number']<3):
            length=0
    if(length==1):
        fin.append(item)
np.save("F:/program/data/500.npy",fin)
print("done!!!")
"""

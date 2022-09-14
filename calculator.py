#!/usr/bin/python3
from tkinter import W
import pandas as pd

def calculator(average_num):
    for byte_num in range(0,1):
        memory_hierarchy = 'L3'
        calculator_name ="./calculator_result"+"_average"+str(average_num)+"_byte"+str(byte_num)+".txt"
        f=open(calculator_name,'w')
        for sample_num in range(1,21):
            sample_num_add = sample_num*1000 #for L3
            corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
            df=pd.read_table(corrname,sep=' ', header=None, names=['correlation'])
            corr=df[['correlation']]
            corr = corr.head(256)
            max_corr = corr.max()
            corr['rank_by_first']=corr.rank(method='first',ascending=False)
            average_sum = 0 
            average_num_range = average_num +2
            for i in range(2,average_num_range):
                corr_temporal=corr.loc[corr.rank_by_first==i,['correlation']]
                average_sum+=corr_temporal.iloc[0]['correlation']
            average=average_sum/average_num
            cal=max_corr.iloc[0]/average
            data = "%f\n" % cal
            f.write(data)
        f.close
for j in range(10,250,10):
    calculator(j)

calculator(255)
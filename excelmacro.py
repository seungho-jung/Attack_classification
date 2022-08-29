#!/usr/bin/python3
import pandas as pd
for sample_num in range(1,21):
    sample_num_add = sample_num*50000
    corrname_0="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(0)+".txt"
    corrname_1="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(1)+".txt"
    df_0 = pd.read_table(corrname_0 ,sep=' ', header=None, names=['correlation'+str(0)])
    df_1 = pd.read_table(corrname_1 ,sep=' ', header=None, names=['correlation'+str(1)])
    result = pd.concat([df_0,df_1],axis=1)
    for j in range(2,16):
        corrname="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(j)+".txt"
        df = pd.read_table(corrname ,sep=' ', header=None, names=['correlation'+str(j)])
        result = pd.concat([result,df],axis=1)
        result.to_csv("temporal"+str(sample_num_add)+".csv")


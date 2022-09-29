#!/usr/bin/python3
import pandas as pd
for sample_num in range(20,21):
    memory_hierarchy = 'mix_million'
#    sample_num_add = sample_num*50000
#    corrname_0="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(0)+".txt"
#    corrname_1="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(1)+".txt"
    sample_num_add = sample_num*500000 #for L1
    corrname_0="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(0)+".txt"
    corrname_1="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(1)+".txt"

    #sample_num_add = sample_num*1000 #for L3
    #corrname_0="./L3_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(0)+".txt"
    #corrname_1="./L3_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(1)+".txt"

    df_0 = pd.read_table(corrname_0 ,sep=' ', header=None, names=['correlation'+str(0)])
    df_1 = pd.read_table(corrname_1 ,sep=' ', header=None, names=['correlation'+str(1)])
    result = pd.concat([df_0,df_1],axis=1)
    for j in range(2,16):
        corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(j)+".txt"    
        #corrname="./L3_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(j)+".txt"
        df = pd.read_table(corrname ,sep=' ', header=None, names=['correlation'+str(j)])
        result = pd.concat([result,df],axis=1)
        result.to_csv("temporal"+str(sample_num_add)+".csv")


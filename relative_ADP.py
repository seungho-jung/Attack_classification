#!/usr/bin/python3
import pandas as pd
#relative_ADP="."+"/"+"realtive_ADP"+".txt"
#f = open(relative_ADP, 'a')
for sample_num in range(1,21):
    #sample_num_add = sample_num*50000
    sample_num_add = sample_num*1000 #for L3
    for j in range(8,9):
        #corrname="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(j)+".txt"
        corrname="./L3_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(j)+".txt"    
        df_1 = pd.read_table(corrname ,sep=' ', header=None, names=['correlation'])
        print(df_1)
        x = df_1.loc[35]/0.01*100
#        print(x)

#f.close()

#!/usr/bin/python3

import pandas as pd
for sample_num in range(1,21): #21
    sample_num_add = sample_num*50000
    kurtosis_name="./kurtosis_result"+"/"+"kurtosis_"+str(sample_num_add)+".txt"
    f = open(kurtosis_name, 'w')
    for byte_num in range(0,16):
        foldername="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
        df=pd.read_table(foldername,sep=' ', header=None, names=['correlation'])
        corr=df[['correlation']]
        corr = corr.head(256)
#        max_corr = corr.max()
#        print(max_corr.iloc[0])
#        corr_byte = corr.index[corr['correlation'] == max_corr.iloc[0]]
#        print(corr_byte[0])
        cal_kurt = corr.kurt()
#        print(cal_kurt)
        data = "%f\n" % cal_kurt
        f.write(data)
    f.close

#library(moments)
#data=rnorm(100)
#skewness(data)
#kurtosis(data)

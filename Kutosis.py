#!/usr/bin/python3

import pandas as pd
for sample_num in range(1,21):
    sample_num_add = sample_num*50000
    kurtosis_name="./kurtosis_result"+"/"+"kurtosis_"+str(sample_num_add)+".txt"
    f = open(kurtosis_name, 'w')
    for byte_num in range(0,16):
        foldername="./attack_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
        df=pd.read_table(foldername,sep=' ', header=None, names=['correlation'])
        corr=df[['correlation']]
        corr = corr.head(256)
        kurt = corr.kurt()
        #axis=1 적용?
#        print(kurt)
        data = "%f\n" % kurt
        f.write(data)
    f.close

#library(moments)
#data=rnorm(100)
#skewness(data)
#kurtosis(data)

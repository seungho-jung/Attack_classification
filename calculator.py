#!/usr/bin/python3
import pandas as pd

def calculator(average_num):
    for byte_num in range(1,2):
        memory_hierarchy = 'L3'
        calculator_name ="./"+memory_hierarchy+"_average/"+"_average"+str(average_num)+"_byte"+str(byte_num)+".txt"
        f=open(calculator_name,'w')
        for sample_num in range(1,21):
            sample_num_add = sample_num*50000 #for L3
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
                if corr_temporal.iloc[0]['correlation'] < 0 :
                    corr_temporal.iloc[0]['correlation'] = 0
                average_sum+=corr_temporal.iloc[0]['correlation']
            average=average_sum/average_num
            cal=max_corr.iloc[0]/average
            data = "%f\n" % cal
            f.write(data)
        f.close

for j in range(10,20,10):
    calculator(j)

calculator(255)

for byte_num in range(0,16):
    memory_hierarchy = 'L3'
    lrd_1="./"+memory_hierarchy+"_average/"+"_average"+str(10)+"_byte"+str(byte_num)+".txt"
    lrd_2="./"+memory_hierarchy+"_average/"+"_average"+str(20)+"_byte"+str(byte_num)+".txt"
    df_1 = pd.read_table(lrd_1,sep=' ', header=None, names=['lrd'+str(10)])
    df_2 = pd.read_table(lrd_2,sep=' ', header=None, names=['lrd'+str(20)])
    result = pd.concat([df_1,df_2],axis=1)
    for average_count in range(30,260,10):
        lrdname="./"+memory_hierarchy+"_average/"+"_average"+str(average_count)+"_byte"+str(byte_num)+".txt"
        df = pd.read_table(lrdname ,sep=' ', header=None, names=['lrd'+str(average_count)])
        result = pd.concat([result,df],axis=1)
    lrd_last="./"+memory_hierarchy+"_average/"+"_average"+str(255)+"_byte"+str(byte_num)+".txt"
    df_last=pd.read_table(lrd_last,sep=' ', header=None, names=['lrd'+str(255)])
    result = pd.concat([result,df_last],axis=1)
    result.to_csv("./"+memory_hierarchy+"_average/average_temporal"+str(byte_num)+".csv")

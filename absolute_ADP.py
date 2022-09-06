#!/usr/bin/python3
import pandas as pd

def cal_lrd(rank):
    for sample_num in range(1,21):
        #sample_num_add = sample_num*50000
        sample_num_add = sample_num*1000 #for L3
        memory_hierarchy = 'L3'
        lrd_name="./"+memory_hierarchy+"_lrd"+"/"+str(rank)+"lrd_"+str(sample_num_add)+".txt"
        f = open(lrd_name, 'w')
        for byte_num in range(0,16):
            corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
            df=pd.read_table(corrname,sep=' ', header=None, names=['correlation'])
            corr=df[['correlation']]
            corr = corr.head(256)
            max_corr = corr.max()
#            max_corr_num = max_corr.loc['correlation']
            corr['rank_by_dense']=corr.rank(method='first',ascending=False)
            total_distance=0
            rank_range = rank + 2
            for i in range(2,rank_range):
                corr_temporal=corr.loc[corr.rank_by_dense==i,['correlation']]
                distance=max_corr-corr_temporal.iloc[0]['correlation']
                total_distance=total_distance+distance.loc['correlation']
            nkp_distance=total_distance/rank
            total_distance=0
            for i in range(2,rank_range):
                corr_temporal=corr.loc[corr.rank_by_dense==i,['correlation']]
                distance=max_corr-corr_temporal.iloc[0]['correlation']
                if nkp_distance>=distance.loc['correlation']:
                    total_distance=total_distance+nkp_distance
                else :
                    total_distance=distance.loc['correlation']
            lrd = rank/total_distance
            data = "%f\n" % lrd
            f.write(data)
        f.close

for i in range(10,256):
    cal_lrd(i)


for j in range(10,256):
    memory_hierarchy = 'L3'
    lrd_1="./"+memory_hierarchy+"_lrd"+str(j)+"/lrd_"+str(1000)+".txt"
    lrd_2="./"+memory_hierarchy+"_lrd"+str(j)+"/lrd_"+str(2000)+".txt"
    df_1 = pd.read_table(lrd_1,sep=' ', header=None, names=['lrd'+str(1000)])
    df_2 = pd.read_table(lrd_2,sep=' ', header=None, names=['lrd'+str(2000)])
    result = pd.concat([df_1,df_2],axis=1)
    for sample_num in range(3,21):
        sample_num_add = sample_num*1000 #for L1
        lrdname="./"+memory_hierarchy+"_lrd"+str(j)+"/lrd_"+str(sample_num_add)+".txt"
        df = pd.read_table(lrdname ,sep=' ', header=None, names=['lrd'+str(sample_num_add)])
        result = pd.concat([result,df],axis=1)
        result.to_csv("./"+memory_hierarchy+"_lrd"+"/lrd_temporal"+str(j)+".csv")
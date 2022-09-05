#!/usr/bin/python3
import pandas as pd

def cal_lrd(rank):
    for sample_num in range(1,2):
        #sample_num_add = sample_num*50000
        sample_num_add = sample_num*1000 #for L3
        memory_hierarchy = 'L3'
        for byte_num in range(0,1):
            corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
            df=pd.read_table(corrname,sep=' ', header=None, names=['correlation'])
            corr=df[['correlation']]
            corr = corr.head(256)
            max_corr = corr.max()
            max_corr_num = max_corr.loc['correlation']
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
            print(lrd)

cal_lrd(10)
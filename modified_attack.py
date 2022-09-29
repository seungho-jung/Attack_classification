#!/home/seungho/anaconda3/envs/project/bin/python3

import pandas as pd
from multiprocessing import Pool

def cal_correlation(byte_num):
    for k in range(1,11):
        memory_hierarchy = 'width_32byte'
        k_1 = k*1000 #for L1
        #k_1 = k*1000 #for L3
        foldername="./memory_request/byte"+str(byte_num)
        corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(k_1)+"corr_"+str(byte_num)+".txt"
        cyclename="./"+memory_hierarchy+"_cycle/output_tot_cycle_"+memory_hierarchy+".txt"
        f = open(corrname, 'w')

        df_2 = pd.read_table(cyclename ,sep=' ', header=None, names=['sample', 'cycle'])
        y = df_2[['cycle']]
        #print(y)
        y_temporal = y.head(k_1)
        #print(y_temporal)

        for i in range(0, 256):
            filename =foldername+"/key"+str(i)
            df_1 = pd.read_table(filename ,sep=' ', header=None, names=['sample', 'mem_request'])
            x = df_1[['mem_request']]
            x_temporal = x.head(k_1)
            #df_2 = pd.read_table('./cycle_data/cycle_default',sep=' ', header=None, names=['sample', 'cycle'])
            #df_2 = pd.read_table('./L3_cycle/output_tot_cycle_DRAM.txt',sep=' ', header=None, names=['sample', 'cycle'])

            z= x_temporal['mem_request'].corr(y_temporal['cycle'])
            data = "%f\n" % z
            f.write(data)
        f.close()

def correlation():
    num_cores = 4
    pool = Pool(num_cores)
    pool.map(cal_correlation,range(0,16))
    pool.close()
    pool.join()

correlation()
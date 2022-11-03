#!/home/seungho/anaconda3/envs/project/bin/python3

import pandas as pd
from multiprocessing import Pool

def cal_correlation(byte_num):
    for k in range(1,11):
        memory_hierarchy = 'DRAM'
        #sample stride
        k_1 = k*1000 #for L1
        #file location 
        foldername="./memory_request/byte"+str(byte_num)
        corrname="./"+memory_hierarchy+"_correlation_result"+"/"+str(k_1)+"corr_"+str(byte_num)+".txt"
        cyclename="./"+memory_hierarchy+"_cycle/output_tot_cycle_"+memory_hierarchy+".txt"
        f = open(corrname, 'w')

        df_2 = pd.read_table(cyclename ,sep=' ', header=None, names=['sample', 'cycle'])
        y = df_2[['cycle']]
        y_temporal = y.head(k_1)
        #calculate correlation
        for i in range(0, 256):
            filename =foldername+"/key"+str(i)
            df_1 = pd.read_table(filename ,sep=' ', header=None, names=['sample', 'mem_request'])
            x = df_1[['mem_request']]
            x_temporal = x.head(k_1)

            z= x_temporal['mem_request'].corr(y_temporal['cycle'])
            data = "%f\n" % z
            f.write(data)
        f.close()
#multi processing
def correlation():
    num_cores = 4
    pool = Pool(num_cores)
    pool.map(cal_correlation,range(8,16))
    pool.close()
    pool.join()

correlation()
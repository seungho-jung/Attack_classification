#!/home/seungho/anaconda3/envs/project/bin/python3

import pandas as pd
for k in range(1,21):
    k_1 = k*50000
    for j in range(0,16):
        foldername="./memory_request/byte"+str(j)
        corrname="./attack_result"+"/"+str(k_1)+"corr_"+str(j)+".txt"
        f = open(corrname, 'w')
        for i in range(0, 256):
            filename =foldername+"/key"+str(i)
            df_1 = pd.read_table(filename ,sep=' ', header=None, names=['sample', 'mem_request'])
            x = df_1[['mem_request']]
            x = x.head(k_1)
            df_2 = pd.read_table('./cycle_data/cycle_default_1',sep=' ', header=None, names=['sample', 'cycle'])
            y = df_2[['cycle']]
            y = y.head(k_1)
            df = pd.concat([x,y],axis =1)
            x= df['mem_request']
            y= df['cycle']
            z= x.corr(y)
            data = "%f\n" % z
            f.write(data)
        f.close()
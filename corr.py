import pandas as pd
f = open("Downloads/key0/corr_0.txt", 'w')

for i in range(0, 256):
    filename ="Downloads/key0/data_"+str(i)+".txt"
    df_1 = pd.read_table(filename ,sep=' ', header=None, names=['sample', 'mem_request'])
    x = df_1[['mem_request']]
    x = x.head(20000)
    df_2 = pd.read_table('Downloads/key0/output_tot_cycle_20000.txt',sep=' ', header=None, names=['sample', 'cycle'])
    y = df_2[['cycle']]
    df = pd.concat([x,y],axis =1)
    x= df['mem_request']
    y= df['cycle']
    z= x.corr(y)
    data = "%f\n" % z
    f.write(data)
    
    f.close()
#!/usr/bin/python3
import pandas as pd

def calculator(mem_hierarchy,average_num):
    for byte_num in range(0,16):
        memory_hierarchy = mem_hierarchy
        calculator_name ="./sample_issue/"+memory_hierarchy+"_calculation/result"+"_average"+str(average_num)+"_byte"+str(byte_num)+".txt"
        f=open(calculator_name,'w')
        for sample_num in range(1,17):
            if sample_num == 7 :
                pass
            elif sample_num == 8 :
                pass
            else :
                sample_num_add = sample_num*50000 #for L3
                corrname="./sample_issue/"+memory_hierarchy+"_correlation_result"+"/"+str(sample_num_add)+"corr_"+str(byte_num)+".txt"
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

def gen_execel(memory_hierarchy,average_num):
    mem_hierarchy = memory_hierarchy
    lrd_1="./sample_issue/"+mem_hierarchy+"_calculation/result"+"_average"+str(average_num)+"_byte"+str(0)+".txt"
    lrd_2="./sample_issue/"+mem_hierarchy+"_calculation/result"+"_average"+str(average_num)+"_byte"+str(1)+".txt"
    df_1 = pd.read_table(lrd_1,sep=' ', header=None, names=['byte_'+str(0)])
    df_2 = pd.read_table(lrd_2,sep=' ', header=None, names=['byte_'+str(1)])
    result = pd.concat([df_1,df_2],axis=1)

    for byte_num in range(2,16):
        lrdname="./sample_issue/"+mem_hierarchy+"_calculation/result"+"_average"+str(average_num)+"_byte"+str(byte_num)+".txt"
        df = pd.read_table(lrdname ,sep=' ', header=None, names=['byte_'+str(byte_num)])
        result = pd.concat([result,df],axis=1)
    result.to_csv("./sample_issue/"+mem_hierarchy+"_calculation/average_temporal"+str(average_num)+".csv")

# for byte_num in range(0,16):
#     memory_hierarchy = 'CTA_8'
#     lrd_1="./"+memory_hierarchy+"_calculation/result"+"_average"+str(26)+"_byte"+str(byte_num)+".txt"
#     lrd_2="./"+memory_hierarchy+"_calculation/result"+"_average"+str(26)+"_byte"+str(byte_num)+".txt"
#     df_1 = pd.read_table(lrd_1,sep=' ', header=None, names=['byte_'+str(byte_num)])
#     df_2 = pd.read_table(lrd_2,sep=' ', header=None, names=['byte_'+str(byte_num)])
#     result = pd.concat([df_1,df_2],axis=1)
#     for average_count in range(30,260,10):
#         lrdname="./"+memory_hierarchy+"_calculation/result"+"_average"+str(average_count)+"_byte"+str(byte_num)+".txt"
#         df = pd.read_table(lrdname ,sep=' ', header=None, names=['lrd'+str(average_count)])
#         result = pd.concat([result,df],axis=1)
#     lrd_last="./"+memory_hierarchy+"_calculation/result"+"_average"+str(255)+"_byte"+str(byte_num)+".txt"
#     df_last = pd.read_table(lrd_last,sep=' ', header=None, names=['lrd'+str(255)])
#     result = pd.concat([result,df_last],axis=1)
#     result.to_csv("./"+memory_hierarchy+"_calculation/average_temporal"+str(byte_num)+".csv")
for mem in  ['L1','L2','L3']:
    calculator(mem,10)
#calculator(26)
gen_list=['L1','L2','L3']#,'CTA_1','CTA_2','CTA_4','CTA_8','CTA_15','CTA_30']
for i in gen_list:
    gen_execel(i)
#calculator(255)

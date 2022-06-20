
import numpy as np
import pandas as pd


icd=pd.read_csv("data/ICD.csv")
dem=pd.read_csv("data/Demographics.csv")
inp_med=pd.read_csv("data/INP_MED.csv")
out_med=pd.read_csv("data/OUT_MED.csv")
labs=pd.read_csv("data/LABS.csv")
vitals=pd.read_csv("data/Vitals.csv")



temp1=icd.merge(dem,on='idx',how= 'inner')
temp2=temp1.merge (inp_med,on='idx',how='inner' )
temp3=temp2.merge(out_med,on='idx',how= 'inner')
temp4=temp3.merge(labs,on='idx',how= 'inner')
ehr=temp4.merge(vitals,on='idx',how= 'inner')
ehr.dtypes



##modify this list. 
part_of_study=[111,117,1033,1046,1054,1082,1095,1219,1221,1396,1168,139,644]
##

part_of_ehr=ehr[ehr['idx'].isin(part_of_study)]
part_of_ehr.shape


part_of_ehr=part_of_ehr.drop(labels=['Unnamed: 0_x','split_x','split_y','Unnamed: 0_y','split_y'],axis=1)
part_of_ehr=part_of_ehr.drop(labels=['Unnamed: 0'],axis=1)


idx_to_save=[]
idx=part_of_ehr['idx'].unique()
idx_set=set(idx)
for i in range(44):
    temp=part_of_ehr.iloc[i,]['idx'] 
    if temp in idx_set:
        idx_to_save.append(i)
        idx_set.remove(temp)
part_of_ehr=part_of_ehr.iloc[idx_to_save]
part_of_ehr.to_csv("data/processed/part_of_ehr.csv")

print('done!')




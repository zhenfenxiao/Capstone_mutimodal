import pickle
f=open("./series_list.pkl",'rb')
data=pickle.load(f)


part_of_data=[]
for obj in data:
    if obj.study_num in [111,117,1033,1046,1054,1082,1095,1219,1221,1396,1168,139,644]:
        part_of_data.append(obj)
with open("data/processed/series_list.pkl",'wb') as f:
    pickle.dump(part_of_data,f)
print("finish")





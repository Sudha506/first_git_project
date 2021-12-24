list=["sudha","suni","niha"]
sds=[]
for i in list:
    sds.append(i)
print(sds)
print([z for z in list])


name=[["sudha","suni"],["niha","ram"]]
names=[]
for i in name:
    for sds in i:
        names.append(sds)
print(names)  


print([sds for i in name for sds in i])      
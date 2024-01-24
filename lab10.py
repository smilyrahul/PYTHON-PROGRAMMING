str=input("enter string-->>  ")
d={}
for i in str:
   if i in d:
      d[i]+=1
   else:
      d[i]=1
print(d)
      
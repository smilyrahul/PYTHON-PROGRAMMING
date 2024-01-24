with open("rah.txt","r")as file:
   data=file.read()
   f={}
   for i in data:
      if i in f:
         f[i]+=1
      else:
         f[i]=1
         print(f)
         for i in f:
            print(i.f[i])
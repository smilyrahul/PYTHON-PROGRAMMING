def even(x):
    return x%2==0
l=[1,2,3,4,8,12,15,16]
result=filter(even,l)
print("original list",l)
print("filter list",list(result))
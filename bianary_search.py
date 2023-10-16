n=(input("eneter the size of an arary :"))
try:
    array=int(n)
except ValueError as e:
    print(e)
    print("the given input value does matches provide an integer type of value")
    exit(1)

real_array=[]
for i in range(array):
    value=(input(f"enter the value at the index number :{i+1} :"))
    real_array.append(value)

print("given array is as follow\n",real_array)
first=0
last = array - 1
search=input("enter  the elenent that is to be searched :")
while first<=last:
    middle=(first+last)//2
    if real_array[middle] == search:
        print(f"Element found at location {middle + 1} and the element is {search}")
        break
    elif search < real_array[middle]:
        last = middle - 1
    else:
        first = middle + 1
else:
    print("Element not found in the array.")
    
        




        
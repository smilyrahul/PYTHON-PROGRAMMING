list=[1,0,3,4,5]
print(list)
list.append(2)
print("updated list",list)
list.insert(1,9)
print("updated list after inserting",list)
list.remove(9)
print("list after remove() :",list)
list.pop(4)
print("list after pop() :",list)
list.clear()
print("list after clear:",list)
print("length of list",len(list))
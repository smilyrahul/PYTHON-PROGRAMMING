print("dictionary values" )
dict1={"name":"rahul kumar sah","regno":93,"course":"BCA","age":22 }
print(dict1)
print("accessing th item in dict")
print(dict1["name"])
print("using get()")
x=dict1.get("age")
print(x)
print("changing values in dict")
dict1.update({"age":23})
print(dict1)
print("length of dictionary :",len(dict1))
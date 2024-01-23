name = "--you are"
name1= '----cute'
name3 = "Rahul Raj" 
#--------------------for multiple line string excution ---------------- 
    #-------------- ''' ''''(<-- triple single coma use)--------
print( name)
print( name1)
multiline = ''' --- Hii 
 i am rahul raj 
 if you talk , i talk
        & 
 you quite , i quite:
 ----'''
print(multiline)
print("you are ," + name3)
print(name3[0])
print(name3[1])
print(name3[2])
print(name3[3])
print(name3[4])
print(name3[5])
print(name3[6])
print(name3[7])
print(name3[8])
#print(name3[9]) throws a errror ( index out of range)
 
print("use of for loop in strings")
for character in multiline:
 print(character)


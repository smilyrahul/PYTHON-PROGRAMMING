print("Enter the value of first number")
a = int(input())
print("Enter the value of Second number")
b = int(input())

print("Enter the operators for calculation")
d = str(input())

if (d == "+"):
    print("The addition of first and second number = ",a+b)
elif (d == "-"):
    print("The subtraction of first and second number = ",a-b)
elif (d == "*"):
    print("The multiplication of first and second number = ",a*b)
elif (d == "/"):
    print("The division of first and second number = ",a/b)
elif(d== "//"):
     print("The floor division  of first and second number = ",a//b)
elif (d== "**"):
 print("The expenential of first and second number = ",a**b)
elif (d == "%"):
 print("The modul of first and second number = ",a%b)    
else:
    print("You have enter wrong operator, please renter coorect operator")
    print("you can only enter (+,-,*,/,//,**,%) only these operators")
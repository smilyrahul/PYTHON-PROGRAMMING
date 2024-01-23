def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Enter your choice\n1. Addition \n2. Subtraction \n3.Multiplication \n4. Division ")
choice=int(input("-->>"))
a=int(input("enter the valueo of A >>"))
b=int(input("enter the value of B  >>"))
if choice==1:
    print("sum = ",add(a,b))
elif choice==2:
    print("sub = ",sub(a,b))
elif choice==3:
    print("mul = ",mul(a,b))
elif choice==4:
    print("div = ",div(a,b))

    print("enter correct choice")
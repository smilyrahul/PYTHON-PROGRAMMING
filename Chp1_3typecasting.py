
# --------------------------------- Explict typecasting ------------------------------------------

a ="1"
b ="2"
print(a+b) 
# in there output will be "12", bqz a ,b values are in string data type 
# for changing into integer with the help of 'type casting'  so that are --

print( int(a) + int (b) )

#if the value of a b is mix of two data types it will show 'ERROR' when we typecast the values, which is mention below---

# c = "1 rahul"
# d = "2 raj"
# print(c+d)
# c = "1 rahul"
# d = "2 raj"
# print(int (c)+ int (d))


#    ----------------------------------- implict types casting --------------------------------------
#  in this python does typecasting itself and give output in higher priority data type 

r = 12.5
s = 14
u=r+s
print ("sum of implict typecasting are ==" , u)
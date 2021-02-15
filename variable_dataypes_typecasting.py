var1 = "hello world " # string
var2 = 4 # integer variable
var3 = 36.7 # floating variable
var4 = "kuntal"
print(type(var1))
print(var1 + var4) # adding two strings concatentates them

# typecasting is converting from one class to the other
var5 = "32"
var6 = "42"
print(int(var5) + int(var6))
"""
str() # converts to strings
int() # to integer
float() # to float
"""
print(10* "hello world\t") # multiplies hello world 10 times

print("enter a number")
inpum = input() # this allows user to input a number in string
print("the sum with 87 is ", int(inpum) + 87)

print("enter first number")
input1 = input()

print("enter second number")
input2 = input()

print("sum of two numbers are", int(input1) + int(input2))
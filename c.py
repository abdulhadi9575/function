def add(x,y):
    return x+y 
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def multi(x,y):
    return x*y
print("pls select the opration")
print("a. add")
print("s. sub")
print("d. div")
print("m. multi")
choice=str(input("pls select the choice"))
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
if choice=="a":
    print(add( num1,num2))
elif choice=="s":
    print(sub(num1,num2))
elif choice=="d":
    print(div(num1,num2))
elif choice=="m":
    print(multi(num1,num2))
else :
    print("invaled input")
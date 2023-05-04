from os import system


def addition(a,b):
    return a+b

def subraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

system('cls')
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("""
1.Addition
2.Subraction
3.Multiplication
4.Division""")

choice = int(input("\nEnter your choice in number:"))

if choice == 1:
    print(addition(a,b))

elif choice == 2:
    print(subraction(a,b))

elif choice == 3:
    print(multiplication(a,b))

elif choice == 4:
    print(division(a,b))

else:
    print("Enter the correct number")
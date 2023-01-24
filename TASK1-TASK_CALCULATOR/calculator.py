print('select an operation to perform')
print('1.ADD')
print('2.SUBTRACT')
print('3.MULIPTY')
print('4.DIVIDE')
operation = input()
if operation == "1":
    num1=input("Enter first number:")
    num2=input("Enter second number")
    print("sum is" + str(int(num1) + int(num2)))
elif operation=="2":
    num1=input("Enter first number:")
    num2=input("Enter second number")
    print(" difference is" + str(int(num1) - int(num2)))
elif operation=="3":
    num1=input("Enter first number:")
    num2=input("Enter second number")
    print("product is" + str(int(num1) * int(num2)))
elif operation=="4":
    num1=input("Enter first number:")
    num2=input("Enter second number")
    print(" result is" + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")


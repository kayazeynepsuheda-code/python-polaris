num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
if num2 == 0:
    print("Your second number cannot be 0. Error..")
else:
    print(f"{num1}/{num2}={num1/num2}")

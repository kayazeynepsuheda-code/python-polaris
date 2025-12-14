a = False
while a== False:
    try:
       enter=input("Please enter a number:")
       num = int(enter)
       a=True
    except ValueError:
        print("!!!Enter an integer value!!!")
    

    

    
print(f"Your number :{num}")






    


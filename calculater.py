print("1 = ADDITION")
print("2 = SUBTRCTION")
print("3 = MULTIFICATION")
print("4 = DIVITION")

choice=input("ENTER YOUR CHOICH (1,2,3,4) :-")

a=float(input("ENTER 1ST NUMBER :-"))
b=float(input("ENTER 2nd NUMBER :-"))

if choice=="1":
    print("ADDITION OF TWO NUBER IS :-",a+b)

elif choice=="2":
    print("SUBTRACTION OF TWO NUBERS IS :-",a-b)    

elif choice=="3":
    print("MULTIFICATION OF TWO NUBERS IS :-",a*b)

else:
    print("DIVITION OF TWO NUBERS IS :-",a/b) 

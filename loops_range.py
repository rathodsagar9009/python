# # #                                      [  while loop  ]
# count=1 #  count ne "iterator" kevay che
# while count<=5:
#     print("sagar rathod",count)
#     count+=1

# print number from 5 to 1
# i=5
# while i>0:
#     print(i)
#     i-=1

#     # print number from 1 to 5
# i=1
# while i<6:
#     print(i)
#     i+=1

 # print num. from 1 to 100
# i = 1
# while i<101:
#     print(i)
#     i+=1
    
# print num. from 100 to 1
# i=100
# while i>0:
#     print(i)
#     i-=1


# print the multification table of a number n.
# num=int(input("enter a number:"))

# i=1
# while i<11:
#     print(num,"x",i,"=",i*num)
#     i+=1


# print the element of the follwing list using a loop
#[1,4,9,16,25.....100]
# i=1
# while i<11:
#     print(i**2)
#     i+=1


#search for a num. x in this tuple using loop(problem)
#(1,4,9,....100)


# num=(1,4,9,16,25,36,49,64,81,100)
# x=36

# i=0
# while i<len(num):
#     if(num[i] == x):
#         print("found at index")
 
        
# i+=1



#######                     [   FOR LOOP   ]



# list=[1,23,5,4,6,7]
# for num in list:
#    print(num)

# tuple=(1,2,3,4,5)   
# for i in tuple:
#     print(i)
#     print(type(i))

    # 1] print the element of the following list using a loop:


# num=(1,4,9,16,25,36,49,64,81,100)
# x=49
# inx=0
# for el in num:
#     if(el == x):
#       print("num. found at index:",inx)

# inx+=1 


##                              [ RANGE ]

# for i in range(2,100):
   
#         print(i)




# # TABLE
# x=int(input("enter num."))
# for i in range(1,11):
#         print(x*i)


#               [ PASS :- WORK NE temparari bandh karva mate uesd thai che]

# TO FIND THE SUM OF FIRST N NUM. (WHILE USING)

# n=int(input("enter num."))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum = ",sum)



# factorial num.(using for)
n=int(input("enter num."))
fact=1
for i in range (1,n+1):
    fact*=i
    i+=1
print("fact.number is :",fact)
#FUNCTIONS :- "block of statements that perform a specific task."
#function i/p lay tene parametar kevay che
#redendency ochi karva mate vapar che

# def calc_sum(a,b):  #function defination
#     sum=a+b         #a and b are parameters
#     print(sum) 
#    # return sum

# calc_sum(2,3)           #function call(argument1,argument2)


# 1 ] avarage of 3 numbers using function.
# def calc_avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg

# calc_avg(1,2,3)
# calc_avg(12,15,18)


  # product function
# def cal_prod(a,b):
#     prod=(a*b)
#     print(prod)
#     return prod

# cal_prod(2,5)
    


# 2]   print the lenght of list(list is the parameter) problem

# citis=["rajkot","mumbai","pune","noida","delhi"]
# heros=["srk","ak","ab"]
 
# def print_len(list):
#     print_len(list)
    
#     print_len(citis)
#     print_len(heros)



# 3] factorial 

# def cal_fact(n):
#   fact=1
#   for i in range (1,n+1):
#     fact*=i
#   print(fact)

# cal_fact(5)

# 4] usd to inr convert
# def converter(usd):
#     inr=usd*83
#     print(usd,"USD=",inr,"INR")

# converter(2)

#  5] even odd define using function

# def con_kuku(n):
#     if(n%2==0):
#      print("even")
#     else:
#        print("odd")
       
# con_kuku(5)


#                               [   RECURSION  ]
#LOOPS==RECURTION

# def show(n):
#     if(n==0):         #base case kevay  
#         return
#     print(n)
#     show(n-1)


# show(5)
 # using recurton factorial

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return(fact(n-1)*n)


# print(fact(5))

#                                         practice 
# write a recurtion function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(5)
print(sum)

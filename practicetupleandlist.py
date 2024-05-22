# # WAP TO ASK THE USER TONENTER NAMES OF 3 FAVORITE MOVIES & STORE IN A LIST

list=[]
m1=input("enter 1st movie name:")
m2=input("enter 2nd movie name:")
m3=input("enter 3rd movie name:")
list.append(m1)
list.append(m2)
list.append(m3)
print(list)

# #WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.(HINT: USE COPY() METHOD)
# #"PALINDROME" MEANS AGAL THI ANE PACHAD THI SAME HOI EXAMPLE [1,2,3,2,1]
# # list=[1,2,3,2,1]
list=[]
list1=int(input("enter first number :"))
list2=int(input("enetr second number:"))
list3=int(input("enetr third number:"))
list.append(list1)
list.append(list2)
list.append(list3)
print(list)
list4=list.copy()
list4.reverse()
if(list==list4):
    print("palindrome")
else:
    print("not palindrome")



#WAP TO COUNT THE NUMBER OF STUDENT WITH THE "A" GRADE IN THE FOLLOWING TUPLE.
grade = ("A","B","C","A","A","B","C","A")
print(grade.count("A"))


#STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D"
grade = ["A","B","C","A","A","B","C","A"]
grade.sort(reverse=True)
print(grade)
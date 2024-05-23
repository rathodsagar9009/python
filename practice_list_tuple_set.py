# 1] STORE FOLLWING WORD MEANING IN A PYTHON DICTIONARY
# dic={
#     "cat":"a small annimal",
#     "table":["a piece of furniture","list of facts & figures"]
# }
# print(dic)

# 2] YOU ARE GIVEN A LIST OF SUBJECT FOR STUDENT.ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT.HOW MANY CLASSROOM ARE NEEDED BY ALL STUDENT.
# subject={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }
# print(subject)
# print(len(subject))
 
# 3] WAP TO ENTER MARKS OF 3 SUBJECT FROM THE USER AND STORE THEM IN A DICTIONARY.START WITH AN EMPTY DICTIONARY & ADD ONE BY ONE.USE SUBEJECT NAME AS KEY &MARK AS VALUE
mark={}
a=int(input("enter phy mark:"))
mark.update({"phy":a})

a=int(input("enter bio mark:"))
mark.update({"bio":a})

a=int(input("enter che mark:"))
mark.update({"che":a})

print(mark)

# 4] 
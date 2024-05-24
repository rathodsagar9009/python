
#       READ FILES

# f=open("basic.txt","r")
# data1=f.readline()
# print(data1)
# data2=f.readline()
# print(data2)

#       WRITE FILE

# f=open("basic.txt","w")
# f.write("i want traveling to mumbai")
# f.close

# #           append file

# f=open("basic.txt","a")
# f.write("\nand i will go jhuh beach")
# f.close


#r+ = ma file over right thase
#w+ = ma file badho data delete thai jase
#a+ = read kai pan nai thai ane write karsu to write thase ane overright(pela nu delete thai ne navu lakhe)nai thai

#r+   = read thase , overright thai jase , pointer startig ma hase,no trunket(delete)
#w+   = read thase , overright thai jase , trunket(delete)
#a+   = read thase , append thase , pointer ending ma hase,no trunket




# #                       [   with syntex     ]
# with open("basic.txt","r") as f:
#   data=f.read()
#   print(data)

# with open("basic.txt","w") as f:
#     f.write("go to goa")

# import os 
# os.remove("basi.txt")



#               [       practice        ]


# new file creat karva mate
# f=open("practice.txt","w")
# data=f.write()
# print(data)

# f=open("practice.txt","w")
# f.write("hi everyone\nwe are learning file i/o\nusing java\ni like programing in java")
# f.close


#  2] WAP THAT REPLACE ALL OCCURRENCES OF JAVA WITH PYTHON IN ABOVE FILE.
# f=open("practice.txt","r")
# data=f.read()

# new_data=data.replace("java","python")
# print(new_data)

# f=open("practice.txt","w")
# f.write(new_data)


#   3] wap search if the worx "LEARNING" exists in the file or not.

# f=open("practice.txt","r")
# data=f.read()
# if(data.find("learning")):
#     print("found")
# else:
    # print("not found")



#  4] WAP TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST

#   5] FROM A FILE CONTAINING NUM. SEPARATED BY COMMMA,PRINT THE COUNT OF EVEN NUM.

with open("practice.txt","r")as f:
    data=f.read()
    print(data)

#       READ FILES

# f=open("basic.txt","r")
# data1=f.readline()
# print(data1)
# data2=f.readline()
# print(data2)

#       WRITE FILE

f=open("basic.txt","w")
f.write("i want traveling to mumbai")
f.close

#           append file

f=open("basic.txt","a")
f.write("\nand i will go jhuh beach")
f.close


#r+ = ma file over right thase
#w+ = ma file badho data delete thai jase
#a+ = read kai pan nai thai ane write karsu to write thase ane overright(pela nu delete thai ne navu lakhe)nai thai

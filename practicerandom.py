# from poly2 import Employee

# e1=Employee()
# e1.showDetails("sagar")



# def main():

#     import random

#     #Open a file named numbersmake.txt.
#     outfile = open('numbersmake.txt', 'w')

#     #Produce the numbers
#     for count in range(12):
#         #Get a random number.
#         num = random.randint(1, 100)

#     #Write 12 random intergers in the range of 1-100 on one line
#     #to the file.
#     outfile.write(str(num))

#     #Close the file.
#     outfile.close()
#     print('Data written to numbersmake.txt')

# #Call the main function
# main()


# new file creat karva mate
import random
import string

filename_len=8

charValues=string.ascii_letters+string.digits+string.punctuation
filename=""
for i in range(filename_len):
 filename+=random.choice(charValues)
 print("file name :",charValues)
             
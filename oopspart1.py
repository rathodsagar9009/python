#  " to map with real world scenarios,we srarted using object in code." obeject oriented programingclas
# class Student:                  #class
#     name="arjun"

# s1 = Student()                      #object
# print(s1.name)  
# s2 = Student()
# print(s2.name)   

# class Car:
#     car="blue"   
#     model="bmw"
# c1 = Car()
# print(c1.car)
# print(c1.model)
 

 # CONSTRUCTOR MEANS KE JETLA OBJECT CREAT THASE TYRE CREAT THASE 
    # __ININ__ FUNNCTION
# class Student:
#     collage_name="ABC COLLAGE"   #it called class attribute
#     def __init__(self,name,mark):  #parameterized contructor mean je self sivay na pan contuctor hooi.
#         self.name=name   #obeject attribute
#         self.mark = mark   #object attribute
#     def welcome(self):
#         print("welcom student",s1.name,"your mark is",s1.mark)
# s1 = Student("sagar",94)   
# #print(s1.name,s1.mark) 

# # s2 = Student("karan",86)
# # print(s2.name,s2.mark) 

# # print(s2.collage_name)
# # print(s1.collage_name)

# s1.welcome()






#  P1] cereat student class that takes name & marks of 3 subject as arguments in constructor .than creat a methot to print the average.

# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark


#     def get_avg(self):
#         sum=0
#         for i in self.mark:
#             sum+=i
#         print("hi",self.name,"your avg score is :",sum/3)    

# s1=student("sagar",[95,96,97])
# print(s1.name,s1.mark)
# s1.get_avg()

# # agar name change karvu hoi to 
# s1.name="karan"
# s1.get_avg()





#                                [      Static Method    ]

# without self method kevay che , aa class level ni mehod kevay che
 
# @staticmethod("decorator=meas keva ma ave che ke ame static method no used karva magi chi")
# class student:

#   @staticmethod
#   def welcome():
#     print("abc")


# #    4 PILLORE OF OOPS:-
# #                           [   1.  ABSTRACTION :- "MEAN KE CHUPAVU OR CLASS NI UNNECCESARY DETAILS N CHUPAVIE"    ]
# class car:
    
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.cluch=False

#     def start(self):
#         self.cluch=True
#         self.acc=True
#         print("car started..")   

# car1 = car()
# car1.start() 
    

 #                      [ 2. ENCAPSULATION :- "DATA + RELATED FUNCTION NU EK CAPSUL BANI CHI"]   




# P2  CREAT ACCOUNT CLASS WITH 2 ATTRIBUTES-BALANCE & ACCOUNT NO. CREAT METHOD FOR DEBIT,CREADIT & PRINTING THE BALANCE.

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
        #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was dibited")
        print("TOTAL BALANCE =",self.get_balance())

        #credit method
    def credit(self,amount):
        self.balance+=amount    
        print("Rs",amount,"was credit")
        print("TOTAL BALANCE =",self.get_balance())

    def get_balance(self):
        return self.balance


# object case
acc1=account(10000,312010110001625)
print(acc1.balance,acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
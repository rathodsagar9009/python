                                        # DEL KEYWORD:-


# delete karva mate 
# del s1.name
# del s1(" pura object ne delete kari saki chi")







# class Student:
#     def __inif__(self,name):
#         self.name=name
       

# #object
# s1 = Student("sagar")
# print(s1.name)

# del s1
# print(s1.name)



                                    # PRIVITE ATTRIBUTE & METHOD:-
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass    # " __ koi pan atrribute ni agal double liti laki atle te privite thai jase


#     def reset_pass(self):
#         print(self.__acc_pass)


# #object
# s1 = account("312010110002010","5680")   
# print(s1.acc_no)
# print(s1.reset_pass())     





#PILLORE OF OOPS                [  3   INHERITANCE:- CLASS NI AMUK PROPERTIES SAME HOICHE JE BIJA CLASS MA VAPARI SAKI TENE INHERITANCE KEVAY CHE  ]

# #
# class car: #BASE CLASS
#     color="black"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stop")

# class toyotacar(car): #DERIVED CLASS
#     def __init__(self,name):
#         self.name=name

#         #object

# car1=toyotacar("Fortuner")
# car2=toyotacar("pries")

# print(car1.color)
# print(car1.name)


    #INHERITANCE 3 TYPE:-
    #1]SINGLE INHERITANCE("SINGLE BASE{PARENT CLASS} CLASS ANE SINGLE DERIVED{CHILDE CLASS} CLASS HOI CHE")
        # UPPER NO EXMPLE CHE
   
   
   
    #2]MULTI-LEVEL INHERITANCE("SINGLE BASE CLASS ANE ANO DERIVED CLASS HASE ,ANE AA DRIVED CLASS YE BASE CLASS BANI JASE ANA PACHI NO CLASS DERIVED CLASS BANSE ")

# class car:  #BASE CLASS
#     @staticmethod
#     def start():
#         print("car started")
#     def stop():
#         print("car stop")

# class toyota(car): #DERIVED CLASS 
#     def __init__(self,brand):
#         self.brand=brand

# class fortuner(toyota): #DERIVED CLASS
#     def __init__(self,type):
#       self.type = type 

# #object
# car1=fortuner("deasel")
# car1.start()

#    3] MULTIPLE INHERITANCE ("BASE CLASS 1 ANE BASE CLASS 2 HASE AND ANO DRIVED CLASS HASE SAME HASE")

# class A:# BASE CLASS
#     varA= "wel come to class A"
# class B:# BASE CLASS
#     varB="wel come to class B"    
# class C(A,B):#DRIVED CLASS
#      varC="wel come to class C"    
    

# c1=C()
# print(c1.varC)



#               [       SUPER METHOD:-PERENT CLASS NI METHOD NE ACCESS KARI         ]



# class car:  #BASE CLASS
#     def ___init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stop")

# class toyotacar(car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
   
   
# c1=toyotacar("prius","electric")
# print(c1.type)

#                   [   CLASS METHOD    ]

# class Person:
#     name="anonymous"

#     def changename(self,name):
#         self.name=name



# p1=Person()
# p1.changename("rathod sagar")
# print(p1.name)
# print(Person.name)


#1)INTANACE METHOD(SELF. NO USED THAI CHE)
#2)CLASS METHOD(CLASS. NO USED THAI CHE )
#3)STATICMETHOD



#               [   PROPERTY DECORATER :- IT IS UESD TO ANY METHOD IN THE CLASS TO UES THE METHOD AS A PROPERTY. ]

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
    

#     @property
#     def percentage(self):
#         return str((self.phy + self.che + self.math) / 3)+ "%"


# stu1=Student(98,95,92)
# print(stu1.percentage)
# stu1.phy=56
# print(stu1.percentage)



#OOPS TYPE           [4.   POLYMORPHISM :- POLY=MANY ,EK JA CIJ NE ALAG ALAG RITE USED KARI TENE KEVAY POLYMORPHISM  ]

#operation overloading:-ek "+,-,*,/...." sine na different meaning


# print(1+2) 
# print(type(1))

# print("rathod" + "sagar") #streang ne join kare to tene "CONCATENAT" KEVAY CHE
# print(type("rathod"))

# print([1,2,3] + [4,5,6]) # marge
# print(type([1,2,3]))



#complex number :-  1i+3j(real part + imeginary part)
#example :- (5i+9j) + (4i+6j) = 9i+15j


class complpex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")



num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4,5)
num2.showNumber()
    
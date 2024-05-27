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
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    # " __ koi pan atrribute ni agal double liti laki atle te privite thai jase


    def reset_pass(self):
        print(self.__acc_pass)


#object
s1 = account("312010110002010","5680")   
print(s1.acc_no)
print(s1.reset_pass())     
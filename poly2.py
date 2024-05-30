class Employee:

  
  def showDetails(self,role=None):
        print("role =",role)
        return role
        
  def showDetails(self,role=None,salary=None):
        print("role =",role)
        print("salary=",salary)
        return role,salary
        
  
  def showDetails(self,role=None,salary=None,department=None):
        print("role =",role)
        print("salary=",salary)
        print("department=",department)
      
      

e1 = Employee()
e1.showDetails("accountanat",25000,"finance")

class Employee:

  def showDetails(self,role=None):
        print("role =",role)
  def showDetails(self,role=None,salary=None):
        print("role =",role)
        print("salary=",salary)
  def showDetails(self,role=None,salary=None,department=None):
        print("role =",role)
        print("salary=",salary)
        print("department=",department)

e1 = Employee()
e1.showDetails("jjjj")


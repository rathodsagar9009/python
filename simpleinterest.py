principle=int(input("ENTER PRINCIPLE VALUES:-"))
rate=int(input("ENTER RATE OF INTEREST VALUES:-"))
time=int(input("ENTER YEAR OF INTEREST VALUES:-"))

def calc_simple_interest(principle,rate,time):
      SI=(principle*rate*time)/100
     # SI=Amount-principle
      print("SIMPLE INTEREST IS :- ",SI)
      return calc_simple_interest



calc_simple_interest(principle,rate,time)
      
principle=float(input("ENTER PRINCIPLE VALUES :-"))
rate=float(input("ENTER RATE VALUES :-"))
time=float(input("ENTER YEAR OF INTEREST VALUES :- "))

def calc_compound_interest(principle,rate,time):
    Amount = principle*(pow((1+rate/100),time))
    CI=Amount-principle 
    print("COMPOUND INTEREST IS :-",CI)
    return calc_compound_interest





calc_compound_interest(principle,rate,time)
p = int(input("Enter your amount: "))
r = float(input("Enter your interest rate: "))
d = int(input("Enter number of days: "))
i1 = p*(2.5/100)*d/365
i = round(i1,1)
print(f"You earned ${i} interest.")
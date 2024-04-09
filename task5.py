#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days
c = int(input("Enter the current population: "))
r = float(input("Enter the rate of growth in percent: "))
t = int(input("Enter the number of days: "))
f1 = c*(1+(r/100))**(12/365)
f = round(f1)
print(f"There will be {f} people after {t} days")
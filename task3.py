#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
a = float(input("The price of the first item"))
b = float(input("The price of the second item"))
c = float(input("The price of the third item"))
d = float(input("The price of the fourth item"))
e = float(input("The price of the fifth item"))
t1 = a+b+c+d+e
t2 = t1*0.12
t3 = t1+t2
t = round(t1,2)
t4 = round(t2,2)
t5 = round(t3,2)
print(f"Your subtotal is ${t} and your taxes total ${t4} for a total of ${t5}")
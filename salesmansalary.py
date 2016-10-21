#!/usr/bin/python3

"""Salesman basic salary is 1500, for every camera he will sell he will get 200
   and the commission on the month's sale is 2%. The input will be number of 
   cameras sold and total price of the cameras."""

basic_salary=1500
camera_sell=200
commission=0.02
camera_sole=int(input("Enter Numbers of camera sold: "))
total_price=float(input("Total Price : "))

salary=basic_salary+(camera_sole*camera_sell)+(total_price*commission*camera_sole)

print("Bonus",camera_sole*camera_sell)
print("Commision ",total_price*commission*camera_sole)
print("Gross Salary: ",salary)


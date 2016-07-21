#!/usr/bin/python3

age=int(input("Enter your age in years:"))
max_heart_rate=206.9-(0.67*age)  # as per Med Sci Sports Exerc.
target=0.65*max_heart_rate
print('Your Target fat-burning heart rate is {}'.format(target))

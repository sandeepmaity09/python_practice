#!/usr/bin/python3

"""This is a very simple game of sticks. There are 21 sticks, first the user
   picks number of sticks between 1-4 then the computer picks sticks(1-4).
   Who ever will pick the last stick will loose."""


sticks=21
print("Game of Sticks")
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: ",sticks)
    sticks_taken=int(input("Take sticks(1-4): "))
    if sticks==1:
        print("You took the last stick, you loose")
        break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: ",(5-sticks_taken),"\n")
    sticks-=5

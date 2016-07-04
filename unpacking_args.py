#!/usr/bin/python3

def parrot(voltage,state='a staff',action='voom',type='Norwegin Blue'):
        print("-- This parrot wouldn't",action,end=' ')
        print("if you put",voltage,"volts through it.")
        print("--Lovely plumage, the",type)
        print("--It's",state,"!")

d={"voltage":"four million","state":"bleedin' demished","action":"VOOOM"}
parrot(**d)


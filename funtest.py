N=input()
name=[]
number=[]
for i in range(int(N)):
    temp=input()
    nametemp=temp.strip().split()
    name.append(nametemp[0])
    number.append(nametemp[1])
    number.append(nametemp[2])
    number.append(nametemp[3])

print(name)
print(number)
    

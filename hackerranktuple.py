# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
temp=raw_input()
temp=temp.strip().split()
data=list()
for i in temp:
    data.append(int(i))
tup=tuple(data)
print hash(tup)

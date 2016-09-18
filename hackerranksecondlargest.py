N=int(raw_input())
num=raw_input()
num=num.strip().split()
num=list(set(map(int,num)))
num.sort()
print num[len(num)-2]

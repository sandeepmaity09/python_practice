Nsize=int(raw_input())
N=raw_input()
Msize=int(raw_input())
M=raw_input()

N=N.strip().split()
M=M.strip().split()

Nset=set(N)
Mset=set(M)
lis=list()
lis.extend((Nset.difference(Mset)))
lis.extend((Mset.difference(Nset)))
lis=(map(int,lis))
lis.sort()
for i in range(len(lis)):
    print lis[i]


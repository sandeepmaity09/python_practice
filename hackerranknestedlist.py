N=int(raw_input())

lis=list()

for i in range(N):
    name=raw_input()
    grade=float(raw_input())
    lis.append([name,grade])

lisnum=list()

for j in range(N):
    lisnum.append(lis[j][1])

lisnum=list(set(lisnum))
lisnum.sort(reverse=True)
leng=len(lisnum)
seclow=lisnum[leng-2]

namelist=list()
for k in range(N):
    if seclow == lis[k][1]:
        namelist.append(lis[k][0])
namelist.sort()

for l in range(len(namelist)):
    print namelist[l]
    

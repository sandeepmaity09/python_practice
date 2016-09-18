# Enter your code here. Read input from STDIN. Print output to STDOUT
X=int(raw_input())
Y=int(raw_input())
Z=int(raw_input())
N=int(raw_input())

"""lis=list()
for i in range(X+1):
    for j in range(Y+1):
        for k in range(Z+1):
            if i+j+k!=N:
                lis.append([i,j,k])"""

print ([[a,b,c] for a in range(X+1) for b in range(Y+1) for c in range(Z+1) if a+b+c!=N] )

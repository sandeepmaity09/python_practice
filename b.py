#!/usr/bin/python3

line1=input().split()
line2=input().split()
line3=input().split()
n=int(line1[0])
k=int(line1[1])
A=list()
B=list()
for i in line2:
    A.append(int(i))
for i in line3:
    B.append(int(i))


#print(n,k,A,Bi)


minsum=0
maxdif=0
product=0
for i in range(n):
    product+=A[i]*B[i]
    print(product)
    if (product<0 and B[i]<0):
        print(product)
        print(B[i])
        temp=(A[i]+(2*n)) *B[i]
        print(temp)
    elif (product<0 and A[i]<0):
        print(product)
        print(A[i])
        temp=((A[i]-(2*n)) *B[i]
    elif (product>0 and A[i]<0):
        print(product)
        print(A[i])
        temp=(A[i]+(2*n)) *B[i]
        print(temp)
    elif (product>0 and A[i]>0):
        print(product)
        print(A[i])
        temp=(A[i]-(2*n)) *B[i]
        print(temp)

    diff=product-temp
    print(diff)
    if(diff>maxdif):
        maxdif=diff
    minsum+=product
    print(minsum)
minsum+=maxdif
print(minsum,maxdif,product)


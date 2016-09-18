T=int(input())
for i in range(T):
    string=input()
    string=str(string)
    even=list()
    odd=list()
    for j in range(len(string)):
        if j%2==0:
            even.append(string[j])
        else:
            odd.append(string[j])
    even=str(even)
    odd=str(odd)
    even=even.strip().split()
    odd=odd.strip().split()
    print(even+"  "+odd)
    

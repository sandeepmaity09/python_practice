N=int(raw_input())
data=list()
for i in range(N):
    inp=raw_input()
    inp=inp.strip().split()
    if inp[0]=='append':
        data.append(int(inp[1]))
    elif inp[0]=='insert':
        data.insert(int(inp[1]),int(inp[2]))
    elif inp[0]=='remove':
        data.remove(int(inp[1]))
    elif inp[0]=='pop':
        data.pop()
    elif inp[0]=='index':
        data.index(int(inp[1]))
    elif inp[0]=='count':
        data.count(int(inp[1]))
    elif inp[0]=='sort':
        data.sort()
    elif inp[0]=='reverse':
        data.reverse()
    elif inp[0]=='print':
        print data
    
    

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)


with open('james.txt') as jaf:
    data=jaf.readline()
    james=data.strip().split(',')
    jamesdot=[]
    
    for each in james:
        temp=sanitize(each)
        #james.remove(each)
        #james.append(temp)
        jamesdot.append(temp)

#print(sorted(james))
print(jamesdot.sort())
print(sorted(jamesdot,reverse=True))
#print(jamesdot.sort())


print(jamesdot)

unique_james=[]

for each_item in jamesdot:
    if each_item in unique_james:
        continue
    else:
        unique_james.append(each_item)



print(unique_james)
print(unique_james[0:3])

james_set=set(jamesdot)
print(james_set)
print(sorted(james_set)[0:3]) #this code doesn't work without sorted cause set doesn't support slicing



#a program to recursively process the list
import sys
def print_lis(lis,level=0,indent=False,output=sys.stdout):
	for each_item in lis:
		if isinstance(each_item,list):
			print_lis(each_item,indent,level+1,output)
		else:
			if indent:
				for tab_intend in range(level):
					print("\t",end='',file=output)
			print(each_item,file=output)

man=[]
other=[]
try:
    data=open('sketchh.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role =='Other Man':
                other.append(line_spoken)
            else:
                pass
        except ValueError as valerr:
            pass  #print("ValueError: "+str(valerr))
        except NameError as nameerr:
            print("NameError: "+str(nameerr))
    data.close()
except IOError as ioerr:
    print("IOError: "+str(ioerr))

print_lis(man)
print_lis(other)
        
try:
    man_file=open('man_data_lis.txt','w')
    other_file=open('other_data_lis.txt','w')

    print_lis(man,0,True,man_file)
    print_lis(other,0,True,other_file)
except IOError as err:
    print('File Error: '+str(err))
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()

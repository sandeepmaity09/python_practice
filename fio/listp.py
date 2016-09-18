#a program to recursively process the list

def print_lis(lis,level=0,indent=false):
	for each_item in lis:
		if isinstance(each_item,list):
			print_lis(each_item,level+1)
		else:
			if indent:
				for tab_intend in range(level):
					print("\t",end='')
			print each_item

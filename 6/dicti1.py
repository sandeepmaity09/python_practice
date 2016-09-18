def santitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)

"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
            temp=data.strip().split(',')
            dicts=dict()
            dicts['Name']=temp.pop(0)
            dicts['DOB']=temp.pop(0)
            dicts['Times']=temp
        return dicts
    except IOError as err:
        print("File Error: "+str(err))
        return(None)
"""

#sarah=get_coach_data('sarah2.txt')
#print(sarah)


#original code
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        templ=data.strip().split(',')
        return({'Name':templ.pop(0),'DOB':templ.pop(0),'Times':str(sorted(set([santitize(t) for t in templ])))})
    except IOError as ioerr:
        print("File Error: "+str(ioerr))
        return(None)

sarah=get_coach_data('sarah2.txt')
print(sarah)

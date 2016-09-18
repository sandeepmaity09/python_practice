def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))
    except IOError as err:
        print("File Error: "+str(err))
        return(None)
    
def santitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)


sarah=get_coach_data('sarah2.txt')
#(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
#print(sarah_name+"'s fastest times are: "+str(sorted(set(santitize(t) for t in sarah))[0:3]))

"""
sarah_dict=dict()
sarah_dict['Name']=sarah_name
sarah_dict['Dob']=sarah_dob
sarah_dict['timing']=sorted(set(santitize(t) for t in sarah))

print(sarah_dict)
"""

#Original Code

sarah_data={}
sarah_data['Name']=sarah.pop(0)
sarah_data['DOB']=sarah.pop(0)
sarah_data['Times']=sarah
print(sarah_data['Name']+"'s fastest times are: "+str(sorted(set([santitize(t) for t in sarah_data['Times']]))[0:3]))

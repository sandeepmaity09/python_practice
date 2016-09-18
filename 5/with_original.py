"""The Original With code as a function"""
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


sarah=get_coach_data('sarah.txt')
print(sorted(set(santitize(t) for t in sarah))[0:3])

def santitize(time_string):
        if '-' in time_string:
            splitter='-'
        elif ':' in time_string:
            splitter=':'
        else:
            return(time_string)
        (mins,secs)=time_string.split(splitter)
        return(mins+'.'+secs)

class Athelete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=a_times
        
    def top3(self):
        return(sorted(set([santitize(t) for t in self.times]))[0:3])

    def add_time(self,time_value):
        self.times.append(time_value)

    def add_times(self,list_of_val):
        self.times.extend(list_of_val)
        

def get_coach_data(filename):
        try:
            with open(filename) as f:
                data = f.readline()
            temp=data.strip().split(',')
            return (Athelete(temp.pop(0),temp.pop(0),temp))
        except IOError as err:
            print("File Error: "+str(err))
            return(None)    

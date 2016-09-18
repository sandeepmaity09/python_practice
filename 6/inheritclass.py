def sanitize(time_string):
        if '-' in time_string:
            splitter='-'
        elif ':' in time_string:
            splitter=':'
        else:
            return(time_string)
        (mins,secs)=time_string.split(splitter)
        return(mins+'.'+secs)
    
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

    
def get_coach_data(filename):
        try:
            with open(filename) as f:
                data = f.readline()
            temp=data.strip().split(',')
            return (AthleteList(temp.pop(0),temp.pop(0),temp))
        except IOError as err:
            print("File Error: "+str(err))
            return(None) 

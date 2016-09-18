man = []
other = []
try:
    data = open('sketchh.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print ('The datafile is missing!')
print(man)
print(other)

try:
    outman = open("man_data.txt","w")
    outline = open("line_data.txt","w")

    print(man,file=outman)
    print(other,file=outlinex)

    outman.close()
    outline.close()

except:
    print("File not created")

finally:
    outman.close()
    outline.close()

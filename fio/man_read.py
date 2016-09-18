try:
    data = open('man_data_lis.txt')
    for each in data:
        try:
            print(each,end='')
        except:
            print("Error")
except IOError as err:
    print("IOError: "+str(err))
    

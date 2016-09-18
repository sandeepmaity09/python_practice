try:
    data=open('missing.txt')
    print(data.readline(),end='')
except IOError:
    print("FILE ERROR")
finally:
    if 'data' in locals():
        data.close()

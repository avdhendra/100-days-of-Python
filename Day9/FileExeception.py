try:
    with open('sad.txt',mode='x') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File not found exist')

except IOError as err:
    print("IO Error")
    raise err
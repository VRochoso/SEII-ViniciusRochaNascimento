

try:
   f = open('testfile.txt')
   var = bad_var

except FileNotFoundError:
    print('sorry. this file does not exist')

except Exception:
    print('sorry. something went wrong')

except Exception as e:
    print(e)

except FileNotFoundError as e
    print(e)

else:
    print(f.read())
    f.close()

finally:
    print("executing finally")

try:
   f = open('corrupt_file.txt')
   if f.name =='corrupt_file.txt':
    raise Exception
#print(dir(locals()['__builtins__']))
'''try:
    even=[2,4,6,8]
    print(even[2]/0)
except ZeroDivisionError:
    print("den cannot be zero")
    
try:
    num=int(input('enter num'))
    assert num%2==0
except:
    print('not even')
else:
    reciprocal=1/num
    print(reciprocal)'''
'''try:
    num=10
    den=10
    res=num/deno
except:
    print('den cannot be zero')
finally:
    print('out of pgm')'''
'''file_path='sindhu.txt'
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(f"An error occured:{e}")
finally:
    print("Closing the file")'''
    
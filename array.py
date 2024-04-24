n=int(input('Enter the number'))
if n>1:
    for i in range(0,n):
        if(n%i)==0:
            print('it is not a prime number')
            break
        else:
            print('it is a prime number')
else:
    print('it is not a prime number')
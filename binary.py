binary_data=input('Enter the data')
if binary_data.isdigit() and set(binary_data).issubset({'0','1'}):
    decimal=int(binary_data,2)
    if decimal%5==0:
        print('The binary number is divisible by 5')
    else:
        print('It is not divisible by 5')
else:
    print('Invalid data')
        

def sum():
    a=input('Enter the numbers:').split()
    a=[int(x) for x in a]
    neg=0
    even=0
    odd=0
    for i in a:
        if i<0:
            neg+=i
            print('Sum of negative num:',neg)
        elif i%2==0:
            even+=i
            print('Sum of positive even:',even)
        else:
            odd+=i
            print('sum of odd:',odd)
sum()
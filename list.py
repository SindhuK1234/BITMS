'''banana=[10,'balaji',250000.75,'z']
print(banana)
for i in banana:
    print(i,end='-')
print()
apple=[10,'balaji',250000.75,'z']#if one element value is changed it returns false
print(apple)
print(apple==banana)

apple=[10,20,30,40,50]
print(apple)
apple[1]=60
print(apple)
apple[2]=70,80,90
apple[1:2]=(-10,-20)#multipleindex values
print(apple)'''


'''college=[10,20,30,40,50]
print(college[1])
print(college[-1])
print(college[1:3])#n-1 concept for 3
print(college[1:7])
#print(college[7])#array index out of bound
print(college[:])#prints all the values
print(college[-4:-1])
print(college[3:-1])
print(college[1:])#prints till last index value
print(college[:-1])#starts from default 0 index
print(college[0:])
print(college[0:4:2])#2 is step value,0 & 4 are index value'''


#accept the input from user
sindhu=[]
n=int(input('Enter the list size'))
for i in range(0,n):
    ele=int(input('Enter the elements'))
    sindhu.append(ele)#append means display extra values at last
print(sindhu)



'''a=[10,20,30,40]
b=[50,60,70,80]
c=a+b
print(c)
print(type(a))
print(type(b))
print(type(c))
print(c*2)#repeat 2 times
print(len(c))#length of c
print(max(c))#max value of c
print(min(c))'''#min value of c


#sum
'''a=[10,20,30,40,50,60]
sum=0
for i in a:
    sum+=i
print(sum)'''

#print num end with 7
'''a=[10,25,37,40,57,65]
sum=0
for i in a:
    if i%10==7:
        print(i)'''

#remove duplicate(repeat) value 
a=[10,20,30,40,50,40,20,60]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


#print the common element
a=[10,20,30,40,50]
b=[60,70,80,90,100,20]
for i in a:
    for j in b:
        if i==j:
            print(j)







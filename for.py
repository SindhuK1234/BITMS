'''a,b,c,d,e=[int(x) for x in  input().split()]
print(a)
print(b)
print(c)
print(d)
print(e)'''

#doubling numbers
'''numbers=[10,20,30,40,50]
double_numbers=[num*2 for num in numbers]
print(double_numbers)'''

#finding square of num
numbers=[10,20,30,40,50]
sq_numbers=[num*num for num in numbers]
print(sq_numbers)

#find even num
even_num=[num for num in range(1,20) if num%2==0]
print(even_num)

#vowels
word='Sindhu'
vowels='aeiou'
result=[i for i in word if i in vowels]
print(result)





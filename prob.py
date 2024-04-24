#class MagicalPrime:
def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
def is_magical_prime(n):
    if is_prime(n):
        reverse_n=int(str(n)[::-1])
        return is_prime(reverse_n)
    return False
#def is_magical(cls,n):
    #return cls.is_prime(n) and cls.is_magical_prime(n)
number=int(input('Enter the num'))
if is_magical_prime(number):
    print(number, "is a magical prime number")
else:
    print(number ,"is not a magical prime number")


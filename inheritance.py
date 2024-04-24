'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Professor(Person):
    def isProfessor(self):
        return f'{self.name} is a Professor'
sir=Professor('sindhu',20)
print(sir.isProfessor())'''
'''class Sindhu:
    num1=3
class Divya:
    num2=5
class Pavi(Sindhu,Divya):
    def addition(self):
        return self.num1+self.num2
p=Pavi()
print(p.addition())'''
class Sindhu:
    num1=3
    def home(self,a,b):
        self.a=a
        self.b=b
        print('Sindhu property value',self.a+self.b)
class Divya:
    num2=5
    def jewels(self,a):
        self.a=2000
        print('Divya jewels property',self.a)
class Pavi(Sindhu,Divya):
    def addition(self):
        return self.num1+self.num2
p=Pavi()
print(p.addition())
print(p.jewels(1000))
print(p.home(12000,13000))
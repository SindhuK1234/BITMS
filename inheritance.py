#single inheritance
class person:#parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age
class professor(person):#subclass
    def isprofessor(self):
        print(obj.addition())

# another multiple
class Mrsindhu:
    num1=3
    def home(self,a,b):
        self.a=a
        self.b=b
        print('Mrsindhu property value is ',self.a+self.b)
class sindhu:
    num2=5
    def jewels(self,a):
        self.a=2000
        print('sindhu jewels property is',self.a)
class sindhuk(Mrsindhu,sindhu):
    def addition(self):
        return self.num1+self.num2
obj =sindhuk()
print(obj.addition())


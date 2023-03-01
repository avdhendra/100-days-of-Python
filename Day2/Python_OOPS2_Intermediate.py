#Mutliple Inheritance
class User:

    def __init__(self,email):
        self.email=email

    
    def sign_in(self):
        print(f"logged in with {self.email}")
 

class Wizard(User):
    
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name=name
        self.power=power
    
    def attack(self):
        print(f'attacking with power of {self.power}')
    

class Archer(User):
    def __init__(self,name,num_arrows,email):
        super().__init__(email)
        self.name=name
        self.num_arrows=num_arrows
    
    def attack(self):
        print(f'attacking with {self.num_arrows} arrows')
    

class Hybrid(Archer,Wizard):
    def __init__(self,name,power,num_arrows,email):
        super().__init__(name,power,email)
        super().__init__(name,num_arrows,email)


hybrid=Hybrid('kylie',100,200,'kylie@gamil.com')


#MRO -Method Resolution Order
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.__mro__)

#order will be BAXYZ happen in mutiple inheritance

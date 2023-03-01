#4 pillar of OOPS
#Encapsulation pack the variable and function in on class is know as Encapsulation

class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
player1=PlayerCharacter('andrei',100)
print(player1.name)
print(player1.age)

#Abstraction is hidding the important information from external sources
#but in python there is no private and protected access specifier 
#so we use _ as to tell the other this is the private data member of class
#so dont use it out side the class

class PlayerCharacter2:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    

#Inheritance

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
    

wizard1 =Wizard('Harry',1000,'jack@gmail.com')
archer1 = Archer('Robin',200,'rose@gmail.com')

wizard1.sign_in()
wizard1.attack()

archer1.sign_in()
archer1.attack()
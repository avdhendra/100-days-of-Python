#everything in the python is Object
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))  

#OOPS
class BigObject: #class is blueprint 
    #code
    pass

obj1=BigObject() #instanciate
obj2=BigObject() #instanciate

print(obj1) #obj1 and obj2 are object of BigObject which have property of class BigObject 
print(obj2)




#2 
class PlayerCharacter:
    #class Object Attribute
    membership=True #static not can be modified
    #constructor method any time we instance means when we create the object of class
    def __init__(self,name): #dunder Method
       #or if(PlayerCharacter.membership)
        if(self.membership):
              self.name=name
              
    #when function didnt return anything we get none
    def run(self):
        print('run')
    #self refer to player character player1 we set the name property of player1 to lol
    #like this in C++ and in Java
player1=PlayerCharacter('Lol')
player2=PlayerCharacter('kol')
player2.attack=40
print(player1)
print(player1.run())
print(player2.attack)

#gave class BluePrint
#help(PlayerCharacter)

#membership is Class Attribute and also Object attribute 
#so it can be access by PlayerCharacter of self key inside the class
#but name is not class attribute it is object attribute to it only access by self keyword
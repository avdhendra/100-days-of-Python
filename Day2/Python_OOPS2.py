#Decorator @classmethod
#we dont need to instantiate the class object to call the function

class PlayerCharacter:
    def __init__(self, name):
        self.name=name
    

    @classmethod
    def adding_Things(cls,num1,num2):
        return num1+num2
    #static method is same as above but we dont use cls
    @staticmethod
    def adding_things2(num1,num2):
        return num1+num2





#player1=PlayerCharacter('Tom')
print(PlayerCharacter.adding_Things(5,6))
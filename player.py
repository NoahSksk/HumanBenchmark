class Player:
    def __init__(self,name):
        if type(name) == str:
            self.name = name
        else:
            raise TypeError("Name must be a string")


    def display(self):
        return str(self.name)

    def nameChanger(self,newName):
        if newName != self.name and type(newName) == str:
            self.name = newName
        else:
            raise TypeError("The new name must be a string and must be different to the last name")

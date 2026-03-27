class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("animal is making the sound ...............")    




class Dog(Animal):
    def speak(self):
        super().speak()
        print("woof")



d= Dog("bruno")                
d.speak()
               
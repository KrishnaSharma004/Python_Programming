class Dog:
    species = "canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog1=Dog("Buddy",3)

print("Dog name is :",dog1.name)
print("Dog age is :",dog1.age)
print("Dog species is :",dog1.species)
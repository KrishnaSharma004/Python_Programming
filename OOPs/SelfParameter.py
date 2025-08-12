class Person:
    gender = "Male"
    def __init__(self,name,age):#self parameter is a reference to the current instance(object) of the class.
        self.name = name
        self.age = age
p1=Person("KrishnaSharma",19)

print("Person name is :",p1.name)
print(f"{p1.gender} gender is :",p1.gender)
print(f"{p1.name} age is :",p1.age)

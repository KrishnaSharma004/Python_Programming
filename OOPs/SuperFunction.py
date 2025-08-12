class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        super().__init__(name,idnumber)
        self.salary = salary
        self.post = post
    
e1 = employee("krishna",10,175000,"Student")

print(e1.name)
print(e1.idnumber)
print(e1.post)
print(e1.salary)
#initiate a class
class Employee:
    # special method/magic method/dunder method
    def __init__(self):
        # gives the address of the object self
        print(id(self))
        print("Started executing the attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("Attributes have been initialized")
    
    def travel(self,destination):
        print("This travel method was added manually")
        print(f"Employee is not travelling to {destination}")

# create an object/instance of the class
sam=Employee()
# it will have the same address as self in the init method because it points to the same object in the memory
# and hence it should be passed in every function call inside the class so that we can access the attributes and methods of the class
print(id(sam))

sami=Employee()
# here we created another object of Employee class and it will have a different address than sam because it is a different object in the memory
print(id(sami))

# sam.name="Sam Kumar"
# here we created an attribute of the Employee class known as a dynamic attribute created outside the class

# printing the attributes
# print(sam.id)

# calling a method
#sam.travel("Kerala")

print(type(sam))

# now importing chatbook class from oops_proj.py file and creating an object so that file can be accessed from within this file.
from oops_proj import chatbook
user1=chatbook()
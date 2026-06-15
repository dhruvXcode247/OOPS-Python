# Simple inheritance

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # # Derived class
# only constructors, non-private methods and non-private attributes can be inherited
# if we create a new __init__ constructor inside child class, it is known as constructor overloading and we can't
# acces the attributes of the parent class, then we use the super() method
# super() doesn't access values/attributes but the whole method
# class Dog(Animal):

# method overloading
#     def speak(self):
#         print(f"{self.name} barks.")

# # # Create an instance of Animal
# # animal = Animal("Generic Animal")
# # animal.speak()  # Output: Generic Animal makes a sound.

# # # Create an instance of Dog
# dog = Dog()
# dog.speak()  # Output: Buddy barks.


# Super Keyword

# Super

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# # Derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()  # Call the base class method
        # super() method can only be used inside the child class
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
# Output:
# Buddy makes a sound.
# Buddy barks. It is a Golden Retriever.
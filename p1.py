class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_instance = Person(name="samule", age=25)

print(f"Person's name: {person_instance.name}")
print(f"Person's age: {person_instance.age}")
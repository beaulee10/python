class Person:
    def __init__(self, first_name, last_name, address, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def get_info(self):
        return f"{self.first_name} {self.last_name}, Address: {self.address}, Age: {self.age}, Phone Number: {self.phone_number}" 
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address
    
    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

person1 = Person("John", "Smith", "68532 Apple Ln.", "20", "384-294-5842")
person2 = Person("Beth", "Crane", "12 Drury Ln.", "67", "912-294-3956")
person3 = Person("Josh", "Chung", "394 Clover Cr.", "18", "354-924-2394")

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
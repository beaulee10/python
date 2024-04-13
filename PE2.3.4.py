class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name
    
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    def set_kind(self, kind):
        self.__kind = kind
    
    def set_breed(self, breed):
        self.__breed = breed
    
    def set_name(self, name):
        self.__name = name
    
    def print_details(self):
        print(f"Pet Details: Kind {self.__kind}\n Breed {self.__breed}\n Name {self.__name}")

pet1 = Pet("Cat", "Siamese", "Jess")
pet2 = Pet("Lizard", "Gecko", "Buzz")
pet3 = Pet("Hamster", "Common", "Gus")

pet1.print_details()
pet2.print_details()
pet3.print_details()

print("\nType")
print(type(pet2))

print("\nGet Attribute")
breed = getattr(pet1, 'get_breed')() 
print(breed)

print("\nIs Instance")
print(isinstance(pet2, Pet))

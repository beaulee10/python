class Pet:

    vet_name = "Doggie Aid"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "Dog"):
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type

    def get_first_name(self):
        return self.owner_first_name
    
    def get_last_name(self):
        return self.owner_last_name
        
    def get_pet_id(self):
        return self.pet_id
    
    def get_pet_name(self):
        return self.pet_name
    
    def get_pet_type(self):
        return self.pet_type

    def set_first_name(self, value):
        self.owner_first_name = value
    
    def set_last_name(self, value):
        self.owner_last_name = value

    def set_pet_id(self, value):
        self.pet_id = value
    
    def set_pet_name(self, value):
        self.pet_name = value

    def set_pet_type(self, value):
        self.pet_type = value

    def display_pet_info(self):
        print("Owner's Details: ")
        print(self.owner_first_name + " " + self.owner_last_name)
        print("Pet's Details: ")
        print(self.pet_id)
        print(self.pet_name)
        print(self.pet_type)
        print("\n")

def main():

    pet1 = Pet("Aidan", "Broom", '012349', "Finn", "Dog")
    pet2 = Pet("Jake", "Wyatt", '885493', "Smitty", "Dog")
    pet3 = Pet("Grant", "Bryczek", "294124", "Hugo", "Dog")
    print("\n\n\n")
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    check_property = Pet("Jake", "Wyatt", '885493', "Smitty", "Dog")
    check_property = Pet("Grant", "Bryczek", "294124", "Hugo", "Dog")
    print(hasattr(check_property, "owner_first_name"))  # True
    print(hasattr(check_property, "owner_middle_name")) # False
    print(hasattr(check_property, "pet_type"))

main()
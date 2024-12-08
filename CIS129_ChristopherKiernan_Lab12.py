class Pet:
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animalType = animalType
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animalType(self, animalType):
        self.__animalType = animalType

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animalType(self):
        return self.__animalType

    def get_age(self):
        return self.__age
        
def main():
    pet_Name = input("Name of the pet? ")
    pet_Type = input("What type of animal is this pet? ")
    pet_Age = int(input("How old is this pet? "))

    pets = Pet(pet_Name,pet_Type,pet_Age)
    
    print("Your pet's name: ", pets.get_name())
    print('Animal Type: ', pets.get_animalType())
    print("Pet's Age: ", pets.get_age())
    input('Press Enter to Exit')
    
main()

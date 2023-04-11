from cryptography.fernet import Fernet

class Person():
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

person1 = Person("Kul kar", "18", "2 Kult,Sted 2001")

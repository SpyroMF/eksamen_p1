class Person():
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    # Denne funksjonen forventer en streng som er enten name, age eller address.
    # Den vil returnere verdien som skrives inn i get() funksjonen.
    def get(self, select: str) -> None:
        if select.lower() == "name":
            return self.name
        elif select.lower() == "age":
            return self.age
        elif select.lower() == "address":
            return self.address
        else:
            return "ERROR"
        
    def change_address(self, address: str):
        self.address = address

person1 = Person("Kul kar", 18, "2 Kult,Sted 2001")

print("Navn:      ", person1.get("name"))
print("Alder:     ", person1.get("age"))
print("Addresse:  ", person1.get("address"))

person1.change_address("19 Ikke Kult,Sted 3012")

print("Addresse2: ", person1.get("address"))
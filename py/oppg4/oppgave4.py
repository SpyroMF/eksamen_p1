class Elev():
    def __init__(self, name: str, address: str, age: int, phonenumber: str, email: str) -> None:
        self.name: str = name
        self.address: str = address
        self.age: int = age
        self.phonenumber: str = phonenumber
        self.email: str = email
    def print_info(self):
        print("Navn:    ", self.name)
        print("Addresse:", self.address)
        print("Alder:   ", self.age)
        print("Tlf:     ", self.phonenumber)
        print("E-post:  ", self.email)


#Eksempel
testperson: Elev = Elev("Kul Kar","2 Kult,Sted 2001", 18, "942 44 544", "kulkar91@gmail.com")
testperson.print_info()
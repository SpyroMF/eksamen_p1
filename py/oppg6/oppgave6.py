from cryptography.fernet import Fernet

class Person():
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    def generate_key(self):
        return Fernet.generate_key()
    def save(self):
        file1 = open("account.save", "w")
        file2 = open("account.key", "wb")
        
        # Saves key
        key = self.generate_key()
        print("Generated key:", key)
        file2.write(key)
        file2.close
        
        # Saves encrypted data
        file1.write(str(Fernet(key).encrypt(
            bytes(str(
            self.name+"\n"+
            self.age+"\n"+
            self.address
            ), encoding='utf8')
        )))
    def load(self):
        file1 = open("account.save", "r")
        file2 = open("account.key", "rb")
        
        # Reads the key
        key = file2.read()
        
        
        # Decrypts the raw text
        token = file1.read()
        raw = Fernet(key).decrypt(token)
        
        raw.split("\n")
        print("Loaded and Decrypted text:", raw)
# Person 1 skal lagre
person1 = Person("Kul kar", "18", "2 Kult,Sted 2001")
person1.save()

person2 = Person("e", "e", "e").load()

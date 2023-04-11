from cryptography.fernet import Fernet

class Person():
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    # Cryptography stuff (thanks https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password)
    def generate_key(self):
        return Fernet.generate_key()
    def encrypt(self, message: bytes, key: bytes) -> bytes:
        return Fernet(key).encrypt(message)
    def decrypt(self, token: bytes, key: bytes) -> bytes:
        return Fernet(key).decrypt(token)

    def save(self):
        save_file = open("account.save", "wb")
        key_file = open("account.key", "wb")

        key = self.generate_key()
        key_file.write(key)
        key_file.close()
        
        save_file.write(
            self.encrypt(bytes("{0}\n{1}\n{2}".format(self.name, self.age, self.address), encoding="utf8"), key)
        )
    def load(self):
        save_file = open("account.save", "rb")
        key_file = open("account.key", "rb")
        
        key = key_file.read()
        key = key_file.close()
        
        raw = self.decrypt(save_file.read(), key)
    
# Person 1 skal lagre
person1 = Person("Kul kar", "18", "2 Kult,Sted 2001")
person1.save()


person2 = Person("e", "e", "e").load()

class Rektangel():
    def __init__(self, lenght: int, width: int) -> None:
        self.length: int = lenght
        self.width: int = width
    def get_area(self):
        return self.length * self.width
    def get_circumference(self):
        return self.length + self.width

rektangel1 = Rektangel(10, 23)
print(
    "Rektangel areal:   ",rektangel1.get_area(),"\n"+
    "Rektangel omkrets: ",rektangel1.get_circumference()
)
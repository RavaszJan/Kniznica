print("kniznica")


class Book:
    def __init__(self,title,pages,price):
        self.titile=title
        self.pages=pages
        self.price=price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value >=0:
            self.__price=value
        else:
            raise  ValueError("Price is negative")

kniha=Book("Harry Poter",400,10)
print(kniha.price)
kniha.price=20
print(kniha.price)
kniha.price=-10

class Kniha:
    def __init__(selfself,nazov,isbn):
        self.nazov=nazov
        self.isbn=isbn
        self.dostupna=True

    def vypozicaj(selfself):
        self.dostupna=False

    class Kniznica:
        def __init__(selfself):
            self.zoznam_knih=[]
        def pridaj_knihu(selfself,kniha):
            self.zoznam_knih.append(kniha)

        def pozica_knihu(selfself,isbn_knihy):
            for k
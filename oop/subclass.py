from dataclasses import dataclass

@dataclass 
class Product: 
    name:str = "" 
    price:float = 0.0 
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100 
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    def getDescription(self): 
        return self.name
    def __str__(self) -> str:
        return self.name


@dataclass
class Book(Product): # Python calls the constructor of the superclass 
    author:str = "" # add another attribute to the three in the superclass

    # override the getDescription method 
    def getDescription(self): 
        return f"{Product.getDescription(self)} by {self.author}"
    
    def __str__(self) -> str:
        return f"{super().__str__()}\t|{self.author}"


@dataclass
class Movie(Product):
    year:int = 1900

    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year})"
    def __str__(self) -> str:
        return f"{super().__str__()}\t|{self.year}"

def show_products(products):
    for p in products:
        print(p.getDescription())
        if(isinstance(p,Book)):
            print(f"\t this is a book with price {p.price:.2f} $")

def print_products(products):
    for p in products:
        print(p)


def main():
    products = (Product("stanly",10,6), Book("book1",12,5,"mat"), Movie("movie01",5,100,2001))
    show_products(products)
    print("_"*20)
    print_products(products)

if __name__ == "__main__":
    main()

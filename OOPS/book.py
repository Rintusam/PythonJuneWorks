class book:

    title=str

    author=str

    price=int

    language=str


    def __init__(self,title,author,price,language):

        self.title=title

        self.author=author

        self.price=price

        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price,self.language)

    def __str__(self) :
        return self.title


# creating object 

book_instance1=book("WingsOfFire","abdul Kalam",2000,"english")

book_instance2=book("Goatlife","benyamin",4000,"malayalam")

book_instance1.display_book()
book_instance2.display_book()

print(book_instance1)
print(book_instance2)
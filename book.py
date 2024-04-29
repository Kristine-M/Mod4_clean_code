# The bookstore system requires a dedicated module for 
# handling various aspects related to books, such as title, 
# author, price, and stock status.

class Book:
    
    def __init__(self, title, author, price, stock):
        self.title  = title
        self.author = author
        self.price = price
        self.stock = stock
    
    
    def book_stock(self):
    
        if self.stock > 0:
            print("The book,", self.title, "is in stock:", self.stock, "remaining")
        else:
            print("The book,", self.title, "is out of stock. Check in another time")
    
    def display_info(self):
        print("Title:", self.title, "Author:", self.author,  "Price:", self.price, "\n\n")

class Cart():
    
    def __init__(self, num_items):
        self.num_items = num_items
        self.cart = []
        
    def add_to_cart(self, add):
        self.cart.append(add)
        self.num_items += 1
        
    def remove_from_cart(self, remove):
        self.cart.remove(remove)
        self.num_items -= 1
        
    def print_cart(self):    
        if len(self.cart) == 0:
            print("Your cart is empty")
        else:
            print("Here is your cart:")
            for item in self.cart:
                item.display_info()
        
class User(Cart):
    
    def __init__(self, num_items, name):
        super().__init__(num_items)
        self.name = name
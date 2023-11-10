class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book Information:\nName: {self.name}\nAuthor: {self.author}\nPrice: ${self.price}\nQuantity: {self.quantity}")


my_book = Book("The Great Gatsby", 20, 100, "F. Scott Fitzgerald")

my_book.read()


# Task 2
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        
        if dish_name not in self.menu:
            return "Dish not available"
        
        dish = self.menu[dish_name]
        
        if quantity > dish['quantity']:
            return "Requested quantity not available"
        
        
        total_cost = dish['price'] * quantity
        
        self.menu[dish_name]['quantity'] -= quantity
        return total_cost


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)


print(mc.order('burger', 5)) 
print(mc.order('burger', 15)) 
print(mc.order('kotleta', 5)) 

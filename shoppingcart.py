
#8) Class ShoppingCart with 3 attributes and 1 method
class ShoppingCart:
    def __init__(self,shopping_cart_id,customer):
        self.shopping_cart_id=shopping_cart_id
        self.products=[]
        self.customer=customer

    # Functions to create 3 methods:
    def display(self):
        print("Shopping Cart ID",self.shopping_cart_id,"Customer ID:",self.customer.name)
        for product in self.products:
            print("Product:",product.product_name)

    # Functions to add products:
    def add_products(self,product):
        self.products.append(product)


#8) Class ShoppingCart
class ShoppingCart:
    def __init__(self,shopping_cart_id, customer):
        self.shopping_cart_id=shopping_cart_id
        self.products=[]
        self.customer=customer

# Method Display:
    def display(self):
        print("Shopping Cart ID",self.shopping_cart_id,"Customer ID:",self.customer)
        for product in self.products:
            print("Product:",product.product_name)

# Function to add products:
    def add_products(self,product):
        self.products.append(product)

#Function to check the ID of each product in the Cart
    def finding_product_id_cart(self):
        origin_of_product=self.products[0]
        if "WP" in origin_of_product:
            return True
        if "MP" in origin_of_product:
            return False




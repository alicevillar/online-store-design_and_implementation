#6) Class Website Products with 5 attributes and 1 method:
class Website_Products:
    def __init__(self,product_name, product_id, category,price,storefront,quantity):#Function to create 5 attributes
        self.product_name=product_name
        self.product_id=product_id
        self.category=category
        self.price=price
        self.storefront=storefront
        self.quantity=quantity
    #Functions to create 3 methods:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront)

#7) Class Marketplace Products with 5 attributes and 1 method
class MarketplaceProducts:
    def __init__(self,product_name, product_id, category,price,storefront,quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.category = category
        self.price = price
        self.storefront = storefront
        self.quantity=quantity

    # Function to create a method:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront)

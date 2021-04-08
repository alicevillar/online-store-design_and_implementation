#6) Class Website Products
class Website_Products:
    def __init__(self,product_name, product_id, category,price,storefront,quantity,product_vendor):#Function to create 5 attributes
        self.product_name=product_name
        self.product_id=product_id
        self.category=category
        self.price=price
        self.storefront=storefront
        self.quantity=quantity
        self.product_vendor=product_vendor

#Function to create one method:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront,"Product Vendor",self.product_vendor)

#7) Class Marketplace Products
class MarketplaceProducts:
    def __init__(self,product_name, product_id, category,price,storefront,quantity,product_vendor):
        self.product_name = product_name
        self.product_id = product_id
        self.category = category
        self.price = price
        self.storefront = storefront
        self.quantity=quantity
        self.product_vendor=product_vendor

    # Function to create a method:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront,"Product Vendor:",self.product_vendor)

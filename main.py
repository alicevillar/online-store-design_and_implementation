#MY ONLINE STORE

#1) Class People has 4 attributes
#2) Class User inherits from People and has 3 attributes
#3) Class WarehouseStaff - inherits from People and has 3 attributes
#4)Class Customers: inherits from People, has 1 attribute and 3 methods purchaseHistory/+display,create,edit
#5)Marketplace - individualSellerName,individualSellerId,companySellerName,companySellerCrm,totalSellers,registration,marketplaceProducts/+display,create,edit
#6) Class Products with 5 attributes and 3 methods:
#7) Class Marketplace Products with 5 attributes and 3 methods
#8) Class ShoppingCart with 3 attributes and 3 methods
#9) Class OnlineOrders with 3 attributes onlineOrderId,productId,customerId
#10) Class Delivery Company with 3 attributes:
#11) Class Loyalty_Schemes with 3 attributes and 3 methods
#12) Class OrderDetails with 1 attribute orderId
#13) Class Payment with 3 attributes paymentId,shoppingCartId,loyaltyId

#1) Class People has 4 attributes crn/id
class People:
    def __init__(self,name,document_type,id_crn,phone,address):
        self.name = name
        self.document_type = document_type
        self.id_crn = id_crn
        self.phone = phone
        self.address = address

#2) Class User inherits from People and has 3 attributes
class User(People):
    def __init__(self,name,document_type,id_crn,phone,address, username,email,password):
        super().__init__(name,document_type,id_crn,phone,address)
        self.username=username
        self.email=email
        self.password=password

#Function to create 1 method:
    def check_password(self,password):
        if password == self.password:
            print("Correct password :)")
            return True
        else:
            print("Incorrect password :( Try again")
            return False

#3) Class WarehouseStaff - inherits from People and has 3 attributes
class Warehousestaff(User):
    def __init__(self, name,document_type,id_crn,phone,address, username,email,password,
                 position,staff_id,salary):
        super().__init__(name,document_type,id_crn,phone,address, username,email,password)
        self.position=position
        self.staff_id=staff_id
        self.salary=salary

    #Function to create 3 methods:
    def display (self):
        print("Name:",self.name,"Document Type:",self.document_type,"Id or crn:",self.id_crn,
              "Phone:",self.phone,"Address:",self.address,
              "Username:",self.username,"Email:",self.email,"Password",self.password,
              "Position:",self.position,"Staff ID",self.staff_id,"Salary:",self.salary)

#4)Class Customers: inherits from People, has 1 attribute and 3 methods purchaseHistory/+display,create,edit
class Customers(User):
    def __init__(self,name, document_type, id_crn, phone, address, username, email, password,purchase_history):
        super().__init__(name, document_type, id_crn, phone, address, username, email, password)
        self.purchase_history=purchase_history


#Functions to create 3 methods:
    def display(self):
        print("Name:",self.name,"Document Type:",self.document_type,"Id or crn:",self.id_crn,"Phone:",self.phone,"Address:",self.address,
              "Username:",self.username,"Email:",self.email,"Password",self.password,"Purchase History:",self.purchase_history)


 #5)Marketplace
class Marketplace(User):
    def __init__(self,name,document_type,id_crn,phone,address, username,email,password,individual_seller_name,individual_seller_id,company_seller_name,
                 company_seller_crm,total_sellers,registration,marketplace_products):
        super().__init__(name,document_type,id_crn,phone,address, username,email,password)
        self._individual_seller_name=individual_seller_name
        self._individual_seller_id=individual_seller_id
        self._company_seller_name=company_seller_name
        self._company_seller_crm=company_seller_crm
        self.total_sellers=total_sellers
        self.registration=registration
        self.marketplace_products=marketplace_products

#6) Class Website Products with 5 attributes and 1 method:
class Website_Products:
    def __init__(self,product_name, product_id, category,price,storefront):#Function to create 5 attributes
        self.product_name=product_name
        self.product_id=product_id
        self.category=category
        self.price=price
        self.storefront=storefront
    #Functions to create 3 methods:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront)

#7) Class Marketplace Products with 5 attributes and 1 method
class MarketplaceProducts:
    def __init__(self,product_name, product_id, category,price,storefront):
        self.product_name = product_name
        self.product_id = product_id
        self.category = category
        self.price = price
        self.storefront = storefront

    # Function to create a method:
    def display(self):
        print("Product name", self.product_name,"Product_ID:",self.product_id,"Category",self.category,
              "Price",self.price,"Storefront",self.storefront)

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

#9) Class OnlineOrders with 3 attributes onlineOrderId,productId,customerId
class OnlineOrders:
    def __init__(self,online_order_id,products,customer):
        self.online_order_id=online_order_id
        self.products=products
        self.customer=customer

 #10) Class Delivery Company with 3 attributes:
class DeliveryCompany:
    def __init__(self,name,crn,registration):
        self.name=name
        self.crn=crn
        self.registration=registration

#11) Class Loyalty_Schemes with 3 attributes and 3 methods
class LoyaltySchemes:
    def __init__(self,coupon_name, coupon_id,total):
        self.coupon_name= coupon_name
        self.coupon_id=coupon_id
        self.total=total

    # Functions to create 3 methods:
    def display(self):
        print("Coupon name:", self.coupon_name,"Coupon ID:",self.coupon_id,"Total:",self.total)

#12) Class OrderDetails with 1 attribute orderId

class OrderDetails:
    def __init__(self,online_order):
        self.online_order=online_order

    # Functions to create 1 method: generating a report

    def report(self):
        pass

#13) Class Payment with 3 attributes paymentId,shoppingCartId,loyaltyId

class Payment:
    def __init__(self,payment_id,online_order_id,loyalty_id):
        self.payment_id=payment_id
        self.online_order_id=online_order_id
        self.loyalty_id=loyalty_id

#TESTING CLASSES:


#1) Class People: creating a person (attributes: name,person_id,phone,address)
person1= People("Alice", "ID", 123, 988093939, "AvenueXXX")
#print(f"Name:{person1.name} \nID:{person1.person_id} \nPhone:{person1.phone} \nAddress: {person1.address}")

person2= People("Richard","ID", 456, 888093939, "AvenueYYY")
#print(f"Name:{person2.name} \nID:{person2.person_id} \nPhone:{person2.phone} \nAddress: {person2.address}")

person3= People("Jennifer","ID", 789, 788093939, "AvenueZZZ")
#print(f"Name:{person3.name} \nID:{person3.person_id} \nPhone:{person3.phone} \nAddress: {person3.address}")

#2) Class User: Creating a user (attributes: people, username,email,password
user1=User(person1.name,person1.document_type,person1.id_crn, person1.phone,person1.address,"Li","a@hh.com.br",123)
user2=User(person2.name,person2.document_type,person2.id_crn,person2.phone,person2.address,"Rich","r@hh.com.br",321)
user3=User(person3.name,person3.document_type,person3.id_crn,person3.phone,person3.address,"Jen","j@hh.com.br",323)

#3) Class WarehouseStaff: Creating an employee (attributes: user,position,staff_id,salary)

employee1=Warehousestaff(user1.name,user1.document_type,user1.id_crn, user1.phone,user1.address,user1.username,user1.email,user1.password,"role1",12,30000.90)
employee1.display()

#4) Class Customers: Creating a customer (attributes: name, person_id, phone, address, username, email, password,purchase_history)
customer1=Customers(user2.name,user2.document_type,user2.id_crn, user2.phone,user2.address,user2.username,user2.email,user2.password," ")
customer1.display()

#5)Class Marketplace: creating a seller
#seller1=Marketplace(user3)

#name, person_id, phone, address, username, email, password,individual_seller_name,individual_seller_id,company_seller_name,
                #company_seller_crm,total_sellers,registration,marketplace_products

#6) Class Website Products: creating a website product (product_name, product_id, category,price,storefront)

website_product1=Website_Products("Elsève",345,"Shampoo",2.00,True)
website_product1.display()

#7) Class Marketplace Products: creating a marketplace product (product_name, product_id, category,price,storefront)

marketplace_product1=MarketplaceProducts("Pantene",432,"Shampoo",1.87,True)
marketplace_product1.display()

#8) Class ShoppingCart: creating a shoppingcart (shopping_cart_id,product_id,customer_id)

shop1=ShoppingCart(1,customer1)
shop1.add_products(marketplace_product1)
shop1.display()

#9) Class OnlineOrders:online_order_id,product_id,customer_id):

order1=OnlineOrders(1,shop1.products,shop1.customer)

#10) Class Loyalty_Schemes: creating a coupon
christmas_card=LoyaltySchemes("Christmas", 1283,30)
christmas_card.display()


#11) Class OrderDetails with 1 attribute: orderId

order_details1=OrderDetails(order1)

#13) Class Payment with 3 attributes: payment_id,shopping_cart_id,loyalty_id

#paym1=Payment(321,435,432432)


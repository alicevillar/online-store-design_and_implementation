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

from people import People
from user import User
from warehousestaff import Warehousestaff
from customers import Customers
from products import Website_Products,MarketplaceProducts
from marketplace import Marketplace
from onlineorders import OnlineOrders
from deliverycompany import DeliveryCompany
from loyaltyschemes import LoyaltySchemes
from orderdetails import OrderDetails
from payment import Payment
from shoppingcart import ShoppingCart
from store import Store

# TESTING CODE:

# 1) Class People: creating a person (attributes: name,person_id,phone,address)
person1 = People("Alice", "ID", 123, 988093939, "AvenueXXX")
# print(f"Name:{person1.name} \nID:{person1.person_id} \nPhone:{person1.phone} \nAddress: {person1.address}")

person2 = People("Richard", "ID", 456, 888093939, "AvenueYYY")
# print(f"Name:{person2.name} \nID:{person2.person_id} \nPhone:{person2.phone} \nAddress: {person2.address}")

person3 = People("Jennifer", "ID", 789, 788093939, "AvenueZZZ")
# print(f"Name:{person3.name} \nID:{person3.person_id} \nPhone:{person3.phone} \nAddress: {person3.address}")

# 2) Class User: Creating a user (attributes: people, username,email,password
user1 = User(person1.name, person1.document_type, person1.id_crn, person1.phone, person1.address, "Li", "a@hh.com.br",
             123)
user2 = User(person2.name, person2.document_type, person2.id_crn, person2.phone, person2.address, "Rich", "r@hh.com.br",
             321)
user3 = User(person3.name, person3.document_type, person3.id_crn, person3.phone, person3.address, "Jen", "j@hh.com.br",
             323)

# 3) Class WarehouseStaff: Creating an employee (attributes: user,position,staff_id,salary)

employee1 = Warehousestaff(user1.name, user1.document_type, user1.id_crn, user1.phone, user1.address, user1.username,
                           user1.email, user1.password, "role1", 12, 30000.90)
employee1.display()

# 4) Class Customers: Creating a customer (attributes: name, person_id, phone, address, username, email, password,purchase_history)
customer1 = Customers(user2.name, user2.document_type, user2.id_crn, user2.phone, user2.address, user2.username,
                      user2.email, user2.password, " ")
customer1.display()

# 5)Class Marketplace: creating a seller

seller1=Marketplace(user3.name,user3.document_type,user3.id_crn,user3.phone,user3.address, user3.username,user3.email,user3.password,
                    "Paul",123244354,"",0,323,True,30)


# name, person_id, phone, address, username, email, password,individual_seller_name,individual_seller_id,company_seller_name,
# company_seller_crm,total_sellers,registration,marketplace_products

# 6) Class Website Products: creating a website product (product_name, product_id, category,price,storefront)

website_product1 = Website_Products("Barbie Beach", 345, "Dolls", 22.00, True)
website_product1.display()

# 7) Class Marketplace Products: creating a marketplace product (product_name, product_id, category,price,storefront)

marketplace_product1 = MarketplaceProducts("LEGO Starship", 432, "Art & Craft", 11.87, True)
marketplace_product1.display()

# 8) Class ShoppingCart: creating a shoppingcart (shopping_cart_id,product_id,customer_id)

shop1 = ShoppingCart(1, customer1)
shop1.add_products(marketplace_product1)
shop1.display()

# 9) Class OnlineOrders:online_order_id,product_id,customer_id):

order1 = OnlineOrders(1, shop1.products, shop1.customer)

# 10) Class Delivery Company with 3 attributes:

company1 = DeliveryCompany("Nike", 938239, 32432)
print(f"Name: {company1.name}, CRN:{company1.crn},Registration:{company1.registration}")

# 11) Class Loyalty_Schemes: creating a coupon:
christmas_card = LoyaltySchemes("Christmas", 1283, 30)
christmas_card.display()

# 12) Class OrderDetails with 1 attribute: orderId

order_details1 = OrderDetails(order1)

# 13) Class Payment with 3 attributes (payment_id,shopping_cart_id,loyalty_id)

paym1 = Payment(321, 435, 432432)
print(f"payment_id:", paym1.payment_id, "online_order_id:", paym1.online_order_id, "loyalty_id", paym1.loyalty_id)

# 14) Class Store

toy_store=Store()
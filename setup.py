
# Importing classes:
from people import People
from user import User
from warehousestaff import Warehousestaff
from customers import Customers
from products import Website_Products, MarketplaceProducts
from marketplace import Marketplace
from onlineorders import OnlineOrders
from deliverycompany import DeliveryCompany
from loyaltyschemes import LoyaltySchemes
from orderdetails import OrderDetails
from payment import Payment
from shoppingcart import ShoppingCart
from store import Store

                        # PART 2:Instantiating the class Store - INSTANTIATION PHASE

# Instantiating the class Store. Here Toy Store is being created:
toy_store = Store()

# Instanciating each class:

# a) Adding new users:

# Adding user 1
person1 = People("Alice", "ID", 123, 988093939, "Avenue XXX")
user1 = User(person1.name, person1.document_type, person1.id_crn, person1.phone, person1.address, "ALi", "a@hh.com.br",
             123)
toy_store.add_new_user(user1)

# Adding user 2

person2 = People("Richard", "ID", 456, 888093939, "Avenue YYY")
user2 = User(person2.name, person2.document_type, person2.id_crn, person2.phone, person2.address, "Rich", "r@hh.com.br",
             321)
toy_store.add_new_user(user2)

# Adding user 3

person3 = People("Jennifer", "ID", 789, 788093939, "AvenueZZZ")
user3 = User(person3.name, person3.document_type, person3.id_crn, person3.phone, person3.address, "Jen", "j@hh.com.br",
             323)
toy_store.add_new_user(user3)

# b) Adding new warehouse staff

employee1 = Warehousestaff(user1.name, user1.document_type, user1.id_crn, user1.phone, user1.address, user1.username,
                           user1.email, user1.password, "role1", 12, 30000.90)

toy_store.add_new_warehousestaff(employee1)

# c) Adding new customers

customer1 = Customers(user2.name, user2.document_type, user2.id_crn, user2.phone, user2.address, user2.username,
                      user2.email, user2.password, " ")

toy_store.add_new_customer(customer1)

# d) Adding new sellers

seller1 = Marketplace(user3.name, user3.document_type, user3.id_crn, user3.phone, user3.address, user3.username,
                      user3.email, user3.password,
                      "Paul", 123244354, "", 0, 323, True, 30)

toy_store.add_new_marketplace_vendor(seller1)

# e) Adding new website products

website_product1 = Website_Products("Barbie Bee", 345, "Dolls", 20.00, True, 3, 1)
toy_store.add_new_website_product(website_product1)

# f) Adding new marketplace products

marketplace_product1 = MarketplaceProducts("LEGO Starship", 432, "Art & Craft", 11.87, True, 3, 2)
toy_store.add_new_marketplace_product(marketplace_product1)

# g) Adding new shopping cart  (only for testing)

shop1 = ShoppingCart(1, customer1)

# h) Adding new online orders (only for testing)

order1 = OnlineOrders(2, shop1.products, shop1.customer)
toy_store.add_new_onlineOrders(order1)

# i) Adding new delivery company

company_postal_service = DeliveryCompany("Postal Office", 1, 222)
toy_store.add_new_delivery_company(company_postal_service)

company_in_house_courier = DeliveryCompany("In-house courier", 2, 333)
toy_store.add_new_delivery_company(company_in_house_courier)

# j) Adding new Loyalty_Schemes:

christmas_card = LoyaltySchemes("Christmas", 1, "Gift Card", 5)
toy_store.add_new_loyalty_schemes(christmas_card)

new_year_card = LoyaltySchemes("New Year", 2, "Promotional Code", 5)
toy_store.add_new_loyalty_schemes(new_year_card)

# l) Adding new order details: (only for testing)
order_details1 = OrderDetails(order1)
toy_store.add_new_order_details(order_details1)

# m) Adding new payment: (only for testing)

paym1 = Payment(1, 2, 1,toy_store.current_user)
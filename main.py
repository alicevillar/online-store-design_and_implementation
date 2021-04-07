                                        # MY TOY STORE

# => Summary: The code is divided in four parts:

# ) PART 1: Creating 13 classes - DEFINITION PHASE
# ) PART 2: Creating methods inside each class - IMPLEMENTATION PHASE
# ) PART 3: Instantiating the class Store - INSTANTIATION PHASE
# ) PART 4: Interacting with user - INTERACTION PHASE

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

# ) PART 3:Instantiating the class Store - INSTANTIATION PHASE

# Instantiating the class Store. Here Toy Store is being created:
toy_store = Store()

# Instanciating each class:

# a) Adding new users:

# Adding user 1
person1 = People("Alice", "ID", 123, 988093939, "AvenueXXX")
user1 = User(person1.name, person1.document_type, person1.id_crn, person1.phone, person1.address, "ALi", "a@hh.com.br",
             123)
toy_store.add_new_user(user1)

# Adding user 2
person2 = People("Richard", "ID", 456, 888093939, "AvenueYYY")
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

# g) Adding new shopping cart

shop1 = ShoppingCart(1, customer1)

# h) Adding new online orders

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

# l) Adding new order details:
order_details1 = OrderDetails(order1)
toy_store.add_new_order_details(order_details1)

# m) Adding new payment:

paym1 = Payment(1, 2, 1,toy_store.current_user)
#print(paym1.date.strftime("%m/%d/%Y %H:%M"))

# PART 4: Interacting with user

# Phase_1: Listing all products and showing on screen
# Phase_2: visitant selects a product
# Phase_3: system offers the possibility to register or login (if he is not)
# Phase_4: system checks product availablity and adds to shopping cart or says that the product is not available
# Phase_5: user is asked if he or she wishes to continue buying (back to 1) or checkout
# Phase_6:system checks if vendor is the website or a third party, then offers the correspondent delivery methods
# Phase_7:system provides 4 payment methods and user chooses one
# Phase_8: system asks if user wants to store payment details or use stored details
# Phase_9: payment is accepted and user receives an invoice message

# Functions:

def login_or_register():
    if not toy_store.is_logged:
        opt = int(input("Hi! If you not registered, type 1 to join us. If you are registered, type 2 to login:"))
        if opt == 2:
            username = input("Type your username:")
            password = input("Type your password:")
            password = int(password)

            if toy_store.check_password(username, password):
                print("\n Welcome to our Toy Store!\n")
                toy_store.is_logged=True
            else:
                print("\n Incorrect username :( Try again!")

        if opt == 1:
            name = input("Full name:")
            document_type = input("Document type:")
            id_crn = input("Type your ID or CRN:")
            phone = input("Phone:")
            address = input("Address:")
            username = input("Create a username:")
            email = input("Email:")
            password = input("Create a password:")

            new_user = User(name, document_type, id_crn, phone, address, username, email, password)
            toy_store.add_new_user(new_user)
            toy_store.is_logged = True

def check_availability(selected_product):
    if toy_store.cheking_product_availability_website(
            selected_product) or toy_store.cheking_product_availability_marketplace(selected_product):
        print("Available product")
        return True
    else:
        print("This product is unavailable")
        return False

def adding_toy_to_cart():
    selected_product_by_user = input("Type product ID:")
    if check_availability(selected_product_by_user):
        if not toy_store.is_logged:
            login_or_register()
        if shop.customer is None:
            shop.customer=toy_store.current_user
        selected_product_itself=toy_store.finding_products(selected_product_by_user)
        shop.add_products(selected_product_itself)
        shop.display()

# Phase_1: Listing all products and showing on screen

toy_store.listing_all_products()

# Phase_2, 3 and 4:

shop = ShoppingCart(0,None)
toy_store.add_new_shopping_cart(shop)

adding_toy_to_cart()

# Phase_5: user is asked if he or she wishes to continue buying or proceed to checkout

while True:
    click = int(input("If you wish to continue buying please click 1, otherwise click 2 to checkout :) "))
    if click == 1:
        toy_store.listing_all_products()
        adding_toy_to_cart()
    if click == 2:
        break

# Phase_6:system checks if vendor is the website or a third party, then offers the correspondent delivery methods

listing_delivery_methods=[]
def delivering():
    website_products=False
    marketplace_products=False

    for cart in toy_store.list_shopping_cart:
        if cart.customer==toy_store.current_user:
            for prod in cart.products:
                if prod.product_vendor == 1:
                    website_products=True
                if prod.product_vendor == 2:
                    marketplace_products=True

    if marketplace_products is True:
        listing_delivery_methods.append(company_postal_service)
    if website_products is True:
        click=0
        while click not in [1,2]:
            click=int(input("Choose a delivery method: 1-Postal Office, 2-In-house courier:"))
        if click==1:
            if company_postal_service not in listing_delivery_methods:
                listing_delivery_methods.append(company_postal_service)
        if click==2:
            listing_delivery_methods.append(company_in_house_courier)

delivering()

# Phase_7:system provides 4 payment methods and user chooses one

storing_payment_information = []


def promotional_code():
    p_cod = int(input("Please type your promotional code:"))
    loyalty = toy_store.finding_loyalty(p_cod)
    if loyalty is not None:
        storing_payment_information.append(loyalty)
    else:
        print("Invalid code")

def gift_voucher():
    g_code = int(input("Please type your gift:"))
    loyalty = toy_store.finding_loyalty(g_code)
    if loyalty is not None:
        storing_payment_information.append(loyalty)
    else:
        print("Invalid code")

def credit_debit_card():
    card = int(input("Please type your credit of debit card number:"))
    storing_payment_information.append(card)

def paypal():
    paypal = int(input("Please type your paypal number:"))
    storing_payment_information.append(paypal)

click = None

while click != 5:

    print("""Payment options: 
           1 - promotional_code 
           2 - Gift Voucher 
           3 - Credit/Debit 
           4 - Paypal
           5 - Proceed to Checkout""")

    click = int(input("Select one or more options: "))

    if click == 1:
        promotional_code()

    elif click == 2:
        gift_voucher()

    elif click == 3:
        credit_debit_card()

    elif click == 4:
        paypal()

paying=Payment(1,1,storing_payment_information,toy_store.current_user)
toy_store.add_new_payment(paying)

# Phase_8: system asks if user wants to store payment details or use stored details

def choosing_to_store_payment_details():
    choosing = int(input("If you want to store payment details, please type 1. If you don't, type 2:"))
    if choosing == 1:
        paying.stored_payment_details()
        print("Your payment details have been successfully stored")
    if choosing == 2:
        print("Your payment details have not been stored")

choosing_to_store_payment_details()


# Phase_9: payment is accepted and user receives an invoice message

def invoice():
    final_message = int(input("To finalize your payment and receive your invoice, please type 1:"))
    if final_message == 1:
        print("TOY STORE INVOICE:")
        toy_store.showing_onlineorders()

invoice()

for l in listing_delivery_methods:
    l.display()
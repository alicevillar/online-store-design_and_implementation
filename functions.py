from setup import *

        #PART 3: Creating methods inside each class - IMPLEMENTATION PHASE

# Function used in Phase 2, 3 and 4 of Part 4

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
        print("This product is available")
        return True
    else:
        print("This product is not available")
        return False


shop = ShoppingCart(0,None)
toy_store.add_new_shopping_cart(shop)

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

# Functions used in Phase 6 of Part 4

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
            click=int(input("Choose a delivery method: 1-Post Office, 2-In-house courier:"))
        if click==1:
            if company_postal_service not in listing_delivery_methods:
                listing_delivery_methods.append(company_postal_service)
        if click==2:
            listing_delivery_methods.append(company_in_house_courier)

# Functions used in Phase 7 of Part 4

storing_payment_information = []
def promotional_code():
    p_cod = int(input("Please enter your promotional code:"))
    loyalty = toy_store.finding_loyalty(p_cod)
    if loyalty is not None:
        storing_payment_information.append(loyalty)
    else:
        print("Invalid code")

def gift_voucher():
    g_code = int(input("Please enter your gift code:"))
    loyalty = toy_store.finding_loyalty(g_code)
    if loyalty is not None:
        storing_payment_information.append(loyalty)
    else:
        print("Invalid code")

def credit_debit_card():
    card = int(input("Please enter your credit or debit card number:"))
    storing_payment_information.append(card)

def paypal():
    paypal = int(input("Please enter your PayPal number:"))
    storing_payment_information.append(paypal)

# Function used in Phase 8 of Part 4

paying=Payment(1,1,storing_payment_information,toy_store.current_user)
toy_store.add_new_payment(paying)
def choosing_to_store_payment_details():
    choosing = int(input("If you want to store payment details, please enter 1. If you don't, enter 2:"))
    if choosing == 1:
        paying.stored_payment_details()
        print("Your payment details have been successfully stored")
    if choosing == 2:
        print("Your payment details have not been stored")

# Phase 9 of Part 4
#=> Payment is accepted and user receives an invoice message

def invoice():
    final_message = int(input("To finalize your payment and receive your invoice, please enter 1:"))
    if final_message == 1:
        print("TOY STORE INVOICE:")
        toy_store.showing_onlineorders()
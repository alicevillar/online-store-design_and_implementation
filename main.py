                                        # MY TOY STORE

# => Summary: The code is divided in four parts:

# ) PART 1: Creating 13 classes - DEFINITION PHASE (classes files)
# ) PART 2: Instantiating the class Store - INSTANTIATION PHASE (file setup.py)
# ) PART 3: Creating methods inside each class - IMPLEMENTATION PHASE (file functions.py)
# ) PART 4: Interacting with user - INTERACTION PHASE (file main.py)

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

from functions import *

# Phase 1: Listing all products and showing on screen

toy_store.listing_all_products()

# Phase 2, 3 and 4:

adding_toy_to_cart()

# Phase 5: user is asked if he or she wishes to continue buying or proceed to checkout

while True:
    click = int(input("If you wish to continue buying please click 1, otherwise click 2 to checkout :) "))
    if click == 1:
        toy_store.listing_all_products()
        adding_toy_to_cart()
    if click == 2:
        break

# Phase 6:System checks if vendor is the website or a third party, then offers the correspondent delivery methods

delivering()

# Phase 7:system provides 4 payment methods and user chooses one

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

# Phase 8: system asks if user wants to store payment details or use stored details

choosing_to_store_payment_details()

# Phase 9: payment is accepted and user receives an invoice message

invoice()

for l in listing_delivery_methods:
    l.display()
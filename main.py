                                        # MY TOY STORE

# => Summary: The development is divided into four parts:

# ) PART 1: Creating 13 classes - DEFINITION PHASE (class files)
# ) PART 2: Instantiating the class Store - INSTANTIATION PHASE (file setup.py)
# ) PART 3: Creating functions inside each class - IMPLEMENTATION PHASE (file functions.py)
# ) PART 4: Interacting with users - INTERACTION PHASE (file main.py)

                                # PART 4: Interacting with users

# Phase 1: Listing all products and showing them on the screen
# Phase 2: visitor selects a product
# Phase 3: system offers the possibility to register or login (if he or she is not)
# Phase 4: system checks product availablity and adds to shopping cart or says the product is not available
# Phase 5: user is asked if he or she wishes to continue buying (back to phase 1) or proceed to checkout
# Phase 6:system checks if vendor is the website or a third party, then offers the corresponding delivery methods
# Phase 7:system offers 4 payment methods and user chooses one or more
# Phase 8: system asks if user wants to store payment details or use stored details
# Phase 9: payment is accepted and user receives an invoice

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
           4 - PayPal
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
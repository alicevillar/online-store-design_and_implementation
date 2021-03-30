                                            # PART 4: Interacting with user

    # Phase_1: Listing all products and showing on screen
    # Phase_2: visitant selects a product
    # Phase_3: system offers the possibility to register or login (if he is not)
    # Phase_3.1:registration
    # Phase_3.2:login
    # Phase_4: system checks product availablity and adds to shopping cart or says that the product is not available
    # Phase_5: user is asked if he or she wishes to continue buying (back to 1) or checkout
    # Phase_6:system checks if vendor is the website or a third party, then offers the correspondent delivery methods
    # Phase_7:system provides 4 payment methods and user chooses one
    # Phase_8: system asks if user wants to store payment details or use stored details
    # Phase_9: payment is accepted and user receives an invoice message


# Phase_1: Listing all products and showing on screen

toy_store.listing_all_products()

# Phase_2: visitant selects a product

selected_product = int(input("Type product ID:"))

# Phase_3: system offers the possibility to register or login:

if not current_user.is_logged:
    opt = int(input("Hi! If you not registered, type 1 to join us. If you are registered, type 2 to login:"))
    if opt == 2:
        username = input("Type your username:")
        password = input("Type your password:")

ccc
        if Toy_Store.check_password(username,password):
            Toy_Store.is_logged = True
            print("\n Welcome to Toy Store!\n")
        else:
            print("\n Incorrect username :( Try again!")
    if opt == 1:
        username = input("Create a username:")
        u = User("", 0, username)
        Toy_Store.add_new_user(u)
        Toy_Store.is_logged = True

 #Registering a visitant

    def register():
        name= input("Name:")
        document_type=input("Document Type:")
        id_crn=input("ID or CRN:"")
        phone=input("Phone:")
        address=input("Address:")
        username = input("Username:")
        email = input("Email: ")
        password = input("Password: ")

    def add_new_user(self, users):
        users.id_crn = len(self.list_users) + 1
        self.list_users.append(users)
        print("\nWelcome! \n")

    def signin():
        username = input("Username: ")
        password = input("password: ")
        u = User(name,document_type,id_crn,phone,address, username,email,password)
        result = Toy_Store.check_password(u)
        global is_logged
        is_logged = result
        if result:
            print("\nSuccessful Login!\n")
        else:
            print("\nIncorrect username or password! Please try again.\n")


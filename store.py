

#Creating class Store with 12 lists:

class Store:
    list_users = []
    list_warehousestaff = []
    list_customers = []
    list_marketplace_vendors = []
    list_website_product = []
    list_marketplace_products = []
    list_online_orders = []
    list_delivery_company = []
    list_loyalty_schemes = []
    list_order_details = []
    list_payment = []
    list_shopping_cart=[]


#Creating two variables to be used in Part 4 ("Interacting with user")
    is_logged = False
    current_user = 0

# Creating 12 methods to add elements in each of the lists above:

    def add_new_user(self, users):
        users.id_crn = len(self.list_users) + 1
        self.list_users.append(users)
        self.current_user=users.id_crn

    def add_new_warehousestaff(self, warehousestaff):
        warehousestaff.id_crn = len(self.list_warehousestaff) + 1
        self.list_warehousestaff.append(warehousestaff)

    def add_new_customer(self, customers):
        customers.id_crn = len(self.list_customers) + 1
        self.list_customers.append(customers)

    def add_new_marketplace_vendor(self, marketplace):
        marketplace.id_crn = len(self.list_marketplace_vendors) + 1
        self.list_marketplace_vendors.append(marketplace)

    def add_new_website_product(self, website_product):
        website_product.product_id = "WP-" + str(len(self.list_website_product) + 1)
        self.list_website_product.append(website_product)

    def add_new_marketplace_product(self, marketplaceproduct):
        marketplaceproduct.product_id = "MP-" + str(len(self.list_marketplace_products) + 1)
        self.list_marketplace_products.append(marketplaceproduct)

    def add_new_onlineOrders(self, online_order):
        online_order.online_order_id = len(self.list_online_orders) + 1
        self.list_online_orders.append(online_order)

    def add_new_delivery_company(self,delivery_company):
        delivery_company.crn= len(self.list_delivery_company) + 1
        self.list_delivery_company.append(delivery_company)

    def add_new_loyalty_schemes(self,loyalty_schemes):
        loyalty_schemes.coupon_id= len(self.list_loyalty_schemes) + 1
        self.list_loyalty_schemes.append(loyalty_schemes)

    def add_new_order_details(self,order_details):
        order_details.online_order= len(self.list_order_details) + 1
        self.list_order_details.append(order_details)

    def add_new_payment(self,payment):
        payment.payment_id=len(self.list_payment) +1
        self.list_payment.append(payment)

    def add_new_shopping_cart(self, cart):
        cart.shopping_cart_id = len(self.list_shopping_cart) + 1
        self.list_shopping_cart.append(cart)

# Creating 2 methods to list products from the website and products from the marketplace

    def listing_website_Product(self):
        for p in self.list_website_product:
            print(f"Product name: {p.product_name} \n Product ID: {p.product_id}")

    def listing_marketplaceProducts(self):
        for p in self.list_marketplace_products:
            print(f"Product name: {p.product_name} \n Product ID: {p.product_id}")

# Creating one method to list all products (this function is used in phase 1 of Part 4)

    def listing_all_products(self):
        self.listing_website_Product()
        self.listing_marketplaceProducts()

#Finding user's loyalty scheme

    def finding_loyalty(self,loyalty_id):
        for l in self.list_loyalty_schemes:
            if l.coupon_id==loyalty_id:
                return l
        return None

#Finding products

    def finding_products(self,product_id):
        for p in self.list_website_product:
            if p.product_id==product_id:
                return p

        for p in self.list_marketplace_products:
            if p.product_id==product_id:
                return p

# 2 methods to dhecking products availability
    def cheking_product_availability_website(self,selected_product_ID_website):
        for p in self.list_website_product:
            if p.product_id == selected_product_ID_website:
                if p.quantity > 0:
                    return True
                else:
                     return False
        return False

    def cheking_product_availability_marketplace(self,selected_product_ID_marketplace):
        for p in self.list_marketplace_products:
            if p.product_id == selected_product_ID_marketplace:
                if p.quantity > 0:
                    return True
                else:
                    return False
        return False


# Creating one method to check password:

    def check_password(self, un,pw):
        for u in self.list_users:
            if u.username.lower()==un.lower() and u.password==pw:
                self.current_user=u.id_crn
                return True
        else:
            return False

# Creating one method to find user in users list by username:

    def finding_user(self,un):
        for u in self.list_users:
            if u.username == un:
                return u

# Creating one method to show online orders:

    my_cart_prod=[]

    def showing_onlineorders(self):
        for user in self.list_users:
            if user.id_crn == self.current_user:
                print(f"Username: {user.username}, Address: {user.address}")

        for cart in self.list_shopping_cart:
            if cart.customer==self.current_user:
                self.my_cart_prod=cart.products

        for p in self.list_payment:
            if p.customer==self.current_user:
                p.stored_payment_details()

        for ol in self.list_order_details:
            print(f"Online order: {ol.online_order}")


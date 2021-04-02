
#Creating class Store with 12 lists:

class Store:
    list_users = []
    list_warehousestaff = []
    list_customers = []
    list_marketplace_vendors = []
    list_website_Product = []
    list_marketplaceProducts = []
    list_shoppingCart = []
    list_onlineOrders = []
    list_deliveryCompany = []
    list_loyaltySchemes = []
    list_orderDetails = []
    list_payment = []


#Creating two variables to be used in Part 4 ("Interacting with user")
    is_logged = False
    current_user = 0

# Creating 12 functions with methods to add elements in each of the lists above:

    def add_new_user(self, users):
        users.id_crn = len(self.list_users) + 1
        self.list_users.append(users)

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
        website_product.product_id = "WP-" + str(len(self.list_website_Product) + 1)
        self.list_website_Product.append(website_product)

    def add_new_marketplace_product(self, marketplaceproduct):
        marketplaceproduct.product_id = "MP-" + str(len(self.list_marketplaceProducts) + 1)
        self.list_marketplaceProducts.append(marketplaceproduct)

    def add_new_cart(self, cart):
        cart.shopping_cart_id = len(self.list_shoppingCart) + 1
        self.list_shoppingCart.append(cart)

    def add_new_onlineOrders(self, online_order):
        online_order.online_order_id = len(self.list_onlineOrders) + 1
        self.list_onlineOrders.append(online_order)

    def add_new_delivery_company(self,delivery_company):
        delivery_company.crn=len(self.list_deliveryCompany) +1
        self.list_deliveryCompany.append(delivery_company)

    def add_new_loyalty_schemes(self,loyalty_schemes):
        loyalty_schemes.coupon_id=len(self.list_loyaltySchemes) +1
        self.list_loyaltySchemes.append(loyalty_schemes)

    def add_new_order_details(self,order_details):
        order_details.online_order=len(self.list_orderDetails) +1
        self.list_orderDetails.append(order_details)

    def add_new_payment(self,payment):
        payment.payment_id=len(self.list_payment) +1
        self.list_payment.append(payment)


# Creating 2 methods to list products from the website and products from the marketplace

    def listing_website_Product(self):
        for p in self.list_website_Product:
            print(f"Product name: {p.product_name} \n Product ID: {p.product_id}")

    def listing_marketplaceProducts(self):
        for p in self.list_marketplaceProducts:
            print(f"Product name: {p.product_name} \n Product ID: {p.product_id}")

# Creating one method to list all products

    def listing_all_products(self):
        self.listing_website_Product()
        self.listing_marketplaceProducts()

#Finding user's loyalty scheme

    def finding_loyalty(self,loyalty_id):
        for l in self.list_loyaltySchemes:
            if l.coupon_id==loyalty_id:
                return l
        return None

# Checking products availability (return true of false)
    def cheking_product_availability_website(self,selected_product_ID_website):
        for p in self.list_website_Product:
            if p.product_id == selected_product_ID_website:
                if p.quantity > 0:
                    return True
                else:
                     return False
        return False

    def cheking_product_availability_marketplace(self,selected_product_ID_marketplace):
        for p in self.list_marketplaceProducts:
            if p.product_id == selected_product_ID_marketplace:
                if p.quantity > 0:
                    return True
                else:
                    return False
        return False


# Creating one method to check password:

    def check_password(self, un,pw):
        for u in self.list_users:
            if u.username==un and u.password==pw:
                self.current_user=u.id_crn
                return True
        else:
            return False

    def finding_user(self,un):
        for u in self.list_users:
            if u.username == un:
                return u
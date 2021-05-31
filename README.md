
# Toy Store 

The following software system was the end of Module 2 (“Object-oriented Information Systems”) assignment in my MSc in Computer Science at the University of Essex, UK. 

This project has been an extraordinary opportunity for me to develop OO programming skills. To push the project even further I decided to use multilevel inheritance. 
In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class. In my project, the class “People” is a superclass. The class User inherits from People. Three other subclasses (customers, warehouse staff and marketplace) will inherit from User (and therefore will also indirectly inherit from People).


## Assignment topic: Online Store System Design 

Design a software system that allows customers to search for products sold at the website and add them to their shopping basket - at this stage an order is in progress. Products are sold both by the website itself and several third-party sellers. Third-party sellers can be individuals or organisations, and once they have registered as a seller, they maintain their own product catalogue, pricing and storefront. If a product is temporarily out of stock, then it will be marked as unavailable.

Once customers have finished shopping, the orders are considered to be processing and they are taken through the checkout process, where they will specify delivery details. Customers have the choice of several delivery options, including standard delivery using the postal service and the company’s own in-house courier service. Products ordered from third-party sellers at the marketplace do not have access to the in-house courier system. When the delivery options have been chosen, then the customers are presented with the payment options, where they can opt to use a credit or debit card, an online payment service (e.g., PayPal) or a gift voucher.  Additionally, customers may use promotional codes that are periodically issued by the website.  Customers have the option to store their payment details and so can simply use stored details for each purchase.  At this stage, the order is pending payment, but once the customers submits their payment information, the validity of the account used (whether it is PayPal, a credit/debit card or gift voucher) will be verified by the appropriate service.  Upon successful completion, the order is awaiting pick up.

When a customer completes a transaction, the order is passed to the warehouse staff.  The warehouse staff will be required to look up the items in the stock database to determine the location of the item in the warehouse. Once the items are successfully collected and packaged, the order will be considered ready for delivery and distributed to the appropriate delivery company, depending on the customers’ preferences. When a member of the warehouse staff selects an item to fulfill a customer order, the item is scanned with a handheld terminal to automatically update the stock levels (which will be reflected on the website). Finally, the order is collected by the appropriate delivery company and marked as shipped.
Using the scenario provided, you should design and develop:

*	A class diagram.
*	An activity diagram for the process of a customer completing an order.
*	A state diagram highlighting the states of an order (and their transitions) for your proposed system.
*	Implement these diagrams using object-oriented Python.
 
## Approach

My software system project is an online store called “Toy Store”. The project contains the architecture (class diagram, activity diagram, state diagram)) and implementation in Python.     

The development of the code is divided into four parts: 

Part 1: Creating 13 classes - DEFINITION PHASE (class files)
Part 2: Instantiating the class Store - INSTANTIATION PHASE (file setup.py)
Part 3: Creating functions inside each class - IMPLEMENTATION PHASE (file functions.py)
Part 4: Interacting with users - INTERACTION PHASE (file main.py)


#### Part 1 is the definition phase. Here the following classes are created:  

* people 
*	user 
*	warehousestaff  
*	customers
*	websiteproducts
*	marketplaceproducts
*	marketplace
*	onlineorders
*	deliverycompany
*	loyaltyschemes
*	orderdetails
*	payment
*	shoppingcart
*	store 

#### Part 2 instantiates classes. Here Toy Store is created.    

#### Part 3 is aimed to create functions, which are in the file “functions.py”:

*	Functions to add elements in each class. 
*	Functions to list products from the website and products from the marketplace. 
*	Function to list all products. 
*	Function to find user's loyalty scheme.
*	Functions to check products availability (from the website or marketplace).
*	Function to check password.
*	Function to show online orders.


#### Part 4 is the interaction phase. Here is where the functions created in Part 3 are being used, so the system can interact with users. This part of the code is separated into 9 phases:

* Phase 1: Listing all products and showing them on the screen
* Phase 2: visitor selects a product
* Phase 3: system offers the possibility to register or login (if he or she is not)
* Phase 4: system checks product availability and adds to shopping cart or says the product is not available
* Phase 5: user is asked if he or she wishes to continue buying (back to phase 1) or proceed to checkout
* Phase 6:system checks if vendor is the website or a third party, then offers the corresponding delivery methods
* Phase 7:system offers 4 payment methods and user chooses one or more
* Phase 8: system asks if user wants to store payment details or use stored details
* Phase 9: payment is accepted and user receives an invoice

## Sample Flows 

Here are sample flows from my Toy Store: 
 
#### Flow A –> Login Richard – buying LEGO Starship (product ID: MP-1) from the website using a credit card: 

```
> Type product ID: MP-1  
> Hi! If you not registered, type 1 to join us. If you are registered, type 2 to login: 2
> Type your username: Rich
> Type your password: 321
> If you wish to continue buying please click 1, otherwise click 2 to checkout :) 2
> Payment options: 
   1 - promotional_code 
   2 - Gift Voucher 
   3 - Credit/Debit 
   4 - Paypal
   5 - Proceed to Checkout
> Select one or more options: 3
> Please enter your credit or debit card number: enter any number

> TOY STORE INVOICE:
Username: Rich, Address: Avenue YYY
Online order: 1
Delivery Company name Postal Office CRN: 1 Registration 222
``` 

#### Flow B –> Login Alice – buying Barbie Bee (product ID: WP-1) from the marketplace using gift voucher and paying with PayPal: 

 ```
> Type product ID: WP-1
> This product is available
> Hi! If you not registered, type 1 to join us. If you are registered, type 2 to login: 2
> Type your username: Ali
> Type your password: 123  
> If you wish to continue buying please click 1, otherwise click 2 to checkout :) 2
> Choose a delivery method: 1-Post Office, 2-In-house courier: 2
Payment options: 
   1 - promotional_code 
   2 - Gift Voucher 
   3 - Credit/Debit 
   4 - Paypal
   5 - Proceed to Checkout
> Select one or more options: 2
> Please enter your gift code:1
Payment options: 
   1 - promotional_code 
   2 - Gift Voucher 
   3 - Credit/Debit 
   4 - Paypal
   5 - Proceed to Checkout
> Select one or more options: 5
> If you want to store payment details, please enter 1. If you don't, enter 2:1

> To finalize your payment and receive your invoice, please enter 1:1

> TOY STORE INVOICE:
Username: Ali, Address: Avenue XXX
Online order: 1
Delivery Company name In-house courier CRN: 2 Registration 333
```

from datetime import datetime

#13) Class Payment

class Payment:
    def __init__(self,payment_id,online_order_id,payment_methods,customer):
        self.payment_id=payment_id
        self.online_order_id=online_order_id
        self.payment_methods=payment_methods
        self.customer=customer
        self.date=datetime.now()

# Function to show stored payment infomation:
    def stored_payment_details(self):
        for p in self.payment_methods:
            if type(p) is int:
                print(f"Number:\n", p)
            else:
                print(f"Coupon name: \n {p.coupon_name}")



#11) Class Loyalty_Schemes with 3 attributes and 3 methods
class LoyaltySchemes:
    def __init__(self,coupon_name, coupon_id,total):
        self.coupon_name= coupon_name
        self.coupon_id=coupon_id
        self.total=total

    # Functions to create 3 methods:
    def display(self):
        print("Coupon name:", self.coupon_name,"Coupon ID:",self.coupon_id,"Total:",self.total)


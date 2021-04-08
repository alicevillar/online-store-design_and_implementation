
#11) Class Loyalty_Schemes
class LoyaltySchemes:
    def __init__(self,coupon_name, coupon_id,pc_gv, total):
        self.coupon_name= coupon_name
        self.coupon_id=coupon_id
        self.total=total
        self.pc_gv=pc_gv

    # Functions to create method display:
    def display(self):
        print("Coupon name:", self.coupon_name,"Coupon ID:",self.coupon_id,"Total:",self.total)



#13) Class Payment with 3 attributes paymentId,shoppingCartId,loyaltyId

class Payment:
    def __init__(self,payment_id,online_order_id,loyalty_id):
        self.payment_id=payment_id
        self.online_order_id=online_order_id
        self.loyalty_id=loyalty_id


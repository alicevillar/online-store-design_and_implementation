#9) Class OnlineOrders with 3 attributes onlineOrderId,productId,customerId
class OnlineOrders:
    def __init__(self,online_order_id,products,customer):
        self.online_order_id=online_order_id
        self.products=products
        self.customer=customer


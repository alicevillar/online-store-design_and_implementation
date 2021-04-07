#12) Class OrderDetails with 1 attribute orderId
class OrderDetails:
    def __init__(self,online_order,chosen_delivery_company=None):
        self.online_order=online_order
        self.chosen_delivery_company=chosen_delivery_company

    # Functions to create 1 method: generating a report

    def report(self):
        pass


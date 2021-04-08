#5)Class Marketplace

from user import User

class Marketplace(User):
    def __init__(self,name,document_type,id_crn,phone,address, username,email,password,individual_seller_name,individual_seller_id,company_seller_name,
                 company_seller_crm,total_sellers,registration,marketplace_products):
        super().__init__(name,document_type,id_crn,phone,address, username,email,password)
        self._individual_seller_name=individual_seller_name
        self._individual_seller_id=individual_seller_id
        self._company_seller_name=company_seller_name
        self._company_seller_crm=company_seller_crm
        self.total_sellers=total_sellers
        self.registration=registration
        self.marketplace_products=marketplace_products


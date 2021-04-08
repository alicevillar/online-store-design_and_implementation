
#10) Class Delivery Company
class DeliveryCompany:
    def __init__(self,name,crn,registration):
        self.name=name
        self.crn=crn
        self.registration=registration

# Functions to create one method:
    def display(self):
        print("Delivery Company name",self.name,"CRN:",self.crn, "Registration",self.registration)


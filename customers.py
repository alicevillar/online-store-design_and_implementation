
#4)Class Customers

from user import User
class Customers(User):
    def __init__(self,name, document_type, id_crn, phone, address, username, email, password,purchase_history):
        super().__init__(name, document_type, id_crn, phone, address, username, email, password)
        self.purchase_history=purchase_history

#Function to create one method:
    def display(self):
        print("Name:",self.name,"Document Type:",self.document_type,"Id or crn:",self.id_crn,"Phone:",self.phone,"Address:",self.address,
              "Username:",self.username,"Email:",self.email,"Password",self.password,"Purchase History:",self.purchase_history)


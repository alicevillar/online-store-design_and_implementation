
from people import People

#2) Class User inherits from People
class User(People):
    def __init__(self,name,document_type,id_crn,phone,address, username,email,password):
        super().__init__(name,document_type,id_crn,phone,address)
        self.username=username
        self.email=email
        self.password=password


# Function to create method display:
    def display(self):
        print("Name:", self.name,"Document Type",self.document_type,"ID or CRN:",self.id_crn,
              "Phone:", self.phone, "Address", self.address, "Username:", self.username)


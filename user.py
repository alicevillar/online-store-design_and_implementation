
from people import People

#2) Class User inherits from People and has 3 attributes
class User(People):
    def __init__(self,name,document_type,id_crn,phone,address, username,email,password):
        super().__init__(name,document_type,id_crn,phone,address)
        self.username=username
        self.email=email
        self.password=password


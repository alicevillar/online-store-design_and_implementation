#3) Class WarehouseStaff - inherits from User
from user import User

class Warehousestaff(User):
    def __init__(self, name,document_type,id_crn,phone,address, username,email,password,
                 position,staff_id,salary):
        super().__init__(name,document_type,id_crn,phone,address, username,email,password)
        self.position=position
        self.staff_id=staff_id
        self.salary=salary

#Function to create one method:
    def display (self):
        print("Name:",self.name,"Document Type:",self.document_type,"Id or crn:",self.id_crn,
              "Phone:",self.phone,"Address:",self.address,
              "Username:",self.username,"Email:",self.email,"Password",self.password,
              "Position:",self.position,"Staff ID",self.staff_id,"Salary:",self.salary)


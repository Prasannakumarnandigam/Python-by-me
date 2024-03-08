class Customer:
    def __init__(self, id, name,B_DoorNo, B_street, B_city, B_country, B_postalcode,S_DoorNo, S_street, S_city, S_country, S_postalcode ):
        self.Customer_id = id
        self.Customer_name = name
        self.Billing_Address = self.Address(B_DoorNo, B_street, B_city, B_country, B_postalcode)
        self.Shipping_Address = self.Address(S_DoorNo, S_street, S_city, S_country, S_postalcode)
    class Address:
        def __init__(self, DoorNo ,street, city, country, postalCode):
            self.DoorNo = DoorNo
            self.street = street
            self.city = city
            self.country = country
            self.postalcode = postalCode

        def displayAddress(self):
            print(self.DoorNo,  self.street, self.city, self.country, self.postalcode)

c = Customer(2001,'Prasanna Kumar', 1423, 'Ragu Ram Nagar ', 'Sattenapalli', "India", 522403, 1312, 'shivaji nagar', 'Sattenapalli', "India", 522403 )
print(c.Billing_Address.displayAddress())
print(c.Shipping_Address.displayAddress())

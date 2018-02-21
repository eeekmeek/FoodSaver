from datetime import date

class Item:
    
    def __init__(self, name, dop, expiry, qty, category):
        ''' constructor '''
        self.name = name
        self.dop = dop
        self.expiry = expiry
        self.qty = qty
        self.category = category
     
    def get_name(self):
        return self.name
    def get_dop(self):
        return self.dop
    def get_expiry(self):
        return self.expiry    
    def get_qty(self):
        return self.qty
    def get_category(self):
        return self.category
        
    def set_name(self, new_name):
        ''' weight modifier/mutator '''
        self.name = new_name
    
    def set_dop(self, new_dop):
        ''' height modifier/mutator '''
        self.dop = new_dop
    
    def set_expiry(self, new_expiry):
        self.expiry = new_expiry
    
    def set_qty(self, new_qty):
        self.qty = new_qty
    
    def set_category(self, category):
        self.category = new_category
        

    def display(self):
        ''' helper/support '''
        print("Name:", self.name)
        print("Date of purchase:", self.dop)
        print("Expiry date:", self.expiry)
        print("Quantity:", self.qty)
        print("Category:", self.category)
    
# main
input_name = raw_input("Enter item: ")
input_dop = date.today()
input_expiry = date.today()
input_qty = int(input("Quantity purchased: "))
input_category = raw_input("Food type: ")
i1 = Item(input_name, input_dop, input_expiry, input_qty, input_category)
i1.display()



class Pojistenci():
#class for adding new insured

    def __init__(self, name, lastname, age, telephone) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age
        self.telephone = telephone
    
    
    def __repr__(self) -> str:
        #return string
        return f'{self.name} {self.lastname}, {self.age} let, tel: {self.telephone}'

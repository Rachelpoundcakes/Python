class BusinessCard:
        def __init__(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
        def print_info(self):
                print("--------------------")
                print("Name: ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")

person1 = BusinessCard("MJ.K", "XXX@gmail.com", "Seoul, Republic of Korea")
person1.print_info()
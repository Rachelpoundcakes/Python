class Employee:
    def __init__(self):
        self.months = 0
    
    def get_months(self): # 값을 불러오는 getter
        return self.months
    
    def set_months(self, value):  # 값을 저장하는 setter
        self.months = value

Justin = Employee()
Justin.set_months(24)
print(Justin.get_months())
        
    
    
    
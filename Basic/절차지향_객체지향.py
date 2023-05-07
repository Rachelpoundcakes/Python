"""
객체 지향 프로그래밍?
- 프로그램을 객체 단위로 생각하고 객체끼리 상호작용 
- 코드 중복 방지, 코드 재사용 및 유지보수를 위해 사용

절차 지향 프로그래밍?
- 순차적으로 진행되는 프로그래밍
"""

# 절차 지향
smarthphone1 = 'Samsung'
smarthphone_information_1 = [
    {'color': 'Rose Gold'},
    {'price': 1000000}
]

# 객체 지향
class Smartphone:
    def __init__(self, brand, price):
        self._brand = brand
        self._price = price
    
    def __str__(self):
        return f'str: {self._brand} - {self._price}'

samsung = Smartphone('Samsung', 1000000)
print(samsung)

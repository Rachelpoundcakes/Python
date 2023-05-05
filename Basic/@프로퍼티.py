# @property로 getter와 setter 구현하기

class Employee:
    def __init__(self):
        self.__months = 0
    
    @property
    def months(self):
        return self.__months
    
    @months.setter
    def months(self, value):
        self.__months = value

Rachel = Employee()
Rachel.months = 24
print(Rachel.months)

"""
@property와 @months.setter를 붙이면 메서드를 속성처럼 사용할 수 있다.
값을 저장할 때는 Rachel.months =24처럼 메서드에 바로 값을 할당하면 되고, 
값을 가져올 때도 Rachel.months처럼 메서드에 바로 접근하면 된다.
"""
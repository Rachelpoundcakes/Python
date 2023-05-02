# Class
## 계산기 만들기

result = 0

def add(num):
    global result
    result += num
    return result

print(add(1))
print(add(2))

# 만약 여러 대의 계산기가 필요하다면?

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(1))
print(cal1.add(2))
print(cal2.add(3))
print(cal2.add(4))
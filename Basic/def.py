# 함수 만들기1: 입력값이 있는 함수
def salary(b):
    return b*12*0.9


print(salary(400))

# 함수 만들기2: 입력값이 없는 함수
def salary():
    return b*12*0.9

b = 400
a = salary()
print(a)

# 함수 만들기3: 리턴값이 없는 함수
def salary(b):
    print("연봉은 %d입니다." %(b*12*0.9))

salary(400)

"""
a = salary(400)
print(a) 
이렇게 하면 None값이 출력된다
"""
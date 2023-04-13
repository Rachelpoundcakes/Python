# 숫자형을 알아보자

## 정수형
a = 123
a = -123

## 실수형
a = 4.5
a = 1.2E10 # 1.2*10^10
a = 1.2e-10 # 1.2*10^-10

## 8진수와 16진수
a = 0o175
a = 0xABC

### 연산자를 알아보자
a = 5
b = 8
print(a ** b) # 5^8
print(a % b) # 나머지 반환
print(a // b) # 몫을 반환


# 문자열을 알아보자

a = "Coding is fun!"

## 문자열 더하기
a = "I love"
b = " bread"
print(a + b)

## 문자열 곱하기
print(a * 2) # Coding is fun!Coding is fun!

## 문자열 길이 구하기
print(len(a)) # 14

## 문자열 인덱싱
print(a[2]) # d

## 문자열 슬라이싱
a = "Coding is fun!"
b = a[0] + a[7] + a[10] # Cif
b = a[0:6] # 연속된 것 구하기 Coding 

## 이스케이프 코드
a = "Coding is fun!\nI love coding"
"""
Coding is fun!
I love coding
"""
escape_code = ["\n", "\t", "\\", "\'", "\"", "\r", "\f", "\a", "\b", "\000"]

a = "         \rCoding is fun!I love coding"
print(a) # Coding is fun!I love coding

## 문자열 포매팅

### 포맷팅 연산자 
format_code = ["%d", "%f", "%s", "%o", "%x", "%%"]


a = "나는 오늘 %dkcal를 섭취했다." % 1200
print(a)

a = "%-8sworld" % "hello" # 대입되는 값 왼쪽 정렬
print(a)

a = "원주율은 %.2f이다." % 3.141592
print(a)

## format 함수를 사용한 포매팅
a = "나는 하루에 약 {}kcal를 섭취한다.".format(1200)
print(a)

a = "나는 매일 과일을 먹는다. 오늘은 {}을/를 먹었다.".format("사과")
print(a)

a = "나는 매일 {}을/를 먹는다. 오늘은 {}을/를 먹었다.".format("빵", "크루아상")
print(a)

a = "오늘은 {date}입니다. 오늘 날씨는 {weather}입니다.".format(date="4월 13일", weather="흐림")
print(a)

## f 문자열 포매팅
name = "김민정"
tone = "쿨"
intro = f"제 이름은 {name}입니다. 제 피부는 {tone}톤입니다."
print(intro)

## 딕셔너리에서의 포매팅: key:value
dic = {'name':'김민정', 'tone':'쿨'}
intro = f"제 이름은 {dic['name']}입니다. 제 피부는 {dic['tone']}톤입니다."
print(intro)

## 문자 개수 세기
a = "Rainbow"
print(a.count('i'))

## 위치 알려주기 1
print(a.find('i'))

## 위치 알려주기 2
print(a.index('i'))

## 문자열 삽입
print(",".join(a))

## 대문자로 바꾸기
print(a.upper())
print(a.lower())

## 공백 지우기
a = "  Rainbow  "
print(a.lstrip()) # 왼쪽
print(a.rstrip()) # 오른쪽
print(a.strip()) # 양쪽

## 문자열 replace
a = "I love cherry blossoms"
print(a.replace("cherry blossoms", "rose"))

## 문자열 split
print(a.split()) # ['I', 'love', 'cherry', 'blossoms']


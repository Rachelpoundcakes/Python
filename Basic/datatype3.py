## 튜플 자료형
t = (1, 2, 3, 'c', 'd')

"""
튜플은 요솟값을 변화시킬 수 없다는 점에서 리스트와 차이가 있다.
"""
### 튜플 인덱싱
print(t[4]) # d

### 튜플 더하기
t2 = ('d', 'f')
t3 = t + t2
print(t3) # (1, 2, 3, 'c', 'd', 'd', 'f')

### 튜플 곱하기
t4 = t2 * 2
print(t4) # ('d', 'f', 'd', 'f')

### 튜플 길이 구하기
print(len(t3)) #7


## 딕셔너리 자료형 {key1:value2, key2:value2, key3:value3...}

### 요소 추가하기
dic = {'이름': '김민정', '성별': '여성', '피부톤': '쿨톤'}
dic['선호하는 화장품 브랜드'] = '이니스프리'
print(dic)

### 요소 삭제하기
del dic['이름']
print(dic)

### key 사용하여 value 얻기
print(dic['성별']) # 여성

### key 리스트 리턴하기
a = dic.keys()
print(a) # dict_keys(['성별', '피부톤', '선호하는 화장품 브랜드'])

for k in dic.keys():
    print(k)

"""
성별
피부톤
선호하는 화장품 브랜드
"""

### 딕셔너리 key객체를 리스트로 변환하기
list1 = list(dic.keys())
print(list1) # ['성별', '피부톤', '선호하는 화장품 브랜드']

### value 리스트로 리턴하기
b = dic.values()
print(b) #dict_values(['여성', '쿨톤', '이니스프리'])

### 딕셔너리 value객체를 리스트로 변환하기
list2 = list(dic.values())
print(list2) # ['여성', '쿨톤', '이니스프리']

### key, value 쌍 얻기 ==> 튜플로 묶어서 반환한다
c = dic.items()
print(c) # dict_items([('성별', '여성'), ('피부톤', '쿨톤'), ('선호하는 화장품 브랜드', '이니스프리')])

### key:value 지우기
print(dic) # {'성별': '여성', '피부톤': '쿨톤', '선호하는 화장품 브랜드': '이니스프리'}
dic.clear()
print(dic) # {}


### key 사용하여 value 얻기 - dic['성별']방법이 있었지만 get을 사용할 수 있다
dic = {'이름': '김민정', '성별': '여성', '피부톤': '쿨톤'}
n = dic.get('이름')
print(n) # 김민정

### key가 딕셔너리 안에 있는지 조사하기
print('성별' in dic) # True








## 집합 자료형
## 불 자료형

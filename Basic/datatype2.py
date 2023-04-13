## 리스트 인덱싱
a = [1, 2, 3]
print(a[0])
a = [1, 2, 3, [4, 5, 'c']]

## 리스트 슬라이싱
print(a[0:4]) # [1, 2, 3, ['4, 5, c']]

## 리스트 수정, 삭제, 추가
a[3] = 4
print(a) # [1, 2, 3, 4]

del a[0]
print(a) # [2, 3, 4]

a.append(6)
print(a) # [2, 3, 4, 6]

## 리스트 정렬하기
a = [3, 1, 2, 7, 5, 4, 6]
a.sort()
print(a) # [1, 2, 3, 4, 5, 6, 7]

## 리스트 reverse
a.reverse()
print(a) # [7, 6, 5, 4, 3, 2, 1]

## 인덱스 반환
print(a.index(2))

## 리스트에 요소 삽입 *append는 추가, inser는 a번째 위치에 b를 삽입하는 함수
a.insert(0, "k")
print(a) # ['k', 7, 6, 5, 4, 3, 2, 1]

## 리스트 요소 제거 * del는 삭제, remove는 첫번재 x 삭제
a.remove('k')
print(a) # [7, 6, 5, 4, 3, 2, 1]

## 리스트 pop() -> 반환한 요소 삭제
a.pop() # 마지막 요소 삭제
a.pop(2) # x번째 요소 삭제
print(a) #[7, 6, 4, 3, 2] -> 5가 삭제되었다

## 리스트 요소 x의 개수 count
a = [1, 2, 2, 1, 3, 3, 4, 4, 5, 6, 7, 1, 1, 8]
print(a.count(1)) # 4

## 리스트 확장 extend
a = [4, 5, 6]
a.extend([7, 8]) #[4, 5, 6, 7, 8]
print(a)

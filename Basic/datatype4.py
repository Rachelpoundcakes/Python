## 집합(set) 자료형
a = set([1, 2, 3, 3, "c", "d", 4, 5])
print(a) # {1, 2, 3, 4, 5, 'c', 'd'} 출력 시, 중복된 건 제거되고 문자열은 맨 뒤로 간다.

### 교집합
b = set([2, 5, 7, 1, 3])
c = set([3, 5, 8, 1, 2, 8])
print(b&c) # {1, 2, 3, 5}

### 합집합
print(b|c) # {1, 2, 3, 5, 7, 8}
print(b.union(c)) # {1, 2, 3, 5, 7, 8}

### 차집합
print(b - c) # {7}
print(b.difference(c)) # {7}

### add
a = set([1, 2, 3, 4, 5])
a.add(6)
print(a)

a.update([7, 8, "c"])
print(a) # {1, 2, 3, 4, 5, 6, 7, 8, 'c'}

### remove
a.remove(7)
print(a) # {1, 2, 3, 4, 5, 6, 8, 'c'}

a.difference_update([1, 2, 3])
print(a) # {4, 5, 6, 8, 'c'}

## bull  자료형
a = True
b = False
print(type(a)) # <class 'bool'>
import numpy as np 
# as np라고 줄여서 부르겠다는 의미
arr = np.array({1, 2, 3, 4})
print(arr)

# arr 타입 확인하기
print(type(arr))

# 0으로 초기화된 배열. 0으로 맞춰주는 이유? 이전에 사용했던 것의 찌꺼기가 남아있기 때문 #2차원 벡터
arr = np.zeros((3, 3))
print(arr)

# 빈 값으로 만들어진 배열
arr = np.empty((4,4))
print(arr)

# 1로 가득찬 배열을 만든다

arr = np.ones((3, 3))
print(arr)

# 배열의 생성
arr = np.arange(10)
print(arr)

# ndarray 배열의 모양, 차수 , 데이터 타입 확인하기
arr = np.array([[1, 2, 3,],[4, 5, 6]])
print(arr)

arr.shape

#차원
arr.ndim

arr.dtype

#float 크기가 클수록 표현할 수 있는 양 많아짐
arr_float = arr.astype(np.float64)
arr_float.dtype

arr_str = np.array(['1', '2', '3'])
arr_str.dtype

arr_int = arr_str.astype(np.int64)
arr_int.dtype

#nadrray 배열의 연산

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr1 + arr2

# 다음과 같이 해도 됨
np.add(arr1, arr2)

arr1 * arr2

# 다음과 같이 해도 됨
np.multiply(arr1, arr2)

# ndarray 배열 슬라이싱 하기
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr.ndim

arr_1 = arr[:2, 1:3]
print(arr_1)

arr[0, 2]

arr[[0, 1 ,2],[2, 0, 1]]

idx = arr > 3
print(idx)

print(arr[idx])

# 첫줄은 헤더니깐 건너뛰고, 다음은 delimiter = 구별자
np.loadtxt(fname='winequality-red.csv', delimiter=';', skiprows=1)

# 변수명 redwine으로 저장
redwine = np.loadtxt(fname='winequality-red.csv', delimiter=';', skiprows=1)
print(redwine)

# 전체 데이터의 합계 (의미없음!! 와인 데이터 다 더하는 것이므로...)
print(redwine.sum())

# 평균 내기
print(redwine.mean())

# 0번 축을 기준으로 합계를 내면 항목의 합으로 나온다. 품질까지 12개 column에 대한 합계가 나옴
# 축(axis)
print(redwine.sum(axis=0))

# 평균
print(redwine.mean(axis=0))

# 이제 슬라이싱을 해 본다. :은 전체 데이터를 의미. 0은 제일 첫번째 컬럼을 의미 fixed acid 항목 쭉 나옴
redwine[:, 0]

redwine[:,0].mean()

# axis 축을 기준으로. 가장 좋은 퀄리티:72, 도수 가장 높은 것:14.9 
redwine.max(axis=0)

# 가장 낮은 퀄리티: 3, 도수 가장 낮은 것: 8.4
redwine.min(axis=0)


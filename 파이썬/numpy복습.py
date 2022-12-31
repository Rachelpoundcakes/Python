import numpy as np
arr = np.array({1, 3, 5, 7}) # 배열 만들기
print(arr)
"""
{1, 3, 5, 7}
"""
print(type(arr))
"""
<class 'numpy.ndarray'>
"""
arr = np.zeros((5, 5))
# 2차원 벡터 5x5 배열을 만들어 0으로 초기화 해준다.
# 혹시 모를 이전의 흔적을 지우기 위함
print(arr)
"""
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
 """
 
arr = np.empty((3, 3)) # 빈 값으로 만들어진 2차원 벡터 3x3 배열 만들기
print(arr)
"""
[[0.00e+000 0.00e+000 0.00e+000]
 [0.00e+000 0.00e+000 4.98e-321]
 [0.00e+000 0.00e+000 0.00e+000]]
"""
arr = np.ones((3, 3)) # 1로 되어 있는 3x3 배열 만들기
print(arr)
"""
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
"""
arr = np.arange(8) # 배열 생성하기 0부터 ()안의 숫자 -1까지 생성
print(arr)
"""
[0 1 2 3 4 5 6 7]
"""
arr = np.array([[3, 5, 8], [2, 5, 4]])
print(arr.shape)
"""
(2, 3) 

[[3, 5, 8]],
[[2, 5, 4]]
--> 2x3 배열
"""
print(arr.ndim)
"""
2
2차원 배열
"""
print(arr.dtype)
"""
int32
"""
arr_float = arr.astype(np.float64) # more float size, more amount
print(arr_float.dtype)
"""
float 64
"""
arr1 = np.array([[1, 3, 5], [4, 3, 6]])
arr2 = np.array([[3, 5, 1], [5, 8, 1]])
arr3 = np.array([[[4, 6, 8]], [[4, 3, 6,]]])
print(arr3.ndim)
"""
3
3차원 배열
"""
print(arr1+arr2)
"""
[[ 4  8  6]
 [ 9 11  7]]
"""
print(np.add(arr1, arr2)) # + 연산 이렇게 해도 됨
print(arr1*arr2)
"""
[[ 3 15  5]
 [20 24  6]]
"""
print(np.multiply(arr1, arr2)) # * 연산 이렇게 해도 됨

# ndarray 배열 슬라이싱
arr = np.array([[3, 5, 1], [3, 5, 6], [7, 1, 2]])
print(arr.ndim)
"""
2차원 배열
"""
arr1 = arr[:2, 1:3]
print(arr1)
"""
[[5 1]
 [5 6]]
"""
print(arr[0, 2])
"""
1
index 0번째인 [3, 5, 1] 에서 2번은 "1 
"""
print(arr[[0, 1, 2], [2, 2, 2]])
"""
[1 6 2]
index 각각 0, 1, 2 중에서 세번째 값 가져오기
"""
idx = arr > 3
print(idx)
"""
[[False  True False]
 [False  True  True]
 [ True False False]]

 [[3, 5, 1], 
 [3, 5, 6], 
 [7, 1, 2]] 에서 3보다 크면 True, 작으면 False
"""
print(arr[idx])
"""
[5 5 6 7]
"""
redwine_data = np.loadtxt(fname='winequality-red.csv', delimiter=';', skiprows=1)
# 첫 줄 건너뛰고, 구별자는 ;로
print(redwine_data)
"""
[[ 7.4    0.7    0.    ...  0.56   9.4    5.   ]
 [ 7.8    0.88   0.    ...  0.68   9.8    5.   ]
 [ 7.8    0.76   0.04  ...  0.65   9.8    5.   ]
 ...
 [ 6.3    0.51   0.13  ...  0.75  11.     6.   ]
 [ 5.9    0.645  0.12  ...  0.71  10.2    5.   ]
 [ 6.     0.31   0.47  ...  0.66  11.     6.   ]]
"""
print(redwine_data.sum(axis=0)) # 각각 12개 columns의 합계가 나온다.
"""
[13303.1       843.985     433.29     4059.55      139.859   25384.
 74302.       1593.79794  5294.47     1052.38    16666.35     9012.     ]
"""
print(redwine_data.mean(axis=0)) # 각각 12개 columns의 평균이 나온다.
"""
[13303.1       843.985     433.29     4059.55      139.859   25384.
 74302.       1593.79794  5294.47     1052.38    16666.35     9012.     ]
[ 8.31963727  0.52782051  0.27097561  2.5388055   0.08746654 15.87492183
 46.46779237  0.99674668  3.3111132   0.65814884 10.42298311  5.63602251]
"""
test = redwine_data[:, 0] # 전체 데이터의 0(첫번째) columns를 슬라이싱 fixed acid column이 나온다.

print(test)
"""
[7.4 7.8 7.8 ... 6.3 5.9 6. ]
"""
print(test.mean())
"""
8.31963727329581
"""
print(redwine_data.max(axis=0))
"""
[ 15.9       1.58      1.       15.5       0.611    72.      289.
   1.00369   4.01      2.       14.9       8.     ]
"""
print(redwine_data.min(axis=0))
"""
[4.6     0.12    0.      0.9     0.012   1.      6.      0.99007 2.74
 0.33    8.4     3.     ]
"""
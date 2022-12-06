import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

x = np.array(3)
print(x)
print(x.shape)
print(np.ndim(x))

#벡터 (1차원 텐서)
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = a + b

print(c)
print(c.shape)
print(np.ndim(c))

c = a * b
print(c)
print(c.shape)
print(np.ndim(c))

#스칼라와 벡터의 곱 #일괄적용에 쓰인다
a = np.array(10) #스칼라
b = np.array([1,2,3]) #1차원 텐서
c = a * b

print(c)

#전치행렬
#이차원 텐서

A = np.array([[1,3,4], [4,5,6]])
print('A\n', A)
print('A.shape\n', A.shape)
print('--------------------')

#전치행렬
A_ = A.T
print('A_\n', A_)
print('A_.shape\n', A_.shape)
print('--------------------')

#순서대로 --> (학습용 데이터, 라벨),(테스트용 데이터, 라벨)
from keras.datasets import mnist
(train_images,train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim)

print(train_images.shape)

print(train_images.dtype)

#제일 첫 번째 장 가져오기 #color map
train_images[0]
temp_image = train_images[0]
plt.imshow(temp_image,cmap='gray')

train_labels[0]

train_labels[3]


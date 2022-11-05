import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
import os
from os.path import join

abalone_path = join('.', 'abalone.txt') #.은 현재경로 ..는 상위 경로
column_path = join('.', 'abalone_attributes.txt')

print(abalone_path)  #암수 정보 데이터. 어떤 조건이면 암컷이 되고, 수컷이 되는지 M, F, I(미정)

abalone_columns = list()
for line in open(column_path):
  abalone_columns.append(line)

print(abalone_columns)

#불필요한 요소들 잘라내기
abalone_columns = list()
for line in open(column_path):
  abalone_columns.append(line.strip()) #abalone_columns에 저장하기

print(abalone_columns)

pd.read_csv(abalone_path, header = None, names = abalone_columns)

#data 변수에 저장
data = pd.read_csv(abalone_path, header = None, names = abalone_columns)

print(data)

label = data['Sex']
del data['Sex']

data.describe()

data.info()

#Scaling하기

#data = (data - np.min(data)) / (np.max(data) - np.min(data))
#print(data)

#위와 같이 코딩하지 않아도 MinMaxScaler를 사용하면 처리된다

from sklearn.preprocessing import MinMaxScaler
mMscaler = MinMaxScaler()
#fit()
#mMscaler.fit(data)
#transfrom()
#mScaled_data = mMscaler.transform(data)
mScaled_data = mMscaler.fit_transform(data)
mScaled_data

#numpy 배열을 pandas에 있는 data frame 객체로 바꿔주기(보기 좋게)

mScaled_data = pd.DataFrame(mScaled_data, columns = data.columns)
mScaled_data

from sklearn.preprocessing import StandardScaler
sdscaler = StandardScaler()

sdscaled_data = sdscaler.fit_transform(data)

#NumPy배열로 되어 있는 data를 Pandas로 바꾸기
sdscaled_data = pd.DataFrame(sdscaled_data, columns=data.columns)
print(sdscaled_data)

# Samlping

from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

ros = RandomOverSampler()
rus = RandomUnderSampler()

#resampling

oversampled_data, oversampled_label = ros.fit_resample(data, label)
undersampled_data, undersampled_label = rus.fit_resample(data, label)

oversampled_data = pd.DataFrame(oversampled_data, columns=data.columns)
undersampled_data = pd.DataFrame(undersampled_data, columns=data.columns)

print('원본 데이터의 클래스 비율: \n{}'.format(pd.get_dummies(label).sum()))
print('Oversample 데이터의 클래스 비율: \n{}'.format(pd.get_dummies(oversampled_label).sum()))
print('Undersample 데이터의 클래스 비율: \n{}'.format(pd.get_dummies(undersampled_label).sum()))

#n_informative 튀는 data

from sklearn.datasets import make_classification
data, label = make_classification(n_samples=1000,
                    n_features=2,
                    n_redundant=0,
                    n_informative=2,
                    n_repeated=0,
                    n_classes=3,
                    n_clusters_per_class=1,
                    weights=[0.05,0.15,0.8],
                    class_sep=0.8,
                    random_state=2019)

#나오는 결과값 첫번째: 데이터, 두 번째: 라벨

plt.Figure(figsize=(12, 6))
plt.scatter(data[:,0],data[:,1],c=label,alpha=0.3) #alpha 투명도

from imblearn.over_sampling import SMOTE
smote = SMOTE()

smoted_data, smoted_label = smote.fit_resample(data, label)

print('원본 데이터의 클래스 비율 \n{}'.format(pd.get_dummies(label).sum()))
print('\nSOMTE 결과 \n{}'.format(pd.get_dummies(smoted_label).sum()))

fig = plt.Figure(figsize=(12,6))
plt.scatter(smoted_data[:,0],smoted_data[:,1],c=smoted_label,alpha=0.3)

# 차원의 축소

from sklearn.datasets import load_digits
digits = load_digits()

print(digits.DESCR)

data = digits.data
label = digits.target

data.shape

label.shape

data[0].reshape(8,8)

label[0]

plt.imshow(data[0].reshape((8,8)))
print('Label: {}'.format(label[0]))

from sklearn.decomposition import PCA #주성분분석
pca = PCA(n_components=2)

new_data = pca.fit_transform(data)

print('원본 데이터의 차원 \n{}'.format(data.shape))
print('PCA를 거친 데이터의 차원 \n{}'.format(new_data.shape))

new_data[0] #data[0]을 2개의 차원으로 압축한 것

data[0] #64차원

plt.scatter(new_data[:, 0], new_data[:, 1], c=label, alpha=0.4)
plt.legend()

data = pd.read_csv(abalone_path, header=None, names=abalone_columns)

label = data['Sex']

from sklearn.preprocessing import LabelEncoder
le =LabelEncoder()

type(label)

print(label)

#위의 MFI 자료를 숫자로 바꿔주기
label_encoded_label = le.fit_transform(label)
label_encoded_label

#One Hot Encoding #(sparse=False) 넣어야 배열 형태의 결과 나옴. 기본값은 True로 매트릭스 형태

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False) #True

one_hot_encoded = ohe.fit_transform(label.values.reshape((-1,1)))

print(one_hot_encoded)


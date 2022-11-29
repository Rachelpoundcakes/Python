import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
iris = load_iris()

print(iris.DESCR)
#종류에 따라 3개
#Setosa, Iris-Versicolour, Iris-Virginica

data = iris.data
label = iris.target
columns = iris.feature_names

#dataframe 만들기
data = pd.DataFrame(data, columns=columns)
data.head()

data.shape

#데이터의 준비 0.2(20%)는 테스트용 데이터
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    data,
    label,
    test_size=0.2, random_state=2022) 

#Loistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#학습하기
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

#이전엔 R2 결정계수였다면 여기에서는 
from sklearn.metrics import accuracy_score

#테스트용 데이터의 실제값, 예측값
print('로지스틱 회귀, 정확도: {:.2f}'.format(accuracy_score(y_test, y_pred)))

#서포트 벡터
from sklearn.svm import SVC
svc = SVC()

svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print('서포트 벡터 머신, 정확도: {:.2f}'.format(accuracy_score(y_test, y_pred)))

#C의 값(parameter) 줘 보기. 정확도 조절
from sklearn.svm import SVC
svc = SVC(C=100)

svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print('서포트 벡터 머신, 정확도: {:.2f}'.format(accuracy_score(y_test, y_pred)))

# Decision Tree 결정 트리
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=5)

dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
print('결정 트리, 정확도 {:.2f}'.format(accuracy_score(y_test, y_pred)))

# Random Forest 
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=5)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print('랜덤 포레스트, 정확도 {:.2f}'.format(accuracy_score(y_test, y_pred)))


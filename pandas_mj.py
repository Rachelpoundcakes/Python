#pip install pandas
#Python에 pandas가 내장되어 있으므로 설치할 필요 X

from pandas import Series

fruit = Series([2500,3800,1200,600], index=['appple','banana','pear','cherry'])

print(fruit)

# 값과 인덱스를 추출
print(fruit.values)
print(fruit.index)

#Dict 표현
fruitData = {'apple':2500,'banana':3800,'pear':1200,'cherry':600}
fruit = Series(fruitData)

print(type(fruitData))
print(type(fruit))

fruit

# Series 객체의 이름과 컬럼명 설정하기

fruit.name = 'fruitPrice'
fruit.index.name = 'fruitName'

print(fruit)

# DataFrame

fruitData = {'fruitName':['apple','banana','cherry','pear'],
             'fruitPrice':[2500,3800,6000,1200],
             'num':[10,5,3,8]
             }

from pandas import DataFrame
fruitFrame = DataFrame(fruitData)

print(fruitFrame)

# 컬럼 순서 지정하기

fruitFrame = DataFrame(fruitData, columns=['fruitPrice','num','fruitName'])
print(fruitFrame)

# 특정 항목 추출하기
fruitFrame['fruitName']

fruitFrame.fruitName

# 컬럼 추가하기 
fruitFrame['Year'] = '2022'

print(fruitFrame)

# Series 객체의 추가 
#Nan은 null값. null 값은 나중에 따로 처리를 다 해야 오류가 발생하지 않는다.

variable = Series([4,2,1], index=[0,2,3])

fruitFrame['Stock'] = variable

print(fruitFrame)

# 자료 구조 다뤄보기 
# 데이터 구조의 항목을 삭제 

print(fruit)

newFruit = fruit.drop('banana')

print(newFruit)

#fruit = fruit.drop('banana') 이걸 프린트하면 삭제되기 전 데이터가 나오므로
# newFruit와 같이 다른 변수에 저장해서 출력한다.

print(fruitData)

fruitName = fruitData['fruitName']
print(fruitName)

fruitFrame = DataFrame(fruitData, index=fruitName, columns=['fruitPrice','num'])
print(fruitFrame)

newFruitFrame = fruitFrame.drop(['apple','cherry'])
print(newFruitFrame)

newFruitFrame = fruitFrame.drop(['num'],axis=1)
print(newFruitFrame)

# Pandas Slice 를 사용하는 방법

print(fruit)

fruit[:'pear']

# Series 객체의 기본 연산
fruit1 = Series([5,9,10,3],index=['apple','banana','cherry','pear'])
fruit2 = Series([3,2,9,5,10],index=['apple','orange','banana','cherry','mango'])

newFruit = fruit1 + fruit2
print(newFruit)

# DataFrame 객체의 기본 연산
fruitData1 = {'Ohio':[4,8,3,5],'Texas':[0,1,2,3]}
fruitData2 = {'Ohio':[3,0,2,1,7],'Colorado':[5,4,3,6,0]}
fruitFrame1 = DataFrame(fruitData1, columns=['Ohio','Texas'], 
              index=['apple','banana','cherry','pear'])
fruitFrame2 = DataFrame(fruitData2, columns=['Ohio','Colorado'],
              index=['apple','orange','banana','cherry','mango'])

print(fruitFrame1)

print(fruitFrame2)

newFruitFrame = fruitFrame1 + fruitFrame2
print(newFruitFrame)

# 데이터의 정렬
# Series의 정렬
print(fruit)

fruit.sort_values() #fruit.sort_values(ascending=True)

fruit.sort_values(ascending=False)

fruitName = fruitData['fruitName']

fruitFrame = DataFrame(fruitData, index=fruitName, columns=['num','fruitPrice'])
print(fruitFrame)

fruitFrame.sort_index(ascending=False)

fruitFrame.sort_index(axis=1)

fruitFrame.sort_values(by=['fruitPrice','num'])

# Pandas를 이용한 기초 분석

import pandas as pd

german = pd.read_csv('http://freakonometrics.free.fr/german_credit.csv')

type(german)

print(german.columns.values)

german_sample = german[['Creditability','Duration of Credit (month)','Purpose','Credit Amount']]

print(german_sample)

german_sample.min()

german_sample.max()

german_sample.mean()

german_sample.head()

german_sample.corr()

# Group By 를 이용한 계산 및 요약 통계

german_sample = german[['Credit Amount','Type of apartment']]
print(german_sample)

german_grouped = german_sample['Credit Amount'].groupby(german_sample['Type of apartment'])

german_grouped.mean()

german_grouped.max()

german_sample = german[['Type of apartment','Sex & Marital Status','Credit Amount']]

for type, group in german_sample.groupby('Type of apartment'):
  print(type)
  print(group.head())

for (type, sex), group in german_sample.groupby(['Type of apartment','Sex & Marital Status']):
  print(type, sex)
  print(group.head(n=3))

#행성 데이터 가져오기
import seaborn as sns
planets = sns.load_dataset('planets')

planets.shape #shape 데이터의 모양을 볼 때 사용

planets.head(n=5)

planets.head #NaN값 처리해 주어야 함. 나중에 문제 발생함

planets.dropna() 
#null 값 삭제한 결과: 498행 나옴. 데이터의 양이 많으면 drop시키면 되지만 데이터의 양이 적으면 null 값을 살리는 게 낫다.
#null 값을 살리려면 평균값을 넣어서 데이터를 보존하는 방법이 있다.

pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv') #pandas 이용해서 csv 불러오기

births = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')

births.shape

births.head

births['decade'] = births['year'] // 10 * 10 #연대로 나타내기

births.head()

births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')

import matplotlib.pyplot as plt

births.pivot_table('births',index='decade',columns='gender',aggfunc='sum')

import matplotlib.pyplot as plt

births.pivot_table('births',index='decade',columns='gender',aggfunc='sum').plot()

births.pivot_table('births',index='year',columns='gender',aggfunc='sum').plot()


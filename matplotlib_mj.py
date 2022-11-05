import matplotlib.pyplot as plt #pip 안 해도 파이썬에 이미 설치되어있음 #matplotlib 데이터 시각화를 위한 도구

# Style 적용하기 #matplotlib 스타일 검색해서 원하는 것으로 넣으면 됨
plt.style.use('classic')

import numpy as np

# Sample Data 생성하기 #0에서 10까지 100개의 데이터를 만들어라 #x값 완성
x = np.linspace(0, 10, 100)
x

#y값 완성
plt.plot(x, np.sin(x)) #sin은 y축의 값을 만들어 낸다.

plt.plot(x,np.cos(x))

plt.plot(x, np.sin(x))
plt.plot(x,np.cos(x))

#fugure =그림판
plt.figure
plt.plot(x, np.sin(x), '-') #solid line
plt.plot(x, np.cos(x), '--') #dash
#그림 save
fig = plt.figure()
fig.savefig('my_figure.png')

fig.canvas.get_supported_filetypes()

#svg 깨지지 않는 포맷!! 벡터로 되어 있음

plt.subplot(2, 1, 1) #2행 1열
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

#??
plt.subplot(2, 2, 1) #column 두 개
plt.plot(x, np.sin(x))
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x))
plt.subplot(2, 2, 4)
plt.plot(x, np.cos(x))

plt.style.use('seaborn-whitegrid')

fig = plt.figure() #그림판 만들기
ax = plt.axes() #미리 축을 설정해 보자

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))

plt.plot(x, np.sin(x-0), color='blue')  #색상의 이름으로 지정
plt.plot(x, np.sin(x-1), color='G')  #짧은 색상코드 g 그린의 약자, K 블랙, RGB, CMYK
plt.plot(x, np.sin(x-2), color='K') 
plt.plot(x, np.sin(x-3), color='0.75') #0과 1 사이의 회색조를 표현한다. 0은 빛이 없는 상태 = 블랙
plt.plot(x, np.sin(x-4), color='#ffdd44') #16진수로 표현한 색: R-은 FF G-는 DD B-는 44
plt.plot(x, np.sin(x-5), color=(1.0, 0.2, 0.3)) #RGB 값을 튜플로 표현
plt.plot(x, np.sin(x-5), color='chartreuse')

plt.plot(x, x+0, linestyle='solid') 
plt.plot(x, x+1, linestyle='dashed')
plt.plot(x, x+2, linestyle='dashdot')
plt.plot(x, x+3, linestyle='dotted')

plt.plot(x, x+4, linestyle='-') #solid
plt.plot(x, x+5, linestyle='--') #dashed
plt.plot(x, x+6, linestyle='-.') #dashdot
plt.plot(x, x+7, linestyle=':') #dotted

plt.plot(x, x+0,'-g' ) #선스타일과 색상 한번에 지정
plt.plot(x, x+1,'--c' ) #cyan
plt.plot(x, x+2,'-.k' )
plt.plot(x, x+3,':k' )

plt.plot(x, np.sin(x)) # x limit와 y limit를 설정할 수 있다.

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

plt.plot(x, np.sin(x)) # x limit와 y limit를 설정할 수 있다. 뒤집어서

plt.xlim(10, 0)
plt.ylim(-1.5, 1.5)

plt.plot(x, np.sin(x))
plt.axis([-1, 11,-1.5, 1.5]) #앞의 두 자리가 x축, 뒤의 두 자리가 y축

plt.plot(x, np.sin(x))
plt.axis('tight') #그래프가 꽉 차게

plt.plot(x, np.sin(x))
plt.axis('equal') # 진위를 파악하고 싶을 때

#플롯에 레이블 붙이기
plt.plot(x, np.sin(x))
plt.title('A Sine Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.plot(x, np.sin(x), '-g', label='sin(x)') # 선의 이름만 라벨링. 그래프에 표시X.
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.legend() #그래프에 라벨 표시됨

# 산점도의 출력

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black') #'o' 자리를 마커라고 한다. 표현하는 방식이 달라진다.

rng = np.random.RandomState(0)
for marker in ['o',  ',', 'x', '+', 'v', '<' , '>', 's', 'd']:
  plt.plot(rng.rand(5), rng.rand(5), marker, label='marker={0}'.format(marker))
  
# 아래 화살표
#왼쪽 삼각형
#오른쪽 삼각형
#사각형
#다이아몬드

plt.legend()
plt.xlim(0, 1.8)

plt.plot(x, y, '-ok')

plt.plot(x, y, '-p', color='gray', markersize=15, linewidth=4) #p 오각형 pentagon

plt.plot(x, y, '-p', color='gray', markersize=15, linewidth=4, markerfacecolor='white') #markerface 색을 바꿔보자

plt.plot(x, y, '-p', color='gray', markersize=15, linewidth=4, markerfacecolor='white',
         markeredgecolor="yellow", markeredgewidth='2')

plt.scatter(x, y, marker='o', s=50)

rng = np.random.RandomState(0)

x = rng.randn(100)
y = rng.randn(100)
color = rng.randn(100)
size = 1000 *rng.randn(100)

plt.scatter(x, y, s=size, c=color, alpha=0.3,cmap='viridis') #alpha값 지정=투명도 #C맵을 지정하여 칼라값 주기(여러 가지 있음)
plt.colorbar() #범주

from sklearn.datasets import load_iris #sckit-learn(싸이킷 런) #datasets에 유명한 샘플 데이터들이 들어 있음
iris = load_iris()

type(iris)

iris.data #data 확인

iris.target

features = iris.data.T
iris

plt.scatter(features[0], features[1], s=100*features[3], c=iris.target, alpha=0.3, cmap='viridis')
plt.xlabel(iris.feature_names[0])  #타이틀 잡아주기
plt.ylabel(iris.feature_names[1])

#오차 시각화
x = np.linspace(0, 10, 50) #0부터 10까지 50개 만들기
dy = 0.8
y = np.sin(x) +dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt ='.k') #yerr 오차 범위 나타내기

plt.errorbar(x, y, yerr=dy, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0) #fmt 포맷 #캡사이즈 0으로 설정하면 위 아래 - 뚜껑 없어짐


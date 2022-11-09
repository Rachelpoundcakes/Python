# AND 게이트 #가중치 만들기
import numpy as np
import matplotlib.pyplot as plt

def AND(a, b):
  input = np.array([a,b])

  #가중치 설정
  weights = np.array([0.4,0.4])
  bias = -0.6

  #출력값
  value = np.sum(input * weights) + bias


#---> 이렇게 하면 뉴럴 한 개의 프로그램을 짠 것!!

  #반환값
  if value <= 0:
    return 0
  else:
    return 1

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

x1 = np.arange(-2,2, 0.01)
x2 = np.arange(-2,2, 0.01)
bias = -0.6

y = (-0.4 * x1 - bias) / 0.4

plt.plot(x1, y, 'r--')
plt.scatter(0,0, color='orange', marker='o', s=150)
plt.scatter(0,1, color='orange', marker='o', s=150)
plt.scatter(1,0, color='orange', marker='o', s=150)
plt.scatter(1,1, color='orange', marker='^', s=150)

# 선 안쪽은 모두 0, 바깥쪽은 1

x1 = np.arange(-2,2, 0.01)
x2 = np.arange(-2,2, 0.01)
bias = -0.6

y = (-0.4 * x1 - bias) / 0.4

plt.plot(x1, y, 'r--')
plt.scatter(0,0, color='orange', marker='o', s=150)
plt.scatter(0,1, color='orange', marker='o', s=150)
plt.scatter(1,0, color='orange', marker='o', s=150)
plt.scatter(1,1, color='orange', marker='^', s=150)


plt.xlim(-0.5,1.5)
plt.ylim(-0.5,1.5)
plt.grid()

# OR 게이트 #가중치 만들기

def OR(a, b):
  input = np.array([a,b])

  #가중치 설정
  weights = np.array([0.4,0.4])
  bias = -0.3

  #출력값
  value = np.sum(input * weights) + bias


#---> 이렇게 하면 뉴럴 한 개의 프로그램을 짠 것!!

  #반환값
  if value <= 0:
    return 0
  else:
    return 1

print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

# NAND 게이트 #가중치 만들기

def NAND(a, b):
  input = np.array([a,b])

  #가중치 설정
  weights = np.array([-0.6,-0.6])
  bias = 0.7

  #출력값
  value = np.sum(input * weights) + bias


#---> 이렇게 하면 뉴럴 한 개의 프로그램을 짠 것!!

  #반환값
  if value <= 0:
    return 0
  else:
    return 1

print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))

def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)

  return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))

#Activation Function

#Steop Function (계단 함수)
def step_function(x):
  if x > 0:
    return 1
  else:
    return 0

print(step_function(-3))
print(step_function(5))

# 시그모이드 함수 

def sigmoid(x):
  value = 1 / (1 + np.exp(-x))
  return value

print(sigmoid(3))
print(sigmoid(-3))

plt.grid()
x = np.arange(-5,5,0.01)
y1 = sigmoid(x)
y2 = step_function(x)

plt.plot(x, y1,'r-')
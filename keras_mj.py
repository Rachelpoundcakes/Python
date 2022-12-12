from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.shape

len(train_labels)

test_images.shape

from keras import models
from keras import layers

#sequential 순차적으로 신경망을 만든다는 뜻
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))
#출력값은 0~9중 하나

#여기까자 신경망 추가! 아직 완성은 X

#optimizer 최적화 방법에 따라 접근 방법이 달라진다. 뭘 써야 할지 모를 땐 rmsprop를 쓰자
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# 데이터 타입의 변환 28*28=784
train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32')
print(train_images[0])

#/255
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
test_image = test_images.astype('float32')/255

print(train_images[0])
#0부터 9까지의 categorical 데이터이다. (숫자나 문자 X)

#분류형 데이터의 설정
from tensorflow.keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
#데이터 준비 완료 이제 훈련을 시켜보자

network.fit(train_images, train_labels, epochs=5, batch_size=128)
#loss는 오차. 오차는 점점 줄어든다. 과대적합을 막으려면 어느 시점에서 멈춰야 한다.

#평가 결과 보기
test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc: ', test_acc)


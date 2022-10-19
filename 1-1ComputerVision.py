# Azure Computer Vision - 이미지 분석
# Computer Vision API를 사용해서 이미지 속에 있는 사물을 인식하는 데모이다.
# Azure와의 *네트워크 통신*을 위해서 requests 패키지를 import 합니다.

import requests
# 이미지처리를 위해서 'matplotlib.pyplot', 'Image', 'BytesIO' 세 개의 패키지를 import 해야 한다.
# matplotlib.pyplot는 import 할 때 시간이 조금 걸릴 수 있다.

# as plt == matplotlib을 plt로 줄여 부르겠다는 의미
# matplotlib -->AI에서 필수적
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# json: 인터넷에서 자료를 주고받을 때 그 자료를 표현하는 양식
import json

# Subscription Key와 접속에 필요한 URL 설정
# Azure portal에서 복붙
subscription_key = ''
vision_base_url = 'vision/v2.0/'
# vision_base_url 주소 맨 끝에 vision/v2.0/ 추가
# 컴퓨터비전 기술의 버전 2.0을 사용할 것임을 명시하는 것

# 이미지 분석을 위한 주소. url + 'analyze'
analyze_url = vision_base_url + 'analyze'

# 분석에 사용되는 이미지를 확인한다.
image_url = 'https://nimage.g-enews.com/phpwas/restmb_allidxmake.php?idx=5&simg=20210507230459055709ecba8d8b8617764132.jpg'

con = requests.get(image_url).content
byte = BytesIO(con) #가져온 이미지를 바이트 단위로 풀어준다
image = Image.open(byte)

# 다음과 같이 간편하게 한 줄로 쓸 수 있다.
# image = Image.open(BytesIO(requests.get(image_url).content))

# 이미지 확인
print(image)

# 헤더 정보 셋팅, 옵션 잡아주기(parameter)- MS visualFeatures 문서 보고 지정하기.
headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories, Description, Color'}
data = {'url': image_url} #분석할 주소

 # 웹에서 호줄하는 방법 get or post
 # analyze_url 주소 셋팅, 헤더 정보, parameter, 데이터

response = requests.post(analyze_url, headers = headers, params = params, json = data)

# result는 json의 형태로 가져올 것이다
result = response.json()

# Json 포맷으로 결과 출력됨
print(result)

# Json으로 나온 결과를 뽑아내기
# [0]은 cations의 0번째 값 [text]
image_caption = result['description']['captions'][0]['text']
print(image_caption)
# Computer Vision Object Dectection
# Computer Vision API를 사용해서 이미지속에 있는 사물을 인식하는 데모 입니다.
# 네트워크 통신을 위해서 requests 패키지를 import 합니다.

import requests
# 이미지처리를 위해서 matplotlib.pyplot, Image, BytesIO 세 개의 패키지를 import 합니다.
# matplotlib.pyplot는 import 할 때 시간이 조금 걸릴 수 있습니다.

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

import json

# Subscription Key와 접속에 필요한 URL을 설정합니다.
subscription_key = ''
vision_base_url = 'vision/v2.0/'
# vision_base_url 주소 맨 끝에 vision/v2.0/ 추가

analyze_url = vision_base_url + 'analyze'
# 분석에 사용되는 이미지를 확인합니다.
image_url = 'https://nimage.g-enews.com/phpwas/restmb_allidxmake.php?idx=5&simg=20210507230459055709ecba8d8b8617764132.jpg'

con = requests.get(image_url).content
byte = BytesIO(con)
image = Image.open(byte)

# image = Image.open(BytesIO(requests.get(image_url).content))
image

headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}

response = requests.post(analyze_url, headers = headers, params = params, json = data) #get or post
result = response.json()
result

image_caption = result['description']['captions'][0]['text']
image_caption
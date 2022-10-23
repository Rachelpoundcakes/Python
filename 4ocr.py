import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

subscription_key = ''
vision_base_url = '/vision/v2.0/'
ocr_url = vision_base_url + 'ocr'

image_url = 'https://i.stack.imgur.com/WiDpa.jpg'

image = Image.open(BytesIO(requests.get(image_url).content))
print(image)

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'} #unknown 언어 자동 인식/detectOrientation 가로 세로 자동 인식
data = {'url': image_url}

response = requests.post(ocr_url, headers=headers, params=params, json=data)

result = response.json() #결과 받기
print(result)

for region in result['regions']: #region이란? 그림, 글 각각의 섹션 부분. for문을 써서 원하는 값만 추려내기
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])

image_url = "https://www.unikorea.go.kr/unikorea/common/images/content/peace.png"
image = Image.open(BytesIO(requests.get(image_url).content))
print(image)

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'ko', 'detectOrientation': 'true'}
data = {'url': image_url}

#지원하는 언어목록

#unk (AutoDetect)
#zh-Hans (ChineseSimplified)
#zh-Hant (ChineseTraditional)
#cs (Czech)
#da (Danish)
#nl (Dutch)
#en (English)
#fi (Finnish)
#fr (French)
#de (German)
#el (Greek)
#hu (Hungarian)
#it (Italian)
#ja (Japanese)
#ko (Korean)
#nb (Norwegian)
#pl (Polish)
#pt (Portuguese,
#ru (Russian)
#es (Spanish)
#sv (Swedish)
#tr (Turkish)
#ar (Arabic)
#ro (Romanian)
#sr-Cyrl (SerbianCyrillic)
#sr-Latn (SerbianLatin)
#sk (Slovak)

response = requests.post(ocr_url, headers=headers, params=params, json=data)
result = response.json()
print(result)

for region in result['regions']:
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])

#평화와
#번영의
#한반도      

#에러 시 import json 해주기

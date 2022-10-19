#통신화 #Pillow(PIL):이미지 처리 #BytesIO:바이트 배열을 이진 파일로 다룰 수 있게 해주는 클래스
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

subscription_key = '2b7132593e37491e8597235dbee959fe'
face_api_url = 'https://labuser79face.cognitiveservices.azure.com/face/v1.0/detect'


#Class, library, Package 대문자 관례
#지역변수, 파라메타 소문자로 관례
#addr, msg 줄임말은 배제
#두 단어가 합쳐지면 두 번째 단어는 대문자
#상수는 전체가 대문자  const MAX_USER=100

image_url = 'http://image.koreatimes.com/article/2021/05/10/20210510094734601.jpg'
image = Image.open(BytesIO(requests.get(image_url).content))
print(image)

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'Smile'
}

data = {'url': image_url}

response = requests.post(face_api_url, params=params, headers=headers,json=data)
faces = response.json()
print(faces)
# 결과 ex [{'faceRectangle': {'top': 203, 'left': 116, 'width': 63, 'height': 63}, 'faceAttributes': {'smile': 0.994}},
#'faceAttributes': {'smile': 0.275}}]

draw = ImageDraw.Draw(image)

def DrawBox(faces):

  for face in faces:
    rect = face['faceRectangle']
    left = rect['left']
    top = rect['top']
    width = rect['width']
    height = rect['height']

# draw.rectangle(((left, top)첫 번째 꼭지점,(left+width, top+heit)두 번째 꼭지점
    draw.rectangle(((left,top),(left+width,top+height)),outline='red')

    face_attributes = face['faceAttributes']
    smile = face_attributes['smile']
    #위의 face와 smile 값 가져오기 위해 아래  draw.text 사용
    draw.text((left, top), str(smile), fill='red')
#숫자값으로 되어 있음 -> str 문자로 바꿔주기

DrawBox(faces)
print(image)
# 얼굴에 rectangle 생김
# Azure Computer Vision - Object Dectection

subscription_key = ''
vision_base_url = 'vision/v2.0/'
# vision_base_url 주소 맨 끝에 vision/v2.0/ 추가
# -->>컴퓨터비전 기술의 버전 2.0을 사용할 것임을 명시하는 것

# 컴퓨터비전 호출 주소 = vision base_url에 + detect 활성화
objectDetection_url = vision_base_url + 'detect'
image_url = 'https://previews.123rf.com/images/paylessimages/paylessimages1502/paylessimages150263433/49371391-%EA%B3%A0%EC%96%91%EC%9D%B4%EC%99%80-%ED%96%84%EC%8A%A4%ED%84%B0.jpg'

# 이미지 불러오기(한줄로 간단하게 씀)
image = Image.open(BytesIO(requests.get(image_url).content))

image

# 헤더 정보 셋팅, 옵션 잡아주기(parameter)- MS visualFeatures 문서 보고 지정하기.
headers = {'Ocp-Apim-Subscription-key': subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url} #분석할 주소

response = requests.post(objectDetection_url, headers = headers, params = params, json = data)

# result는 json의 형태로 가져올 것이다
result = response.json()
result

# 다음과 같은 형태로 출력됨
# ---> {'objects': [{'rectangle': {'x': 211, 'y':35, 'w':349, 'h':407...}] }

# PIL = matplotlib.pyplot
from PIL import Image, ImageDraw, ImageFont

#그림 그리기 위한 draw 
draw = ImageDraw.Draw(image)

# boundingBox를 위한 함수
def DrawBox(detectData):
  objects = detectData['objects'] #29행 결과에서 'object' 불러오기

#요소 수만큼 반복
  for obj in objects:
    #print(obj) 잘 나오는지 확인

    rect = obj['rectangle']
    print(rect)

    ImageDraw(result) #입력하면 다음과 같은 형태로 출력 {'x': 211, 'y':35, 'w':...}

    x = rect['x']
    y = rect['y']
    w = rect['w']
    h = rect['h']

#사각형을 그리겠다
    draw.rectangle(((x, y), (x+w, y+h)), outline='red')

#object에 있는 것을 뽑아내겠다
    objectName = obj['object']
    draw.text((x,y), objectName, fill='red')

    DrawBox(result)
    # 결과 ex {'x': 211, 'y': 35, 'w': 349, 'h': 407}

    image
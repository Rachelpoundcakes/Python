# Custom Vision
# pip install azure-cognitiveservices-vision-customvision

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Azure custom vision에서 다음 값 가져오기
ENDPOINT = ''

training_key = ''
prediction_key = ''
prediction_resource_id = ''

# 학습 반복 이름 정하기
publish_iteration_name = "classifyModel"

# credential를 사용하여 암호화
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})

# 트레이닝 시키기
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

print ("Creating project...")
project = trainer.create_project("Mj New Project")

Jajangmyeon_tag = trainer.create_tag(project.id, "Jajangmyeon")
Champon_tag = trainer.create_tag(project.id, "Champon")
Tangsuyug_tag = trainer.create_tag(project.id, "Tangsuyug")

import time

print('Training....')
#iteration이 실행되면 트레이닝이 시작된다.
iteration = trainer.train_project(project.id)
while (iteration.status != 'Completed'):
  iteration = trainer.get_iteration(project.id, iteration.id)
  print('Training status' + iteration.status)

  time.sleep(2)

print('Done!')


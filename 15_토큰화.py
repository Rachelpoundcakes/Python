# 텍스트 토큰화

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


#install nltk

# 구두점 데이터 다운로드
nltk.download('punkt')

string_temp = "Artificial Intelligence is the present and uncoming future"
token_temp = word_tokenize(string_temp)
print(token_temp)

string_temp01 = "Artificial Intelligence is the present. It is uncoming future"
sent_data = sent_tokenize(string_temp01) # 문장으로 나누기
print(sent_data)

"""
결과
['Artificial', 'Intelligence', 'is', 'the', 'present', 'and', 'uncoming', 'future']
['Artificial Intelligence is the present.', 'It is uncoming future']
"""


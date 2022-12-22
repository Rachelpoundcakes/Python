# 단어 중요도에 가중치 부여하기
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

text_data = np.array(
    ['I love Korea. Korea!!', 'Sonny is the best player in the world', 'Go for it!'])

# tf-idf 특성 행렬을 만들기
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)
feature_matrix.toarray()  # tf-idf 특성 행렬을 밀집 배열로 확인
# print(feature_matrix)
# 특성 이름 확인
tf = tfidf.vocabulary_
print("...", tf)

"""
{'love': 7, 'korea': 6, 'sonny': 9, 'is': 4, 'the': 10, 'best': 0, 'player': 8, 'in': 3, 'world': 11, 'go': 2, 'for': 1, 'it': 5}
"""

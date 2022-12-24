# 구두점 삭제
# 구두점을 key로 하고 값은 None인 puctuatuion 딕셔너리 만들기
# punctuation에 있는 모든 문자를 None으로 바꾼다

import unicodedata
import sys
text_data = ["I am Rachel Kim. I, love watching drama...",
            "I lived in Canada in 2012. It was awesome!!",
            "To improve your English skills, you should speak a lot."]
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P'))

# 문자열의 구두점 삭제
test = [string.translate(punctuation) for string in text_data]
print(test)

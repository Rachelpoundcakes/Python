# 텍스트 데이터 처리 01
import re
text_data = ["Sky is blue and clean.",
             "I have such a nice coat.",
             "Everything was perfect."]

# 공백 제거
strip_whitespace = [string.strip() for string in text_data]
print("공백 제거 >> ", strip_whitespace)

# 마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print("마침표 제거 >> ", remove_periods)

# 대문자로 만들기
def capitalizer(string: str) -> str: return string.upper()


temp = [capitalizer(string) for string in remove_periods]
print(temp)

# X로 치환하기
def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-Z]", "X", string)


data = [replace_letters_with_X(string) for string in remove_periods]
print(data)

"""
<결과>
공백 제거 >>  ['Sky is blue and clean.', 'I have such a nice coat.', 'Everything was perfect.']
마침표 제거 >>  ['Sky is blue and clean', 'I have such a nice coat', 'Everything was perfect'] 
['SKY IS BLUE AND CLEAN', 'I HAVE SUCH A NICE COAT', 'EVERYTHING WAS PERFECT']
['XXX XX XXXX XXX XXXXX', 'X XXXX XXXX X XXXX XXXX', 'XXXXXXXXXX XXX XXXXXXX']
"""
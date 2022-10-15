import GTTS
text =  "안녕하세요 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다."

tts = GTTS(text=text, lang='ko')
tts.save(r"hello.mp3")


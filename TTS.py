from gtts import gTTS
text = "안녕하세요, 저는 마이크로소프트 에이아이 스쿨에서 공부하는 교육생입니다."
tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")
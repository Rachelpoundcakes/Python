# while문

americano = 20
price = 4000
while price:
    print("아메리카노 제조중입니다.")
    americano = americano -1
    print("주문 가능한 아메리카노는 %d잔입니다."% americano)
    if americano == 0:
        print("아메리카노가 모두 소진되었습니다.\n다음에 이용해 주세요.\n감사합니다.")
        break

americano = 20
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 4000:
       select = input("HOT/COLD 선택하세요. HOT: 1, COLD:2__")
       if select == "1":
           print("따뜻한 아메리카노를 제조중입니다.")
           americano = americano -1
           print("현재 주문 가능한 아메리카노는 %d잔입니다."%americano)
       elif select == "2":
            print("시원한 아메리카노를 제조중입니다.")
            americano = americano -1
            print("현재 주문 가능한 아메리카노는 %d잔입니다."%americano)
    else:
        print("돈이 모자랍니다.")
        break

        
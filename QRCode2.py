import qrcode

#with 키워드를 사용하여 파일을 열면, 파일을 사용하지 않을 때 자동으로 close()를 호출하여 닫아준다.
with open('site_list.txt', 'rt', encoding='UTF8') as f:
  read_lines = f.readlines()

  for line in read_lines:
    line = line.strip()
    print(line)

    qr_data = line
    qr_image = qrcode.make(qr_data)

    qr_image.save(qr_data + '.png')
    

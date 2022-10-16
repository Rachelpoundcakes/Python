import qrcode

qr_data = 'applepy.tistory.com'
qr_image = qrcode.make(qr_data)

qr_image.save(qr_data + '.png')
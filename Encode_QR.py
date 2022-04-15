import qrcode   # QR code generator module

data = "Scan me"
img = qrcode.make(data)
img.save('C:/Programming/Projects/QR-Code-Encoder-Decoder/myqrcode1.png')
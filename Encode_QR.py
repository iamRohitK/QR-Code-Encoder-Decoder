import qrcode   # QR code generator module

data = "Scan me"
img = qrcode.make(data)
img.save('C:/Programming/Projects/QR Code/myqrcode1.png')
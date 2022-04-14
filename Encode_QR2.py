# Ref: https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/

import qrcode

data = "Scan me"
qr = qrcode.QRCode(version=4, box_size=10, border=4)
qr.add_data(data)    # This method is used to add data to the QRCode object. It takes the data to be encoded as a parameter.

qr.make(fit=True)   # This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.

img = qr.make_image(fill_color='cyan', back_color='white')  # This method is used to convert the QRCode object into an image file. 
                                                            # It takes the fill_color and back_color optional parameters to set the foreground and background color.
img.save('C:/Programming/Projects/QR Code/myqrcode2.png')
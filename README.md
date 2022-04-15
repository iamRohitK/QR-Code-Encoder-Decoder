# Introduction

* This project is about **generating QR Code** and **encoding/decoding** information from the generated QR Code

## Features

* Can **generate QR code image** using [qrcode](https://pypi.org/project/qrcode/) library
* Can change the size of the QR code, box size of boxes, thickness of the border of the box
* Can change the **foreground** and **background color**
* Can **decode the QR Code in image** using `decode` function of [pyzbar](https://pypi.org/project/pyzbar/) module
* Can load images from files using `Image` sub-module of [PIL](https://pypi.org/project/Pillow/) module
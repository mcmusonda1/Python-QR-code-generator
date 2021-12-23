import qrcode

img = qrcode.make(input('Enter your message: \n'))
img.save("single.png")
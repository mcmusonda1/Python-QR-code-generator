import qrcode

img = qrcode.make(input('Enter your message: \n'))
img.save("you.png")
import qrcode

name = input("Enter your name: \n")
Phone = input("Enter your mobile number: \n")
email = input("Enter your email address: \n")


image = qrcode.make('Name: ' + name + ' ' + '\n Phone number: ' + Phone + ' ' + '\n Email: ' + email)
type(image)
image.save("Mutiple.png")
import qrcode

name = input("Enter your name: \n")
Phone = input("Enter your mobile number: \n")
email = input("Enter your email address: \n")
dob = input("Enter your date of birth: \n")
gender = input("Enter your gender: \n")
university = input("Enter the name of your university: \n")
course = input("Enter name of the course your are doing: \n")
year = input("Enter the year of study you are in: \n")


image = qrcode.make('Name: ' + name + ' ' + '\n Phone number: ' + Phone + ' ' + '\n Email: ' + email + ' ' + '\n Date Of Birth: ' + dob + ' ' + '\n Gender: ' + gender + ' ' + '\n University: ' + university + '\n Course: ' + course + ' ' + '\n Year: ' + year)
type(image)
image.save("Mutiple.png")
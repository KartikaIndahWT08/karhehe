# TUGAS ALGORITMA dan PEMOROGRAMAN (19 September 2022)
# KARTIKA INDAH WIDYAS TANTRI / 222410102001

# Buatlah program python untuk menghitung Body Mass Index seseorang dengan menggunakan rumus yang telah dicantumkan

weight = float(input('Input your Weight (kg): '))
height = float(input('Input your Height (cm): '))

# Converse Height (cm) to (m) :
height = height/100

# Formula BMI = weight (kg) / height (m)**2
bmi = weight / (height**2)

print('Your BMI score: ',bmi)

# If else
if bmi <= 18.5:
    print('Your weight status is UNDERWEIGHT')
elif bmi > 18.5 and bmi <= 24.9:
    print('Your weight status is NORMAL WEIGHT')
elif bmi >= 25.0 and bmi <= 29.9:
    print('Your weight status is OVERWEIGHT')
elif bmi >= 30.0 and bmi <= 34.9:
    print('Your weight status is OBESITY Class I')
elif bmi >= 35.0 and bmi <= 39.9:
    print('Your weight status is OBESITY Class II')
elif bmi >= 40 :
    print('Your weight status is OBESITY Class III')
elif bmi >= 50 :
    print('Your weight status is OBESITY Class IV')

# Print name 
a = input('Input your name: ')
b = int(input('Input your birth date: '))

if a == 'Kartika':
    print("Your name is correct")
print("try again")

if b == '8112003':
    print('Succes')
print("Try Again")


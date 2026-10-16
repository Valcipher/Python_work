# check the eligiblity for marr(M/F) on based on their gender and age group

name = input('Enter your name: ')
gender = input('Enter your gender(M/F): ')
age = int(input('Enter your age: '))

if(gender == 'F'):
    if(age>=18):
        print(f'{name} is eligible for marriage')
    else:
        print(f'{name} is not eligible for marriage')
else:
    if(age>=21):
        print(f'{name} is eligible for marriage')
    else:
        print(f'{name} is not eligible for marriage')
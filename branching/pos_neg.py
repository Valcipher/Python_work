num = int(input('Enter a no. : '))

if(num == 0):
    print("It's zero! It is neither positive nor negative")
elif(num < 0):
    print(f'{num} is negative number')
else:
    print(f'{num} is positive number')
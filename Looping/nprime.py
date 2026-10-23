#WAP to print first n prime number

num = int(input('Enter a number: '))
a = int(input('Enter how many prime numbers you want to print: '))
count= 0 
for i in range(2,num):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i, end = " ")
        count += 1

        if(count == a):
            break
1





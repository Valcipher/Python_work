num = int(input('Enter a number: '))

for i in range(2,num+1):
    for a in range(2,i):
        if(i % a ==0):
            break
    else:
        print(i, end = ' ')
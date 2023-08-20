import random
while True:
    print('Operations: 1.Roll the dice 2.exit')
    choice = int(input('Enter the number: '))
    if(choice==1):
        print('The number is: {}'.format(random.randint(1,6)))
    else:
        break   
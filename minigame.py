import random
number = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input('Угадай число:'))
    attempts +=1
    if guess < number:
            print('Маленькое')
    elif guess > number:
            print('Большое')
    else:
            print('Ты угадал!!!')
            print(f'Ты угадал за {attempts} попыток')
            break
    if attempts == 5:
        print("Ты проиграл")
        break

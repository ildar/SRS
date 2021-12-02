#!env python3
import random

def is_valid(s):
    if s.isdigit() and int(s)>=1 and int(s)<=100:
        return int(s)
    else:
        return -1

myno = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')
while True:
    guess = is_valid(input())
    if guess == -1:
        print('А может быть все-таки введем целое число от 1 до 100?')
    elif guess < myno:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif guess > myno:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        break
print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
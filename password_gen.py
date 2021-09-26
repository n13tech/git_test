import random

letters = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
letters += letters.upper()

def pass_gen(n=12):
    return ''.join([random.choice(letters) for i in range(n)])
    
password_length = int(input('Введите количество символов пароля: '))

result = pass_gen(n=password_length)

assert len(result) == password_length, 'С паролем что-то не так'

print(result)

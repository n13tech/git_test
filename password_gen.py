import random

abcd = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
abcd += abcd.upper()

def pass_gen(n=12):
    return ''.join([random.choice(abcd) for i in range(n)])
    
n = int(input('Введите количество символов пароля: '))

res = pass_gen(n=n)

assert len(res) == n, 'С паролем что-то не так'

print(res)

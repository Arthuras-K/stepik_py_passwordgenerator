import random as rnd

digits = '0123456789';
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz';
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
punctuation ='!#$%&*+-=?@_'
chars = ''

def generate_password(qty, ch):
  pas = ''
  for _ in range(qty):
    pas += rnd.choice(ch)
  return pas

print('Генератор паролей приветствует тебя!')
qty_pass = int(input('Сколько паролей тебе сгенирировать: '))
qty_chars = int(input('Сколько символов будет в каждом пароле: '))
dig = input(f'Включать ли в пароль цифры "{digits}"?(y/n): ').lower().strip()
low_let = input(f'Включать ли в пароль строчные буквы "{lowercase_letters}"?(y/n): ').lower().strip()
up_let = input(f'Включать ли в пароль прописные буквы "{uppercase_letters}"?(y/n): ').lower().strip()
pun = input(f'Включать ли в пароль символы "{punctuation}"?(y/n): ').lower().strip() 
unpun = input('Исключить ли неоднозначные символы "il1Lo0O"?(y/n): ').lower().strip()

if dig == 'y':
  chars += digits
if low_let == 'y':
  chars += lowercase_letters
if up_let == 'y':
  chars += uppercase_letters
if pun == 'y':
  chars += punctuation
if unpun == 'y':
  for i in "il1Lo0O":
    chars = chars.replace(i,'')

print(f'\nВ твой пароль могут входить следующие символы: {chars}\n')

for i in range(qty_pass):
  print(f'{i+1}) {generate_password(qty_chars, chars)}')  
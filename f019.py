#IF , ELIF e ELSE

num1 = 2
num2 = 2

expr = (num1 == num2)
print(expr)

comparacao1 = int(2)
comparacao2 = 2

comparacao1 and comparacao2
comparacao1 or comparacao2

if comparacao1 == comparacao2:
    print('Sim')
else:
    print('Nao')

if not comparacao1 == comparacao2:
    print('Sim')
else:
    print('Nao')

nome = 'Miguel'

if 'M' in nome:
    print('Voce tem M em seu nome')



usuario= input('Nome de usuario : ')
senha = input('Senha do usuario : ')  
usbd = 'Miguel'
snbd = '1234'

if usbd == usuario and snbd == senha:
     print('Login Sucess')
else:
     print('Not Login')
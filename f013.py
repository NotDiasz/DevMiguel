#variaveis
#str , bool , int , float , double

idade = 18
emaior = idade >=18

print('type {}'.format(emaior))

idd = input('Qual sua Idade ? ')
Nm = input('Qual seu Nome ? ')
ps = float(input('Qual seu peso ? '))
al = float(input('Qual sua Altura ? '))

imc = ps / (al ** 2)

print('Ola seu nome e : {} , Sua idade e : {} , E seu peso e : {} , e sua altura e : {} , e seu IMC e : {:.2f} '.format(Nm , idd , ps , al , imc))
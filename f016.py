
nome = str(input('Qual e o seu Nome ? '))
idade = int(input('Qual sua Idade ? '))
altura = float(input('Qual a sua altura ? '))
peso = float(input('Qual o seu peso ? '))
ano_atual =  2024

nasc = (ano_atual - idade)
imc = peso / (altura * 2)

print(f'{nome} tem {idade} anos , {altura}m de altura e pesa {peso}kg \n O imc de {nome} e {imc:.2f} \n {nome} nasceu em {nasc} e o ano atual e {ano_atual} ')
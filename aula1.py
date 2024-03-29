
# VERSOS DO SONETO FELICIDADE DE VINICIUS DE MORAES

print('De tudo, ao meu amor serei atento ')
print('Antes, e com tal zelo, e sempre, e tanto')
print('Que mesmo em face do maior encanto')
print('Dele se encante mais meu pensamento.')


# \n quebra de linha # # \t tabulação #
print("saudações jedi\nViemos numa missão de\tpaz")

# inclusão de cores
print("Saudações\033[1;35;40m Jedi\033[0m\nViemos numa missão de\t\033[1;32;40m paz\033[0m")

# Tipos variáveis

ano = 1989
nome = "Luke Skywalker"
saldo = 50.30
print(("O tipo da variável ano é {}".format(type(ano))))
print(("O tipo da variável nome é {}".format(type(nome))))
print(("O tipo da variável saldo é {}".format(type(saldo))))
print(f'O tipo de variável saldo ´é {type(saldo)}')

# ENTRADA DE DADOS

nome = input('nome: ')
sobrenome = input('sobrenome: ')
print(nome, sobrenome)

x = int(input('informe um número: '))
y = float(input('informe outro número: '))
multiplicacao = x * y
divisao = x / y
adicao = x + y
subtracao = x - y

print(multiplicacao, divisao, adicao, subtracao)
print("x * y = {}".format(multiplicacao), '\n\n')
print(f'x / y = {divisao}')
print(f'x + y = {adicao}', '\n\n')
print('o tipo de dados de x + y é, ', type(x + y), '\n\n')


# \n = espaço entre linhas, \t = tab

print('como vai você\n\nComo \tvocê se sente')

print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável 1: ")
B = input("Digite o conteúdo da variável 2: ")
troca = A
A = B
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}".format(A, B))


# PESO BAGAGEM CLIENTE

peso_bagagem = float(input('Peso bagagem: '))
cliente_VIP = input('É cliente VIP? ')

if cliente_VIP == 'sim':
    if peso_bagagem > 32:
        print('peso da bagagem excede 32 kg')
    elif peso_bagagem <= 32:
        print('peso permitido para o limite')
    elif peso_bagagem > 28:
        print('peso da bagagem excede 28 kg')
    else:
        print('peso permitido para o limite')

# CÁLCULO IMC

peso = float(input('Peso: '))
altura = float(input('Altura: '))
IMC = peso / (altura ** 2)

print(f'O IMC é {IMC}')

if IMC > 0:
    if IMC <= 18.5:
        print('magreza')
    elif IMC <= 24.9:
        print('normal')
    elif IMC <= 29.9:
        print('sobrepeso')
    elif IMC <= 39.9:
        print('obesidade')
    elif IMC <= 40:
        print('obesidade grave')
    else:
        print('informação inconsistente')

# DIAS DA SEMANA

print('DIA DA SEMANA')
dia = int(input('Digite o número do dia da semana: '))

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case  6:
        print('Sexta-feira')
    case 7:
        print('Sábado')
    case other:
        print('Dia inválido')
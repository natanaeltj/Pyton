# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print('Hello world') # print == função

print(2+3)

# Operadores e operação matematica (// = Divisão(Somente a parte inteira), (% = Módulo/Resto da divisão),
#(** = Exponenciação ou potenciação).

notaAlun = 7.3 #Nunca inicie o nome de uma variavel com um número!!!!!!!!!!!! só pode ser criado com underline no inicio
if notaAlun <= 7 :
 print('Você esta de recuperação!')
else:
    print('Você passou cachorro aiaiai uiui!')
#tipos primitivos de dados

frase = ('eita disgraceira')
print(frase[3]) #chamando o indice da string

teste = ('a' + ' ' * 20 + 'b' + ' ' * 5 + 'c')
print(teste)

disciplina = 'matematica'
s1 = f'Você tirou {notaAlun} em {disciplina} seu fudido'  #composição com marcadores de posição modernos
print(s1)
print(s1[0:4]) #fatiamento string

nome = input('digite o seu nome?')
print(nome)
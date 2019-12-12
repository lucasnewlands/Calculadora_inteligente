escolha = []
import os

def mostra_linha():
    print("-="*50)

def options_user():
    print('''
    [1]Para calculadora Simples
    [2]Para calculadora Financeira''')
    

'''
funções Calculadora Simples
'''

def options_cs():
    os.system('cls')
    print('\nOBS: Está calculadora só executa operações com dois números\nOBS: A operação de racionalização só é executada com um valor\nOBS: Na operação de potenciação o segundo valor informado será utilizado como expoente da operação')

    numero1 = float(input('\ninsira o primeiro valor: '))
    numero2 = float(input('\ninsira o segundo valor: '))
    print('\npara encerrar o programa, digite 0')
    print('''
    [0]Para encerrar o programa
    [1]Para somar
    [2]para subtrair
    [3]Para Dividir
    [4]Para multiplicar
    [5]para potenciar
    [6]Para racionalizar
    [7]Para retornar ao início''' )
    while True:
            try:
                opções = int(input('\n\nescolha a operação que deseja utilizar: '))
                assert opções in[0, 1, 2, 3, 4, 5, 6, 7]
                break
            except:
                print('insira uma opção válida .')
    while True:
        if opções == 1:
            soma = (numero1 + numero2)
            print(f'\n\nA soma de {numero1} + {numero2} é igual a: {soma}')
            return options_user()
        elif opções == 2:
            subtracao = (numero1 - numero2)
            print(f'\nA subtração de {numero1} - {numero2} é igual a: {subtracao}')
        elif opções == 3:
            divisao = (numero1 / numero2)
            print(f'\nA divisão de {numero1} - {numero2} é igual a: {divisao}')
        elif opções == 4:
            multiplicacao = (numero1 * numero2)
            print(f'\nO produto de {numero1} * {numero2} é igual a: {multiplicacao}')
        elif opções == 5:
            print('para potenciacao o segundo valor servirá como o expoente da operação')
            potenciacao = (numero1 ** numero2)
            (print(f'\nA potência de {numero1} no expoente {numero2} é igual a: {potenciacao}'))
        elif opções == 6:
            racionalização = (numero1 ** (1/2))
            print(f'a raiz quadrara de {numero1} é igual a: {racionalização} ')
        elif opções == 7:
            print('voltando para o menu ')
            return options_user()
            escolha == int(input('escolha uma opção: '))
        elif opções == 0:
            print('programa encerrado') 
            break 
        return options_cs()

def options_calculadora_financeira():
    import os
    print('Escolha uma das opções: \n\n[1]Para Juros Simples\n[2]Para Juros Compostos')
    while True:
        try:
            operações = int(input('\nescolha a operação que deseja utilizar: '))
            assert operações in [1, 2]
            break
        except:
                print ('opção inválida')
                import os
                
    while True:
        import os
        if operações == 1:
            print('insira as informações necessárias para o cálculo: ')
            c = float(input('insira o capital: '))
            i = float(input('insira a taxa de empréstimo: '))
            n = int(input('obs: utilizar o formato de ano = 12 meses para o cálculo \ninsira o tempo de duração: '))
            j= c*i*n
            valor_bruto = (c * n)
            valor_final = (c + j)
            print(f'\nvalor bruto é igual a: {valor_bruto} ')
            print(f'\n\no valor final devido séra igual a: {valor_final} \n\n')
            break
        if operações == 2:
            print('insira as informações necessárias para o cálculo: ')
            capital = float(input('insira o capital inicial: '))
            tempo = int(input('insira o tempo total da aplicação: '))
            i = float(input('insira a taxa de juros aplicada: '))
            i2 = i / 100
            montante = capital*((i2+1)**tempo)
            juros = montante - capital
            valor_bruto = capital * tempo
            print(f'valor: {montante}')
            print(f'valor juros: {juros}')
            break

        

           

            














    
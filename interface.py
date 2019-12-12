import funções
import os
print('\n\nBem Vindo a sua calculadora pessoal   v(0.1)')
funções.options_user()
while True:
        try:
            escolha = int(input('\n\nescolha uma opção: '))
            assert escolha in [1, 2,]
            break
        except:
            print('Escolha uma opção válida')
if escolha == 1:
    funções.options_cs()
if escolha ==2:
    funções.options_calculadora_financeira()


            





    









    

    

        











    

            


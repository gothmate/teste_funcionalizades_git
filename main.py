def bloco(str):
    print('=' * 25)
    print(str)
    print('=' * 25)


while True:
    variavel0 = input('digite um nome: ').strip()

    if variavel0.isalpha():
        variavel1 = input('digite um valor: ')

        if variavel1.isnumeric():
            variavel2 = int(variavel1) + 1
            print(f'''de acordo com os dados passado seu nome é {variavel0.upper()} 
            e  você tem {variavel1} anos, amanhã você terá {variavel2} Happy birthday...''')
            if variavel2 >= 100:
                bloco('yo\'re dead')
                break
            else:
                bloco('você está vivo')

        else:
            bloco('Algum valor está invalido')
    else:
        print('Esse não é um nome válido')

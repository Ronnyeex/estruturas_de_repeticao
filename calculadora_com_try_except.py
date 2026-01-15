while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operado(+-/*): ')

    num1_float = 0
    num2_float = 0

    numeros_validos = None
    operados_permitidos = '+-/*'

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None

        if numeros_validos == None:
            print('Um ou ambos números não são validos.')
            continue

    if operador not in operados_permitidos:
        print('Operador digitado não é permitido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Verifique o resultado abaixo:')

    if  operador == '+':
        print(num1_float + num2_float)
    elif  operador == '-':
        print(num1_float - num2_float)
    elif  operador == '/':
        print(num1_float / num2_float)
    elif  operador == '*':
        print(num1_float * num2_float)
    else:
        print('Algo deu errado.')


    sair = input('Deseja sair? [S]im: ').lower().startswith('s')
    if sair is True:
        break
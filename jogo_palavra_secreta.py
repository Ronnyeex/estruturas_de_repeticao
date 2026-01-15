palavra_secreta = 'laura'
letras_acertadas = ''
numero_tentativas = 0

print(21 * '═')
print(' JOGO DE ADIVINHAÇÃO')
print(21 * '═')
print('\nSeja bem-vindo! Adivinhe a palavra secreta...\n')

while True:
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Adivinhe a palavra:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print(30 * '═')
        print('      🏆 PARABÉNS, VOCÊ GANHOU! 🏆')
        print(30 * '═')
        print(f'\nA palavra secreta era: "{palavra_secreta}"')
        print(f'Você precisou de {numero_tentativas} tentativas para acertar.')
        break

    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) != 1:
        print('\n🚫 ERRO: Por favor, digite apenas UMA letra.\n')
        continue

    numero_tentativas += 1

    if letra_digitada in palavra_secreta:
        if letra_digitada in letras_acertadas:
            print(f'\nVocê já tinha acertado a letra "{letra_digitada}". Tente outra!\n')
        else:
            print(f'\nBoa! A letra "{letra_digitada}" existe na palavra!\n')
            letras_acertadas += letra_digitada
    else:
        print(f'\nQue pena! A letra "{letra_digitada}" NÃO existe na palavra.\n')

print('Obrigado por jogar!')
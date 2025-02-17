import random

#listagem das possiveis palavras, e as letras a serem adicionadas pelo jogador.
lista_palavras = 'Kyan', 'mAjor rd', 'Yunk vino', 'Bk', 'taSha', 'biG rush', 'Aka rasta'
lista_letras_digitadas = []

#Seleção da palavra do jogo atual.
palavra_secreta = random.choice(lista_palavras).lower().replace(' ', '')

print(palavra_secreta)
#Quantidade de erros possíveis.
chances = 3

#Direcionamento ao jogador por meio de frases.
print('bem vindo jogador ao jogo da forca, o tema é Trappers Brasileiros.')
print('a palavra selecionada possui', len(palavra_secreta) * '*', 'letras')

#while para fazer o loop em que o jogador ou acerta a palavra e continua, ou erra e perde o jogo, ambos encerrando o loop.
while True:

    #letra que o jogador escolher.
    letra_escolhida = input('Digite a letra da palavra: ')

    #Lenght(tamanho) da letra escolhida.
    if len(letra_escolhida) > 1:
        print('Você deve por APENAS UMA letra por tentativa!!!')
        continue

    #Se a letra escolhida pertence a palavra secreta(a palavra do jogo atual), Adicione-a a lista de letras digitadas.
    if letra_escolhida in palavra_secreta:
        print('parabéns,vc acertou uma letra')
        lista_letras_digitadas.append(letra_escolhida)

    #Se a letra escolhida não pertencer a palavra, exclua da lista de letras digitadas.
    else:   
        chances -= 1
        if chances <= 0:
            print('vc perdeu o jogo, tente novamente')
            break
        else:
            print(f'vc errou a letra, agora vc tem {chances} chances')
    palavra_secreta_temporaria = ''
    for letra in palavra_secreta:
        if letra in lista_letras_digitadas:
            palavra_secreta_temporaria = palavra_secreta_temporaria + letra
        else:
            palavra_secreta_temporaria += '*'
    if palavra_secreta_temporaria == palavra_secreta:
        print(f'parabéns, vc venceu o jogo, a palavra secreta era {palavra_secreta}!!')
        break
    print(palavra_secreta_temporaria)
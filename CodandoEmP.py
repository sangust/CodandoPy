#caderneta de exercicios em PY
print('A seguir haverá uma sequencia de exercicios, tente resolver-los, deseja prosseguir?')
if input() in ["sim", 's', 'yes']:
    print('O primeiro exercicio é sobre triangulo')
    print('Existe um triangulo retangulo de área 50cm^2, qual poderá ser suas bases e altura?')
    while True:
        B = int(input('qual o valor de B em CMs? '))
        H = int(input('qual o valor de H em CMs? '))
        ATriangulo = int(B * H / 2)

        if ATriangulo == 50:
            print('Correto, a resolução seria a seguinte: {}cm*{}cm / 2cm, = {}cm^2, parabéns!'.format(B, H, ATriangulo))
            break
        else:
            tentar_novamente = input('infelizmente vc errou, deseja tentar novamente? ') 
            if tentar_novamente in ["nao", "não", "n", "no"]:
                print('Ok, outra hora vc volta! ;)')
                break
            else:
                print('Ok, vamos de novo! ;)')   
else:
    print('Ok, Volte e tente fazer os exercicios outra hora!')   
   
   
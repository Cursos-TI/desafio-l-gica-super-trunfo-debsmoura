import random

def escolher_atributo():
    atributos = ["forca", "velocidade", "inteligencia", "resistencia"]
    print("Escolha um atributo:")
    for i, atributo in enumerate(atributos, start=1):
        print(f"{i} - {atributo}")
    escolha = int(input("Digite o número do atributo: "))
    return atributos[escolha - 1]

def comparar_cartas(carta1, carta2, atributo):
    valor1 = carta1.atributos()[atributo]
    valor2 = carta2.atributos()[atributo]

    if valor1 > valor2:
        return 1
    elif valor1 < valor2:
        return -1
    else:
        return 0

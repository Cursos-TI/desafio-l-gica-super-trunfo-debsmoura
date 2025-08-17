from cartas import Carta
from utils import escolher_atributo, comparar_cartas
import random

# Criando cartas de exemplo
cartas = [
    Carta("Dragão", 90, 60, 70, 85),
    Carta("Guerreiro", 75, 80, 60, 70),
    Carta("Mago", 50, 65, 95, 55),
    Carta("Gigante", 85, 40, 50, 95),
    Carta("Elfo", 60, 90, 85, 65),
]

print("=== SUPER TRUNFO ===")
print("Distribuindo cartas...\n")

carta_jogador = random.choice(cartas)
carta_computador = random.choice(cartas)

print(f"Sua carta: {carta_jogador.nome}")
print("Atributos:", carta_jogador.atributos())

atributo_escolhido = escolher_atributo()
resultado = comparar_cartas(carta_jogador, carta_computador, atributo_escolhido)

print(f"\nCarta do Computador: {carta_computador.nome}")
print("Atributos:", carta_computador.atributos())
print(f"Atributo escolhido: {atributo_escolhido}")

if resultado == 1:
    print("\n🎉 Você venceu!")
elif resultado == -1:
    print("\n😢 Você perdeu!")
else:
    print("\n😐 Empate!")

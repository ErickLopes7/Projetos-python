from pickle import TRUE
import random 

numero_secreto = random.randint(1, 10) 

print("=== JOGO DE ADIVINHAR NUMERO ===") 

while TRUE:
    palpite = int(input(" digite um numero entre 1 e 10"))
    if palpite == numero_secreto:
        print("🎉 Parabéns! você acertou!")
        break 

    elif palpite < numero_secreto:
        print("O número secreto é MAIOR")

    else: 
        print("O número secreto é MENOR")



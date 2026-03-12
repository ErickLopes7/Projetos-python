print("=== MINI CALCULADORA ===")

print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

opção = input("escolha uma operação").strip()  

numero1 = int(input("digite o primeiro numero"))
numero2 = int(input("digite o segundo numero"))

if opção == "1":
    resultado = numero1 + numero2
    print("resultado:", resultado)

elif opção == "2":
    resultado = numero1 - numero2 
    print("resultado:", resultado)))

elif opção == "3":
    resultado = numero1 * numero2 
    print("resultado:", resultado)

elif opção == "4":
    resultado = numero1 / numero2
    print("resultado:", resultado)

else:
    print("opção invalida")



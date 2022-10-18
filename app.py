import adivinhacao
import forca


print("[1] - Advinhação. ")
print("[2] - Forca. ")
op = input("Escolha um jogo: ")

if(int(op) == 1): 
    adivinhacao.jogar()
elif(int(op) == 2):
    forca.jogar()
else:
    print("Opção inválida. ")

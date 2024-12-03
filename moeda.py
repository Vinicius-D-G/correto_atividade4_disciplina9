import random

def girar_moeda():
    resultado = random.choice(["Cara", "Coroa"])
    print(f"O resultado é: {resultado}")

# Loop para o usuário girar várias vezes
while True:
    resposta = input("Digite 'girar' para lançar a moeda ou 'sair' para encerrar: ").strip().lower()
    if resposta == 'girar':
        girar_moeda()
    elif resposta == 'sair':
        print("Encerrando... Até a próxima!")
        break
    else:
        print("Comando inválido. Tente novamente.")

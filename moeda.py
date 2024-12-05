import random

# Contadores globais para "Cara" e "Coroa"
cara_count = 0
coroa_count = 0

def girar_moeda():
    """
    Simula o giro de uma moeda, atualizando os contadores globais
    e exibindo o resultado para o usuário.
    """
    global cara_count, coroa_count  # Permite modificar variáveis globais
    resultado = random.choice(["Cara", "Coroa"])
    if resultado == "Cara":
        cara_count += 1
    else:
        coroa_count += 1
    print(f"O resultado é: {resultado}")
    print(f"Contagem - Cara: {cara_count} | Coroa: {coroa_count}")

def mostrar_resultado_final():
    """
    Exibe o resultado final após o encerramento do programa.
    Mostra quantas vezes cada lado caiu e qual foi o mais frequente.
    """
    print("\n--- Resultados Finais ---")
    print(f"Total de Cara: {cara_count}")
    print(f"Total de Coroa: {coroa_count}")
    
    if cara_count > coroa_count:
        print("Cara caiu mais vezes!")
    elif coroa_count > cara_count:
        print("Coroa caiu mais vezes!")
    else:
        print("Empate! Ambos os lados caíram o mesmo número de vezes.")

# Loop para interação com o usuário
while True:
    resposta = input("Digite 'girar' para lançar a moeda ou 'sair' para encerrar: ").strip().lower()
    if resposta == 'girar':
        girar_moeda()
    elif resposta == 'sair':
        mostrar_resultado_final()
        print("Encerrando... Até a próxima!")
        break
    else:
        print("Comando inválido. Tente novamente.")

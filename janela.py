import tkinter as tk
import random

# Variáveis de contagem
cara_count = 0
coroa_count = 0

def girar_moeda():
    global cara_count, coroa_count
    resultado = random.choice(["Cara", "Coroa"])
    
    # Atualizar as contagens
    if resultado == "Cara":
        cara_count += 1
    else:
        coroa_count += 1

    # Exibir o resultado e as contagens
    resultado_label.config(text=f"Resultado: {resultado}")
    contagem_label.config(text=f"Cara: {cara_count} | Coroa: {coroa_count}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulador de Cara ou Coroa")

# Adicionando um botão para girar a moeda
girar_button = tk.Button(janela, text="Girar Moeda", command=girar_moeda, font=("Arial", 14))
girar_button.pack(pady=20)

# Label para mostrar o resultado
resultado_label = tk.Label(janela, text="Resultado: -", font=("Arial", 16))
resultado_label.pack(pady=10)

# Label para mostrar a contagem de caras e coroas
contagem_label = tk.Label(janela, text="Cara: 0 | Coroa: 0", font=("Arial", 14))
contagem_label.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()

# Projeto Cara ou Coroa

## **Objetivos do Projeto**
- Simular o lançamento de uma moeda virtual, gerando resultados aleatórios entre "Cara" e "Coroa".
- Implementar funcionalidades interativas e informativas para o usuário.
- Demonstrar boas práticas de desenvolvimento, incluindo o uso de Git para controle de versão.

## **Funcionalidades Planejadas**
1. Simulação do lançamento da moeda.
2. Contagem dos resultados de "Cara" e "Coroa".
3. Exibição do lado que caiu mais vezes ao final.
4. Interface interativa no terminal.
5. Organização e estruturação do código com boas práticas.

## **Cronograma de Desenvolvimento**
| Etapa                          | Descrição                                   | Prazo              |
|--------------------------------|---------------------------------------------|--------------------|
| 1. Configuração inicial        | Criar o repositório, configurar Git         | 1 dia              |
| 2. Estrutura básica do código  | Implementar a lógica inicial do programa    | 2 dias             |
| 3. Adicionar contadores        | Rastrear e exibir os resultados da moeda    | 1 dia              |
| 4. Mensagens finais            | Implementar resultado comparativo final     | 1 dia              |
| 5. Revisão e ajustes finais    | Revisar código, limpar erros e documentar   | 2 dias             |

---

## **Uso de Branches**
Para garantir organização e controle de versão, cada funcionalidade foi desenvolvida em uma branch específica:
- **Branch:** `feature/interface` - Desenvolvimento da interação no terminal.
- **Branch:** `feature/contador` - Adição do contador de resultados.
- **Branch:** `feature/resultados-finais` - Implementação do cálculo e exibição do lado mais frequente.

### **Exemplo de Criação e Merge**
```bash
# Criar branch para uma funcionalidade
git checkout -b feature/contador

# Fazer alterações e realizar commits
git add .
git commit -m "Implementa contador para resultados de Cara e Coroa"

# Retornar à branch principal e mesclar mudanças
git checkout main
git merge feature/contador

Documentação
Desafios Enfrentados
Geração de números aleatórios: Foi necessário garantir que o resultado fosse verdadeiramente imprevisível.
Gerenciamento de contadores globais: Houve ajustes para sincronizar os contadores com as ações do usuário.
Uso de Git para controle de versão: O uso de branches separadas ajudou a isolar cada funcionalidade e evitou conflitos.
Como o Git Ajudou
Controle de versões com branches tornou o desenvolvimento mais organizado.
O histórico de commits permitiu reverter mudanças problemáticas rapidamente.
Pull requests e merges garantiram a revisão e integração segura do código.


Como Usar
Requisitos
Python instalado:

Certifique-se de ter o Python 3.6 ou superior instalado em sua máquina.
Para verificar, execute:
bash
Copiar código
python --version
Clonar o repositório:

Baixe o código-fonte do repositório GitHub:
bash
Copiar código
git clone <link-do-repositorio>
cd cara-ou-coroa
Execução
Inicie o programa:

Execute o script principal diretamente no terminal:
bash
Copiar código
python cara_ou_coroa.py
Interaja com o programa:

O programa exibirá uma mensagem solicitando que você digite um comando:
arduino
Copiar código
Digite 'girar' para lançar a moeda ou 'sair' para encerrar:
Comandos Disponíveis
girar: Lança a moeda e exibe o resultado (Cara ou Coroa). O programa também atualiza a contagem de ocorrências de cada lado.
Exemplo de interação:

yaml
Copiar código
Digite 'girar' para lançar a moeda ou 'sair' para encerrar: girar
Resultado: Cara
Cara: 1 | Coroa: 0
sair: Encerra o programa e exibe um resumo dos resultados, indicando o lado mais frequente:

yaml
Copiar código
Encerrando... Até a próxima!
Resumo dos Resultados:
Cara: 3
Coroa: 2
O lado que apareceu mais vezes foi: Cara
Comando inválido: Caso digite algo diferente, o programa pedirá para tentar novamente:

arduino
Copiar código
Digite 'girar' para lançar a moeda ou 'sair' para encerrar: errado
Comando inválido. Tente novamente.
Exemplo de Fluxo Completo
plaintext
Copiar código
$ python cara_ou_coroa.py
Digite 'girar' para lançar a moeda ou 'sair' para encerrar: girar
Resultado: Cara
Cara: 1 | Coroa: 0

Digite 'girar' para lançar a moeda ou 'sair' para encerrar: girar
Resultado: Coroa
Cara: 1 | Coroa: 1

Digite 'girar' para lançar a moeda ou 'sair' para encerrar: sair
Encerrando... Até a próxima!
Resumo dos Resultados:
Cara: 1
Coroa: 1
O lado que apareceu mais vezes foi: Empate# correto_atividade4_disciplina9

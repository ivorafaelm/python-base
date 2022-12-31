#!/usr/bin/env python3
# A primeira linha indica que a versão do python que será usado é o python3 
# que está no env (disponível no path do ambiente);

"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente

Como usar:

Tenha a variável LANG devidamente configurada em seu sistema.

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

# As próximas linhas são metadados e são bastante utilizadas na distribui
# ção do software 
__version__ = "0.0.1"
__authon__ = "Ivo Rafael Santos Menezes"
__license__ = "Unlicense"

# Através do comando import a gente pode carregar códigos externos ao nosso
# programa. Serve inclusive para fazer o carregamento de módulos que já estão
# disponíveis por padrão nas instalações do python.
import os

# Início do código propriamente dito

# Obs1. A variável __name__ só terá o valor de __main__ se o código estiver
# sendo executado a partir de um terminal. Caso ela esteja sendo chamada
# por um outro programa essa variável irá assumir o nome do programa.

# Obs2. Esta formação pode ser utilizada para indicar que este é o bloco 
# principal do programa em Python.

# Obs3. Este tipo de formação está caindo em desuso e irá ficar disponível
# como comentário para efeitos de estudo.

# if __name__ == "__main__":
#    print("Hello, World!!")

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_BR":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
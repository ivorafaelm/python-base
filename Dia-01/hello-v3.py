#!/usr/bin/env python3
# A primeira linha indica que a versão do python que será usado é o python3 
# que está no env (disponível no path do ambiente);

"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente

Como usar:

Tenha a variável LANG devidamente configurada em seu sistema.

    export LANG=pt_BR

Passe os argumentos no momento da execução

    python3 hello.py --lang=pt_BR --count=2

Informe no momento através da opção input, caso a variável LANG não exista no S.O.


Execução:

    python3 hello.py
    ou
    ./hello.py
"""

# As próximas linhas são metadados e são bastante utilizadas na distribui
# ção do software 
__version__ = "0.1.3"
__authon__ = "Ivo Rafael Santos Menezes"
__license__ = "Unlicense"

# Através do comando import a gente pode carregar códigos externos ao nosso
# programa. Serve inclusive para fazer o carregamento de módulos que já estão
# disponíveis por padrão nas instalações do python.

import os
import sys

# O comando abaixo é interessante para efetuar debug, pois ele apresenta o 
# parâmetro e o seu valor
# print(f"{sys.argv=}")
# A saída do comando seria sys.argv=["hello.py"] -> python hello.py
# Para a seguinte chamada pyhton hello.py --lang=fr_FR -> sys.argv=["hello.py", "lang=fr_FR"]

arguments = {
    "lang": None,
    "count": 1,
}
# O slice foi feito a partir da posição 1, pois a posição 0 indica o nome do 
# arquivo e não nos interessa. O que nos interessa são os argumentos que serão
# informados nas posiçoes seguintes. 
for arg in sys.argv[1:]:
    # Os valores podem ser desempacotados através do resultado do split feito a partir do caractere = 
    key, value = arg.split("=")
    # Dessa forma será exibido um erro "ValueError" nos casos em que o usuário informar 
    # parâmetros inválidos. Esse erro será tratado em uma versão futura.
    
    # Efetuar a remoção dos -- informados antes da chave do parâmetro e os espaços em branco do 
    # começo e do final de cada argumento
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()
    
    arguments[key] = value
    
current_language = arguments["lang"]
if current_language is None:
    # TODO usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language")
        
current_language = current_language[:5]

msg ={
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language] * int(arguments["count"]))

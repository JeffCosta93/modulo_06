"""1° O módulo random, que fornece funções para geração de números aleatórios.
   2° Em seguida, uma lista é chamada e definida com os elementos [1, 2, 3, 4, 5]
   3° A função random.choice(lista) é usada para selecionar aleatoriamente um elemento da lista e atribuí-lo à
      variável onde ela conterá um valor aleatório entre 1 e 5. """

import random

lista = list(range(10, 21))
numero_aleatorio = random.choice(lista)
print(numero_aleatorio)


import random

lista = list(range(1, 101))
lista_aleatoria = [random.choice(lista) for _ in range(5)]
print(lista_aleatoria)

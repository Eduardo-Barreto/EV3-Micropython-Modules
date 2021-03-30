#!/usr/bin/env pybricks-micropython
# ↑ Interpretador do python definido para o EV3

# Importações dos módulos utilizados
# Módulo principal do brick importado da biblioteca principal
from pybricks.hubs import EV3Brick
# Módulo de cores do brick
from pybricks.parameters import Color
# Módulo de esperar, dentro das ferramentas
from pybricks.tools import wait

# Inicializar o brick
ev3 = EV3Brick()

'''
Podemos controlar o sistema de luzes do bloco muito facilmente
Para ligar, usamos a função
    ev3.light.on(color)
no parâmetro "color" passamos a cor que desejamos
As cores disponíveis para essa parte são:
    Color.RED
    Color.GREEN
    Color.YELLOW
    Color.ORANGE
'''

# Lista de cores disponíveis / compativeis com o brick
cores_disponiveis = [
    Color.GREEN,    # Verde
    Color.YELLOW,   # Amarelo
    Color.RED,      # Vermelho
    Color.ORANGE    # Laranja
]


# Criar uma função que passa por todas as cores disponíveis
def mudar_cores():
    # Para cada cor na lista de cores disponíveis
    for cor in cores_disponiveis:
        # Ligar luzes na cor do momento
        ev3.light.on(cor)
        # Esperar 1 segundo
        wait(1000)


'''
Existem duas principais maneiras de desligar as luzes do bloco
    1. ev3.light.off() - Jeito certo
    2. ligar em uma cor indisponível
'''


def teste_desligar():
    # Inicia ligando na cor verde
    ev3.light.on(Color.GREEN)
    # Mantém ligado por 1 segundo
    wait(1000)
    # Desliga do modo convencional
    ev3.light.off()
    # Mantém desligado por meio segundo
    wait(500)
    # Liga novamente na cor verde
    ev3.light.on(Color.GREEN)
    # Mantém ligado por 1 segundo
    wait(1000)
    # Desliga do modo gambiarrento
    ev3.light.on(Color.BROWN)
    # Mantém desligado por meio segundo
    wait(500)

    # Os dois modos funcionam, mas o light.off() é altamente recomendado


# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossas funções de teste
    mudar_cores()
    teste_desligar()

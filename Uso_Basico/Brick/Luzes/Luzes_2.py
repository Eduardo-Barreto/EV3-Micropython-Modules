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
Ao usarmos cores, podemos facilitar o processo com uma classe,
para evitar a escrita complexa de coisas como "Color.RED" por exemplo,
podemos transformar em uma maneira mais simples apresentada a seguir
'''

# Uma classe possui suas variáveis, que possuem seu valor
class cores:
    # A variável VERDE tem como valor a cor verde
    VERDE    =  Color.GREEN
    # E assim por diante
    AMARELO  =  Color.YELLOW
    VERMELHO =  Color.RED
    LARANJA  =  Color.ORANGE


# Para ligarmos a luz amarela agora, podemos utilizar:
def main():
    # Liga a luz na cor especificada de acordo com a classe
    ev3.light.on(cores.AMARELO)
    # Mantém ligada por 1 segundo
    wait(1000)
    # Desliga
    ev3.light.off()
    # Mantém desligada por 1 segundo
    wait(1000)

# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossa função de teste
    main()


#!/usr/bin/env pybricks-micropython
# ↑ Interpretador do python definido para o EV3

# Importações dos módulos utilizados

# Módulo principal do brick importado da biblioteca principal
from pybricks import ev3brick as brick
# Módulo dos botões do brick
from pybricks.parameters import Button
# Módulo de esperar, dentro das ferramentas
from pybricks.tools import wait

# Importa a nossa outra função criada no outro programa
from Botoes_1 import pressionado

'''
Ao executar o programa anterior, você perceberá que ao pressionar o botão
muitas linhas foram registradas no console, e isso acontece por conta da
taxa de atualização do programa.

Quando você aperta o botão uma vez, ele percebe isso e escreve no console,
mas não espera você soltar, e é isso que vamos explorar nesse programa
'''


# Criar uma função que verifica se um botão não está pressionado
def solto(botao):
    # Se o botão escolhido não estiver dentro da lista de botões pressionados
    if botao not in brick.buttons():
        # Retorna verdadeiro
        return True
    # Senão
    else:
        # Retorna falso
        return False


# Criar uma função que espera o botão ser pressionado e depois solto
def esperar_pressionado_solto(botao):
    # Enquanto o botão não for pressionado
    while not pressionado(botao):
        # Faz uma pausa de 10 ms
        wait(10)

    # Após pressionado, enquanto não for solto
    while not solto(botao):
        # Faz uma pausa de 10 ms
        wait(10)

    # Ou seja, verifica de 10 em 10 ms nossas condições

# Vamos testar!
def main():
    print('Inicio do teste... Pressione e solte o botão!')
    esperar_pressionado_solto(Button.UP)
    print('Botão pressionado e solto!')


# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossa função de teste
    main()

# Fonte:
# https://pybricks.github.io/ev3-micropython/hubs.html#pybricks.hubs.EV3Brick.buttons.pressed

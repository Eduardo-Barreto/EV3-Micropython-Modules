#!/usr/bin/env pybricks-micropython
# ↑ Interpretador do python definido para o EV3

# Importações dos módulos utilizados
# Módulo principal do brick importado da biblioteca principal
from pybricks import ev3brick as brick
# Módulo dos botões do brick
from pybricks.parameters import Button

# Podemos pegar a lista de botões pressionados com a função
# brick.buttons()
botoes_pressionados = brick.buttons()
print(botoes_pressionados)
'''
Retornos possíveis
╔═════════════╦═══════════════╦══════════════╗
║  ---------- ║   Button.UP   ║  ----------  ║
╠═════════════╬═══════════════╬══════════════╣
║ Button.LEFT ║ Button.CENTER ║ Button.RIGHT ║
╠═════════════╬═══════════════╬══════════════╣
║  ---------- ║  Button.DOWN  ║  ----------  ║
╚═════════════╩═══════════════╩══════════════╝
Disponível em:
https://pybricks.github.io/ev3-micropython/parameters.html#pybricks.parameters.Button
'''


# Criar uma função que verifica se um botão está pressionado
def pressionado(botao):
    # Se o botão escolhido estiver dentro da lista de botões pressionados
    if botao in brick.buttons():
        # Retorna verdadeiro
        return True
    # Senão
    else:
        # Retorna falso
        return False


# Uso da função
def main():
    # Loop infinito
    while True:
        # Se o botão de cima estiver pressionado
        if pressionado(Button.UP):
            # Escreve no console que ele está pressionado!
            print('Botão pra cima pressionado!')
    # Ou seja, toda vez que o botão de cima for pressionado
    # Será registrado no console


# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossa função de teste
    main()


# Fonte:
# https://pybricks.github.io/ev3-micropython/hubs.html#pybricks.hubs.EV3Brick.buttons.pressed

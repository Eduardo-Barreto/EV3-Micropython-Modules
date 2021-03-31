#!/usr/bin/env pybricks-micropython
# ↑ Interpretador do python definido para o EV3

# Importações dos módulos utilizados
# Módulo principal do brick importado da biblioteca principal
from pybricks.hubs import EV3Brick

# Inicializar o brick
ev3 = EV3Brick()

'''
Além de tocar beeps e arquivos, também podemos
fazer nosso EV3 falar!
para isso, usamos a função say()
que é configurada pela set_speech_options
'''

# Vamos configurar nosso "falador"!
ev3.speaker.set_speech_options(
    language='pt-br',  # Linguagem de fala, vamos deixar em português (BR)
    voice=None,     # A voz usada (em portugues só tem uma 😭)
    speed=None,     # Velocidade em palavras por minuto, manteremos padrão
    pitch=None      # Tom de voz, podemos alterar de 0 a 99, manteremos padrão
)


# Vamos testar com uma frase!
def main():
    ev3.speaker.say('A filha da Xuxa se chama Sasha!')


# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossa função de teste
    main()

# Fonte:
# https://pybricks.github.io/ev3-micropython/hubs.html#pybricks.hubs.EV3Brick.speaker.beep

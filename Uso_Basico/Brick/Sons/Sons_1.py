#!/usr/bin/env pybricks-micropython
# ↑ Interpretador do python definido para o EV3

# Importações dos módulos utilizados
# Módulo principal do brick importado da biblioteca principal
from pybricks.hubs import EV3Brick

# Inicializar o brick
ev3 = EV3Brick()

# Para usar os sons do EV3 usamos o módulo speaker
# Tocar um beep com uma frequencia de 500 hz e duração de 100 ms
ev3.speaker.beep(frequency=500, duration=100)
# Você pode padronizar alguns sons para avisar coisas durante a programação

# Com a função set_volume você pode configurar o volume do speaker
ev3.speaker.set_volume(
    volume=100,  # 100% de volume
    which='_all_'  # Quais volumes serão alterados
    # 'Beep' para beeps, 'PCM' para notas e fala. O '_all_' afeta todos
)


# Criar uma função para um beep padronizado para usar quando o robõ ver verde
def aviso_verde():
    ev3.speaker.beep(frequency=600, duration=300)
    # Assim em vez de digitar tudo isso toda vez que quiser um aviso de verde
    # Você pode escrever somente "aviso_verde()"
    # e ele tocará o seu beep padrão


# Uma forma de facilitar isso é usando notas, com o play_notes
# Criar uma função para tocar todas as notas disponíveis
# Lista com as notas disponíveis
notas_disponiveis = [
    # O formato das notas é NotaOitava/tempo e as oitavas vão de 2 até 8
    'C4/4',  # Nota C (dó) na 4ª oitava, 1/4 de tempo
    'C#4/4',
    'D4/4',
    'D#4/4',
    'E4/4',
    'F4/4',
    'F#4/4',
    'G4/4',
    'G#4/4',
    'A4/4',
    'A#4/4',
    'B4/4',
    'C5/4'
]

# Incluí uma visão delas em um piano, basta acessar o link abaixo
# https://github.com/Eduardo-Barreto/EV3_Micropython_Modules/blob/master/Uso_Basico/Brick/Sons/notas_disponiveis.png


def tocar_notas(notas):
    # Toca as notas por 120 bpm (1 batida = nota de 1/4)
    ev3.speaker.play_notes(notes=notas, tempo=120)


'''
Também podemos fazer nosso ev3 tocar um som de um arquivo
Para isso, usamos a função play_file() e passamos
o caminho para o nosso arquivo como argumento
Tive alguns problemas usando arquivos .mp3
sugiro que use o formato WAV
se tem um mp3 e deseja usar, pode converter em
https://cloudconvert.com/mp3-to-wav
'''
# Função principal do programa


def main():
    # Toca as notas da nossa lista
    print('tocando notas...')
    tocar_notas(notas_disponiveis)
    # Toca o nosso arquivo, que está nessa mesma pasta
    # https://github.com/Eduardo-Barreto/EV3_Micropython_Modules/blob/master/Uso_Basico/Brick/Sons/arquivo_de_som.wav
    print('tocando arquivo...')
    ev3.speaker.play_file('arquivo_de_som.wav')


# Se o programa está executando como principal
if __name__ == '__main__':
    # Executa nossa função de teste
    main()

# Fonte:
# https://pybricks.github.io/ev3-micropython/hubs.html#pybricks.hubs.EV3Brick.speaker.beep

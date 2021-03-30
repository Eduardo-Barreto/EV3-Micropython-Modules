# Botões
Essa pasta mostra alguns exemplos de como usar os botões

Dentro deles temos a possibilidade de verificar se um botão está pressionado ou solto, além de uma função que espera até que ele esteja pressionado e depois solto (pulsado)

# Uso
Para usar, você pode importar os módulos no seu programa, desde que tenha os arquivos na sua pasta

**Arquivos**:
```
📂sua_pasta
 └ main.py
 └ Botoes_1.py
 └ Botoes_2.py
```
**Importação (no `main.py`)**
```python
from Botoes_1 import pressionado
from Botoes_2 import solto, esperar_pressionado_solto
```
Também é possível juntar os dois arquivos num só:
```
📂sua_pasta
 └ main.py
 └ Botoes.py
```
A importação fica assim:
```python
from Botoes import *
```
> o `*` indica que tudo de dentro de `Botoes` deve ser importado

Se preferir, também pode colocar o conteúdo no seu arquivo `main.py` (o principal lido pelo micropython) e executar diretamente

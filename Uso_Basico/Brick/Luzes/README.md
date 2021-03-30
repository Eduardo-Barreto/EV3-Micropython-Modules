# Luzes
Essa pasta mostra alguns exemplos de como usar as luzes

Dentro delas temos a possibilidade de apagar as luzes ou acender com a cor que desejarmos

# Uso
Para usar, você pode importar os módulos no seu programa, desde que tenha os arquivos na sua pasta
**Arquivos**:
```
📂sua_pasta
 └ main.py
 └ Luzes_1.py
 └ Luzes_2.py
```
**Importação (no `main.py`)**
```python
from Luzes_1 import mudar_cores
from Luzes_2 import cores
```
Também é possível juntar os dois arquivos num só:
```
📂sua_pasta
 └ main.py
 └ Luzes.py
```
A importação fica assim:
```python
from Luzes import *
```
> o `*` indica que tudo de dentro de `Luzes` deve ser importado

Se preferir, também pode colocar o conteúdo no seu arquivo `main.py` (o principal lido pelo micropython) e executar diretamente

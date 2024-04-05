---
blogpost: true
date: Apr 4, 2024
author: jbolo
location: Lima, Perú
category: Snippets
tags: csv, pandas, utilidades
language: Español
---

# Leyendo archivos CSV con Pandas

En esta publicación, discutiremos cómo leer archivos CSV usando pandas, una biblioteca básica para el manejo de datos escritos en Python.

![Python developer](/_static/images/biblioteca_pandas.jpg)

Primero nos aseguraremos de tener instalado Pandas en nuestro sistema y con Python 3:

```bash
pip install pandas
```

Usaremos un archivo base para empezar `sample.csv`:

```text
id,name,job,score
1,'Wilmer Pacheco','Software Engineer',92
2,'Bruno Cordova','Assassin',95
3,'Cexitar Anaya','Batman',99
4,'Yisas Manchego','Superman',95
```

## Cargando el archivo CSV:

Para leer el archivo CSV usando pandas, nosotros usaremos la funcion `read_csv`:

```python
import pandas
df = pandas.read_csv('data/sample.csv')
print(df)
```

La salida de la ejecución será de la siguiente manera:

```bash
$ python sample.py
   id              name                  job  score
0   1  'Wilmer Pacheco'  'Software Engineer'     92
1   2   'Bruno Cordova'           'Assassin'     95
2   3   'Cexitar Anaya'             'Batman'     99
3   4  'Yisas Manchego'           'Superman'     95
```

El comando generará una salida de lectura amigable de acuerdo al contenido del archivo CSV.

## Indicando el separador:

El archivo CSV no necesariamente usa la coma como separador, este podría ser cualquier caracter como `\t`, `|` … etc.

Afortunadamente, hay una opcion en la función `read_csv`que ayuda a cargar los archivos CSV con un separador en específico.

```python
df = pandas.read_csv('data/sample.csv', sep='\t')
```

El alias para `sep` es `delimiter`. El resultado será el mismo.

```python
df = pandas.read_csv('data/sample.csv', delimiter='\t')
```

El separador puede ser una secuencia de caracteres.

```python
df = pandas.read_csv('data/sample.csv', sep='||')
```


## Control de la fila cabecera:

CSV file might not have the header row, so if you execute the script in this case:
El archivo CSV podría no tener una fila cabecera, si se ejecuta el script:

```python
df = pandas.read_csv('data/sample.csv')
```

La salida muestra:

```python
   1  'Wilmer Pacheco' 'Software Engineer'  92
0  2   'Bruno Cordova'          'Assassin'  95
1  3   'Cexitar Anaya'            'Batman'  99
2  4  'Yisas Manchego'          'Superman'  95
```

pandas asumirá que la primera fila es la cabecera.

Para ello, nosotros podemos pasar la opcion `header=None` y decirle a pandas que no hay fila cabecera en el archivo CSV.

```python
df = pandas.read_csv('data/sample.csv', header=None)
```

y tendremos la salida:

```text
   0                 1                    2   3
0  1  'Wilmer Pacheco'  'Software Engineer'  92
1  2   'Bruno Cordova'           'Assassin'  95
2  3   'Cexitar Anaya'             'Batman'  99
3  4  'Yisas Manchego'           'Superman'  95
```

Como no especificamos ningún encabezado, pandas usa un valor entero para indexar la fila del encabezado.

También podemos establecer nombres para cada columna mediante la opción `names=[]` option.


```python
df = pandas.read_csv('data/sample.csv', names=['id', 'nombre', 'trabajo', 'score'])
```

Esto nos mostrará la salida:

```text
   id              name                  job  score
0   1  'Wilmer Pacheco'  'Software Engineer'     92
1   2   'Bruno Cordova'           'Assassin'     95
2   3   'Cexitar Anaya'             'Batman'     99
3   4  'Yisas Manchego'           'Superman'     95
```

---
blogpost: true
date: Feb 10, 2025
author: soloidx
location: Lima, Perú
category: Data science
tags: pandas, python, csv
language: Español
---

# Introducción a DuckDB: Una alternativa ligera y poderosa para análisis de datos

Cuando pensamos en base de datos normalmente se nos ocurre Oracle, PostgreSQL o hasta Redis y MongoDB, pensamos en servidores dentro de arquitecturas con múltiples nodos y clientes que se comunican por la red. Sin embargo no todas las aplicaciones requieren ser tan complejas,  tenemos por ejemplo a SQLite, que es ligero y embebido (se integra directamente en la aplicación y no requiere de un servidor) y por eso suele ser la solución perfecta para muchas aplicaciones móviles y web.

![Python developer](/_static/images/introduction_duckdb.png)

Usando SQLite como inspiración nació DuckDB, es una herramienta que, para análisis de datos no requiere de dependencias externas y se ejecuta eficientemente en memoria y es lo suficientemente flexible como para soportar diferentes tipos de datos. En este artículo exploraremos cómo usar DuckDB con Python y por qué puede ser una excelente alternativa para ciertas cargas de trabajo.

## Primeros pasos:

Empezamos instalando DuckDB:

```bash
pip install duckdb
```

Luego dentro de un script o en el REPL iniciamos una instancia:

```python
import duckdb

con = duckdb.connect(database=":memory:", read_only=False)
con.execute("SET temp_directory='/tmp/duckdb.temp';")
```

Aquí:
- Creamos una conexión `con` con la base de datos configurada en memoria.
- Creamos un directorio temporal (en el caso nos quedemos sin memoria)

Ahora obtenemos datos de un archivo CSV con 100 clientes:

```python
customer_100 = con.query("SELECT * FROM read_csv('data/customers-100.csv', normalize_names=TRUE)")
print(customer_100)
```

```text
┌─────────────────┬────────────┬─────────────────────────────────┬───────────────────┐
│   customer_id   │ first_name │             company             │       city        │
│     varchar     │  varchar   │             varchar             │      varchar      │
├─────────────────┼────────────┼─────────────────────────────────┼───────────────────┤
│ DD37Cf93aecA6Dc │ Sheryl     │ Rasmussen Group                 │ East Leonard      │
│ 1Ef7b82A4CAAD10 │ Preston    │ Vega-Gentry                     │ East Jimmychester │
│ 6F94879bDAfE5a6 │ Roy        │ Murillo-Perry                   │ Isabelborough     │
│ 5Cef8BFA16c5e3c │ Linda      │ Dominguez, Mcmillan and Donovan │ Bensonview        │
│ 053d585Ab6b3159 │ Joanna     │ Martin, Lang and Andrade        │ West Priscilla    │
│ 2d08FB17EE273F4 │ Aimee      │ Steele Group                    │ Chavezborough     │
│ EA4d384DfDbBf77 │ Darren     │ Lester, Woodard and Mitchell    │ Lake Ana          │
│ 0e04AFde9f225dE │ Brett      │ Sanford, Davenport and Giles    │ Kimport           │
│ C2dE4dEEc489ae0 │ Sheryl     │ Browning-Simon                  │ Robersonstad      │
│ 8C2811a503C7c5a │ Michelle   │ Beck-Hendrix                    │ Elaineberg        │
├─────────────────┴────────────┴─────────────────────────────────┴───────────────────┤
│ 10 rows                                                                  4 columns │
└────────────────────────────────────────────────────────────────────────────────────┘
```

Eso ha sido sencillo, DuckDB ha sido desarrollado como una herramienta OLAP (procesamiento analítico en línea) por lo que permite analizar múltiples archivos eficientemente aquí podemos ver:

```python
import time
import csv

file_path = 'data/customers-2000000.csv'

start = time.time()

with open(file_path, newline='') as csvfile:
    data = list(csv.DictReader(csvfile))

end = time.time()
print(f"CSV read time: {end - start} seconds")

start = time.time()
customer_100 = con.query(f"SELECT * FROM read_csv('{file_path}')")
end = time.time()

print(f"DuckDB read time: {end - start} seconds")
```

Aquí estamos comparando la implementación básica con Python y la de DuckDB, estos son los tiempos:

```text
CSV read time: 5.0357770919799805 seconds
DuckDB read time: 0.061506032943725586 seconds
```

## Integración con Pandas y Pyarrow

DuckDB es flexible al momento de integrarse con otras fuentes de datos como Pandas o Pyarrow

```python
import pandas as pd
from pyarrow import csv


source_path = "data/customers-100.csv"

pd_dataframe = pd.read_csv(source_path)
pa_table = csv.read_csv(source_path)

data = con.query("SELECT * FROM pd_dataframe LIMIT 10;")
print(data)
data = con.query("SELECT * FROM pa_table LIMIT 10;")
print(data)
```

En el código anterior podemos ver que el query toma el nombre de la variable, la conexión toma el valor directamente del scope local e inserta los datos transparentemente.

En otro escenario, si lo que queremos es tomar los datos de DuckDB y ponerlos en un DataFrame de Pandas o Pyarrow podemos hacerlo de esta manera:

```python
customer_100 = con.query("SELECT * FROM read_csv('data/customers-100.csv')")

dataframe = customer_100.df()

pa_table = customer_100.arrow()

print(type(dataframe))
print(type(pa_table))
```
## Integración con la nube

Muchos de los datos que utilizamos no se encuentran almacenados localmente, y para procesarlos tenemos que conectarnos a nubes como AWS, GCP o Azure. Para esto, DuckDB contiene extensiones que podemos instalar y usar para poder conectarnos y hacer consultas directamente desde la nube.

```python
# AWS?

con.execute("INSTALL httpfs;")
con.execute("LOAD httpfs;")
con.execute("INSTALL aws;")
con.execute("LOAD aws;")
con.execute("set http_keep_alive=false;")
con.execute("set s3_endpoint='s3.us-west-2.amazonaws.com';")
con.execute("set s3_region='us-west-2';")
con.execute("CALL load_aws_credentials();")

source = "s3://soloidx-bank1305/apps/balancesheetriskmanagement/output/instrument/data/"

con.query(f"SELECT COUNT(*) FROM read_parquet('{source}**/*.parquet', hive_partitioning = true);")
```

También cabe resaltar que DuckDB maneja eficientemente las consultas sobre directorios, si tenemos un directorio con datos en particiones (como Apache Hive) las consultas se hacen solamente en las particiones definidas en el WHERE dentro del query.

Para terminar, DuckDB es una opción poderosa y ligera para el análisis de datos, ya que no requiere un servidor y se ejecuta eficientemente en memoria. Su rapidez en la lectura y procesamiento de archivos como Parquet, CSV, JSON (y hasta Excel!) lo hace ideal para tareas analíticas sin depender de bases de datos tradicionales. Además, su integración nativa con Pandas y PyArrow y la posibilidad de leer datos de la nube permite a los desarrolladores trabajar con datos de manera fluida dentro de sus flujos de trabajo habituales en Python.

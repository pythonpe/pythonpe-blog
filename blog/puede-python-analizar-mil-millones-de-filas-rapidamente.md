---
blogpost: true
date: 15 Apr, 2024
author: hellhound
category: Desafío de Mil Millón de Filas
tags: 1brc, python, ai-generated
---

# Explorando el Desafío de Mil Millón de Filas en Python

El desafío de procesar mil millón de filas de datos es una tarea intimidante que pone a prueba la
capacidad de cualquier lenguaje de programación, incluido Python. En este artículo, exploraremos
cómo Python, con su naturaleza interpretada, se compara ante este reto colossal, adoptando
estrategias ingeniosas y aprovechando la potencia de las librerías disponibles para manejar una tarea
de procesamiento de datos de tal magnitud.

```{youtube} utTaPW32gKY
```

## Python Puro vs Competidores Compilados

Este recorrido comienza con una implementación simple en Python puro, utilizando diccionarios para
agrupar mediciones por ciudad y calcular valores mínimos, máximos y promedios de temperatura. Esta
aproximación tomó 9 minutos y 28 segundos para ejecutarse en un archivo de texto de 13GB, una
diferencia notable frente a la implementación base en Java que corre en 3 minutos y 12 segundos.

No obstante, el cambio a PyPy, un intérprete JIT para Python, mejora significativamente los tiempos
de ejecución, demostrando el potencial oculto dentro de Python a través de optimizaciones y el uso
de intérpretes alternativos.

## Estrategias de Escalado en Python

Una serie de estrategias dentro del ecosistema Python fueron exploradas para abordar este
desafío. La utilización de múltiples núcleos de CPU mediante el módulo `multiprocessing`, el ajuste
de estructuras de datos y la manipulación astuta de cadenas de bytes fueron solo algunas de las
tácticas empleadas para exprimir cada onza de rendimiento del lenguaje.

La implementación más rápida puramente en Python, nombrada aquí como Doug Booty versión 2,
demostró ser un esfuerzo complicado pero fructífero, capaz de ejecutarse en un impresionante tiempo
de sub 10 segundos, acercándose al rendimiento de soluciones altamente optimizadas en lenguajes
compilados.

## Extendiendo las Fronteras de Python

Para aquellos dispuestos a "estirar" su definición de qué constituye código Python, librerías
como **Polars** y **DuckDB** ofrecen una alternativa atrayente. Escritas en Rust y C++,
respectivamente, estas librerías se instalan con un simple comando `pip` y revelan un nuevo
nivel de rendimiento, demostrando ser tan rápidas como la mejor implementación pura de Python
con una complejidad significativamente reducida.

### Polars: Tratamiento de Datos con Rust

Polars propone una interfaz simple para el procesamiento de grandes volúmenes de datos, permitiendo
operaciones de agrupamiento y agregación con una sintaxis sucinta y expresiva. Esta aproximación
no solo iguala el rendimiento de la solución Python pura más rápida sino que también ofrece una
mayor simplicidad y mantenibilidad.

### DuckDB: Un Motor SQL para Análisis de Datos

DuckDB transforma completamente el enfoque hacia el procesamiento de datos, permitiendo que las
operaciones se expresen en términos de SQL sobre una base de datos en memoria. Con tiempos de
ejecución rondando los 9 segundos para archivos de texto y reduciéndose a 5 segundos para archivos
en formato parquet, DuckDB se presenta como una solución potente y versátil para el análisis de
datos.

## Conclusión

Aunque Python no pueda competir directamente con lenguajes compilados en términos de velocidad en
bruto, la riqueza de su ecosistema, la flexibilidad de sus herramientas y la creatividad de su
comunidad le permiten enfrentarse a desafíos de procesamiento de datos de gran magnitud de manera
efectiva. Ya sea mediante técnicas ingeniosas de programación en Python puro o a través del uso de
librerías potentes escritas en lenguajes compilados, Python continúa demostrando ser una herramienta
valiosa y versátil en el mundo de la ingeniería de software y el análisis de datos.

¿Te interesa profundizar en las estrategias Pythonicas para el manejo de grandes volúmenes de
datos? Te invitamos a explorar más sobre este fascinante viaje en el video adjunto y a sumergirte
en el mundo del procesamiento de datos con Python.

```{admonition} Referencias
Desafío principal - https://github.com/gunnarmorling/1brc

Ifnesi - https://github.com/ifnesi/1brc/tree/main

Booty - https://github.com/booty/ruby-1-billion/

Solución de Danny van Kooten C - https://www.dannyvankooten.com/blog/2024/1brc/

Post de Awesome duckdb - https://rmoff.net/2024/01/03/1%EF%B8%8F⃣%EF%B8%8F-1brc-in-sql-with-duckdb/

Duelo de pypy vs Cpython - https://jszafran.dev/posts/how-pypy-impacts-the-performance-1br-challenge/
```

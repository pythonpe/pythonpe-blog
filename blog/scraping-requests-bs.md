---
blogpost: true
date: Apr 8, 2024
author: jbolo
location: Lima, Perú
category: Snippets
tags: scraping, requests, beautifulsoup4, utilidades
language: Español
---

# Scraping con Python utilizando la biblioteca requests

![Python developer](/_static/images/scraping-requests.jpg)

## Introducción
El scraping web es una técnica poderosa para extraer datos de páginas web de manera automatizada. Python, con su amplio ecosistema de bibliotecas, proporciona herramientas robustas para realizar scraping de manera eficiente. En este artículo, exploraremos cómo utilizar la biblioteca `requests` de Python para realizar scraping básico.

## ¿Qué es el scraping web?
El scraping web es el proceso de extracción de información de páginas web de manera automatizada. Se utiliza para recopilar datos de interés, como precios de productos, información de noticias, estadísticas, y más. Aunque puede ser una técnica útil, es importante utilizarla con responsabilidad y ética, respetando los términos de servicio de los sitios web y evitando la sobrecarga de los servidores.

## Realizando scraping con Python y requests
La biblioteca `requests` de Python nos permite realizar solicitudes HTTP de manera sencilla, lo que es fundamental para el scraping. Además, utilizaremos la biblioteca `beautifulsoup4` para analizar el contenido HTML de las páginas web. A continuación, mostraremos un ejemplo práctico de cómo utilizar `requests` para extraer datos del clima de Lima desde la página web del Servicio Nacional de Meteorología e Hidrología del Perú (SENAMHI).

## Instalación de dependencias
Antes de comenzar, asegúrate de tener instaladas las dependencias necesarias. Puedes instalarlas utilizando `pip`, el administrador de paquetes de Python:

```sh
pip install requests beautifulsoup4
```

## Ejemplo práctico: Scraping del clima en Lima desde SENAMHI
Supongamos que queremos obtener el pronóstico del clima para Lima de hoy desde la página web del SENAMHI. Utilizaremos `requests` para enviar una solicitud a la página web correspondiente y luego extraeremos los datos que nos interesan.

```python
import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP
url = 'https://www.senamhi.gob.pe/?&p=home'
response = requests.get(url)

# Parsear la página web
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar la sección del clima para Lima
lima_section = soup.find('div', class_='lima')

# Extraer los datos del clima
temperatura = lima_section.find('div', class_='cajaTemperatura').text.strip()
condiciones = lima_section.find('div', class_='imgDescripcion').text.strip()

# Imprimir los datos del clima
print(f'Temperatura en Lima: {temperatura}')
print(f'Condiciones en Lima: {condiciones}')
```

En este ejemplo, primero realizamos una solicitud HTTP a la URL del sitio web del SENAMHI. Luego, utilizamos BeautifulSoup para analizar el contenido de la página y encontrar la sección correspondiente al clima de Lima. A partir de ahí, extraemos la temperatura y las condiciones climáticas y las imprimimos en la consola.

# Conclusiones
El scraping web con Python y la biblioteca `requests` ofrece una forma poderosa de recopilar datos de páginas web de manera automatizada. Sin embargo, es importante utilizar esta técnica de manera responsable y ética, respetando los términos de servicio de los sitios web y evitando la sobrecarga de los servidores. Con las herramientas adecuadas y un enfoque cuidadoso, el scraping web puede ser una herramienta valiosa para recopilar información útil en tus proyectos.
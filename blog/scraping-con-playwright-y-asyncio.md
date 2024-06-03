---
blogpost: true
date: 02 Jun, 2024
author: hellhound
category: Scraping
tags: python, scraping, playwright, asyncio
language: Español
---

# Desarrollando un Bot de Scraping Evasivo

En el mundo del scraping, enfrentamos constantemente la batalla contra
mecanismos de defensa diseñados para detectar y bloquear nuestros bots. Hoy,
quiero compartirles un proyecto personal que busca no solo sortear estas
defensas, sino hacerlo de manera eficiente y escalable.

## El Contexto

Al intentar extraer datos de un sitio web que utiliza Radware, un servicio
avanzado contra bots de scraping, me vi en la necesidad de crear una solución
que pudiera superar estos obstáculos. Aquí les presento cómo logré desarrollar
un bot de scraping que no solo logra su cometido sino que evita ser detectado
por mecanismos de anti-bots.

```{youtube} G_t2DXSwx-I
```

## La Implementación

La herramienta está desarrollada en Python, utilizando librerías como
**Playwright** para la navegación y manipulación de sitios web y **asyncio**
para la ejecución asincrónica que permite escalar el proceso de scraping.  El
script realiza una navegación automatizada, seleccionando dinámicamente opciones
en un formulario y resolviendo CAPTCHAs.

### Selección y Extracción

El bot automático realiza la selección de opciones en un formulario de manera
secuencial: primero selecciona una ubicación, luego un tipo de juzgado, y así
sucesivamente hasta llegar a ingresar un año (en nuestro caso, 2024) y un número
de expediente. Una vez superado el CAPTCHA, accede a los datos deseados.

### Refinamiento del Scraping

Una vez dentro del registro, el bot captura la información relevante tanto del
contenido principal del registro como de los detalles proporcionados en
secciones adicionales. Si el formulario revela más de un registro, el bot
iterará sobre cada uno, extrayendo todos los datos necesarios antes de reiniciar
el proceso con un nuevo conjunto de entradas.

## Tecnologías y Enfoques

El uso de **Typer** para la gestión de la línea de comandos facilita la
interacción con el script, permitiendo especificar el rango de documentos y
otros parámetros de manera sencilla. Este proyecto también emplea técnicas de
**caching** mediante `lru_cache` para optimizar el rendimiento, evitando
lecturas repetidas de archivos de configuración.

### Asyncio y Playwright

La combinación de `asyncio` con Playwright representa el corazón de la
eficiencia del bot. Esta sinergia permite manejar múltiples tareas de manera no
bloqueante, escalando el número de "trabajadores" en función del hardware
disponible y las necesidades del proyecto.

### Gestión de Tareas y Errores

Una característica crucial es su robustez frente a errores y timeouts. El script
está diseñado para reintentar o pasar al siguiente documento automáticamente
ante cualquier fallo, asegurando un mínimo impacto en la productividad general
del bot.

## Conclusión

Este bot de scraping demuestra que, con las herramientas y enfoques adecuados,
es posible no solo extraer datos de sitios protegidos sino hacerlo de manera
eficiente y respetando las políticas de uso. A través de estrategias
inteligentes y una buena implementación técnica, los límites convencionales del
scraping pueden superarse.

Espero que este vistazo a mi aplicación les haya resultado informativo e
inspirador para sus propios proyectos de scraping.

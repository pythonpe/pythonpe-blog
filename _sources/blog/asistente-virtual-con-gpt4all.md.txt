---
blogpost: true
date: Feb 18, 2025
author: soloidx
location: Lima, Perú
category: Tutorial
tags: AI, chatbots, ollama, gpt4all, llm, llama, chat
language: Español
---

# Python y GPT4All, Creando tu asistente de IA personal con 5 líneas

Cuando buscamos tutoriales sobre asistentes virtuales, a menudo encontramos recursos que involucran integraciones con APIs externas como OpenAI, Claude o Gemini. Si bien estas soluciones son poderosas, nos enfrentamos a dos limitaciones significativas: la dependencia de una conexión a internet y los costos asociados con el uso de APIs de terceros. Es aquí donde herramientas como GPT4All y Ollama brillan, permitiéndonos ejecutar modelos de lenguaje directamente en nuestro hardware local, lo que no solo elimina la necesidad de una conexión constante a internet, sino que también nos libera de los costos recurrentes asociados con servicios en la nube, haciendo que la inteligencia artificial sea más accesible para desarrolladores, investigadores y entusiastas por igual.

![Python developer](/_static/images/gpt4all.png)

En este artículo haremos un breve cliente en Python para crear nuestro propio cliente utilizando GPT4All como herramienta principal.

## ¿Por qué no Ollama?:
Ollama es una herramienta poderosa, una de sus mayores ventajas es que podemos utilizar los modelos mas recientes pero tendríamos que lidiar con iniciar el servicio externo y comunicarnos por medio de la interfaz REST que provee esta herramienta.

GPT4All por otro lado nos permite usar la librería propia de Python para poder cargar el modelo e interactuar directamente con él de una forma mas sencilla.

## Mi primer chat con LLM:

Para comenzar crearemos un entorno virtual e instalaremos GPT4All:

```bash
python -m venv venv
source venv/bin/activate
pip install gpt4all
```

Con estas dependencias podremos empezar con nuestro código, en un archivo nuevo de Python (yo lo llamé chat.py) creamos estas líneas:

```python
from gpt4all import GPT4All

model = GPT4All("Llama-3.2-1B-Instruct-Q4_0.gguf")

with model.chat_session():
    respuesta = model.generate(
        "¿Cómo puedo implementar un algoritmo de ordenamiento rápido en Python? "
        "muestrame el codigo correspondiente.", max_tokens=1024)
    print(respuesta)
```

Después de descargar el modelo (toma unos minutos la primera vez) ya nos devuelve una respuesta:

```text
¡Claro! A continuación, te muestro una lista de algunos algoritmos de ordenamiento rápidos y su implementación en Python:

1. **Burbuja**: El algoritmo de burbuja es uno de los más simples y efectivos para ordenar un conjunto de elementos.
2. **Mercedón**: El mercedón es similar a la burbuja, pero utiliza una estructura de búsqueda de dos pointers que se mueven hacia adelante hasta encontrar el elemento correcto en el medio del arreglo.
3. **Búsqueda en lista**: La búsqueda en lista es un algoritmo simple y eficiente para ordenar un conjunto de elementos.
4. **Algoritmo de ordenamiento por toma a toma (QuickSort)**: El QuickSort es un algoritmo de ordenamiento que funciona como una mezcla, dividiendo el arreglo en dos partes hasta encontrar la posición correcta del elemento.

Aquí te muestro el código para cada uno de estos algoritmos:

**Burbuja**

def burbuja(arr):
    n = len(arr)

    for i in range(n-1):
        key = arr[i]
        j = i+1

        while j < n and arr[j] > key:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j += 1

        print("Arrango:", arr)

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(burbuja(arr))

[la respuesta sigue...]

**Algoritmo de ordenamiento por toma a toma (QuickSort)**

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print("Arrango:", arr)
    quicksort(left).extend(middle)
    quicksort(right)

arr = [64, 34, 25, 12, 22, 11, 90]
quicksort(arr)

Espero que esta muestra te haya ayudado a entender cómo implementar algunos algoritmos de ordenamiento rápidos en Python. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!
```

¡Y esto fue sencillo! Para terminar podemos hace una implementación mas elaborada con una interfaz en consola:

```python
from gpt4all import GPT4All

model = GPT4All("Llama-3.2-1B-Instruct-Q4_0.gguf")

print("Esperando mensaje, escriba 'salir' para terminar.")
with model.chat_session():
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == 'salir':
            print("Gracias por usar el chat. ¡Hasta luego!")
            break

        answer = model.generate(user_input, max_tokens=1024)
        print("AI:", answer)

```

Y con esto tenemos nuestro asistente de IA de bolsillo.

## Notas:
- Una de las desventajas de GPT4All es que no disponemos de todos los modelos disponibles en Hugging Face (a la fecha de este artículo intente correr deepseek-r1 pero me encontré con errores pendientes en nuevas releases)
- GPT4All ofrece algunas herramientas para hacer embeddings pero aun tiene ciertas limitaciones
- Encontré la lista de modelos disponibles desde el repositorio de [GPT4All-chat](https://github.com/nomic-ai/gpt4all/tree/29f29773af72abefd114f119a6632837263e1896/gpt4all-chat/metadata) no todos los modelos están soportados por la SDK de Python pero puedes ir viendo y probando el mejor modelo que se acomode a las especificaciones de tu ordenador.
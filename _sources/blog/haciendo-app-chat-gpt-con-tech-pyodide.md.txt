---
blogpost: true
date: Mar 12, 2025
author: hellhound
location: Lima, Perú
category: Tutorial
tags: pyodide, openai, gpt, httpx, python
language: Español
---
# Creación de una Aplicación de Chat Potenciada por Pyodide y GPT-3.5 Turbo: Una Prueba de Concepto

![OpenAI](/_static/images/openai.png){ align=center width=400px }

Construir una aplicación basada en la web que aproveche tanto el entorno de
Python como el modelo de lenguaje GPT-3.5 Turbo de OpenAI puede ser una empresa
emocionante. Este artículo explica la creación de una aplicación de chat como
prueba de concepto utilizando Pyodide, una herramienta que permite ejecutar
Python en el navegador web, e integrarla con GPT-3.5 Turbo para simular un
agente conversacional inteligente.

## El Panorama de la Integración entre Pyodide y GPT-3.5 Turbo

Con la capacidad de ejecutar Python directamente en los navegadores web, Pyodide
ofrece una oportunidad emocionante para llevar las capacidades poderosas de las
bibliotecas basadas en Python directamente a las aplicaciones del lado del
cliente. Esto incluye aplicaciones que pueden beneficiarse de estar cerca de los
usuarios, como herramientas interactivas y tableros de visualización de datos.

Esta prueba de concepto integra Pyodide con el modelo GPT-3.5 Turbo de OpenAI,
que proporciona la capacidad de simular una conversación similar a la humana. A
continuación, te guiaré a través de cada componente de esta aplicación,
explicando su funcionalidad, técnicas de integración y la razón detrás de
cada elección.

## Desglose de Componentes

La aplicación se compone de varios archivos clave y tecnologías, incluyendo
HTML, JavaScript y Python integrados a través de Pyodide. Vamos a desglosar
estos componentes paso a paso.

### HTML: Estructuración de la Interfaz

El archivo HTML configura la interfaz básica de usuario para la aplicación de
chat:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodide Chat App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: auto;
            padding: 20px;
        }
        #chatbox {
            border: 1px solid #ccc;
            height: 300px;
            overflow-y: scroll;
            padding: 10px;
            margin-bottom: 10px;
        }
        #user-input {
            width: calc(100% - 70px);
        }
        #send-button {
            width: 60px;
        }
    </style>
</head>
<body>

<!-- Pyodide setup logic will insert content here -->
<script src="https://cdn.jsdelivr.net/pyodide/v0.27.3/full/pyodide.js"></script>
<script src="python.js"></script>
</body>
</html>
```

Este diseño HTML crea una interfaz básica con un cuadro de chat y un control de
entrada de usuario, envuelto en CSS simple para estilizar la apariencia. La
configuración de Pyodide es gestionada por un archivo JavaScript que
exploraremos a continuación.

### JavaScript: Inicialización de Pyodide y Conexión del Frontend con el Backend

Se emplea JavaScript para configurar el entorno Pyodide y conectar la interfaz
de usuario del frontend con el backend de Python. Aquí está el archivo de
inicialización de JavaScript:

#### `python.js`

```javascript
async function setupPyodide() {
    const pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");

    // JavaScript functions to register with the Python environment
    const jsModule = {
        async displayResponse(response) {
            const chatbox = document.getElementById("chatbox");
            chatbox.innerHTML += `<div><strong>AI:</strong> ${response}</div>`;
        }
    };

    pyodide.registerJsModule("js_module", jsModule);

    await pyodide.runPythonAsync(`
        import micropip
        import os
        from pyodide.http import pyfetch

        response = await pyfetch("app.tar.gz")
        await response.unpack_archive()

        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/multidict/multidict-4.7.6-py3-none-any.whl', keep_going=True)
        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/frozenlist/frozenlist-1.4.0-py3-none-any.whl', keep_going=True)
        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/aiohttp/aiohttp-4.0.0a2.dev0-py3-none-any.whl', keep_going=True)
        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/openai/openai-1.3.7-py3-none-any.whl', keep_going=True)
        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/urllib3/urllib3-2.1.0-py3-none-any.whl', keep_going=True)
        await micropip.install("ssl")
        import ssl
        await micropip.install("httpx", keep_going=True)
        import httpx
        await micropip.install('https://raw.githubusercontent.com/psymbio/pyodide_wheels/main/urllib3/urllib3-2.1.0-py3-none-any.whl', keep_going=True)
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        from main import sender_message_proxy
    `);
    
    // Prompt the user for the OpenAI API key
    const apiKey = window.prompt("Please enter your OpenAI API key:");

    // Add the HTML content after Pyodide setup.
    document.body.innerHTML += `
        <h1>Pyodide Chat with AI Assistant</h1>
        <div id="chatbox"></div>
        <input type="text" id="user-input" placeholder="Type your message...">
        <button id="send-button">Send</button>
    `;

    const sendMessageToPython = pyodide.globals.get("sender_message_proxy");

    // Add event listener to send button
    document.getElementById("send-button").addEventListener("click", () => {
        const userInput = document.getElementById("user-input").value;
        document.getElementById("user-input").value = "";
        const chatbox = document.getElementById("chatbox");
        chatbox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

        sendMessageToPython(apiKey, userInput);
    });

    // Add event listener for the Enter key on the input field
    document.getElementById("user-input").addEventListener("keypress", (event) => {
        if (event.key === "Enter") {
            document.getElementById("send-button").click();
        }
    });

    await pyodide.runPythonAsync(`
        from main import main as py_main

        await py_main()
    `);
}

document.addEventListener("DOMContentLoaded", function() {
    setupPyodide();
});
```

#### Aspectos Clave del Código JavaScript

- **Inicialización de Pyodide**: El script inicializa el entorno de Pyodide y
  asegura que los paquetes de Python necesarios estén disponibles a través de
`micropip`.

- **Solicitud de la Clave API**: Para asegurar la interacción con GPT-3.5
  Turbo, se requiere una clave API. Esto se obtiene a través de un aviso del
navegador cuando la aplicación se carga por primera vez.

- **Interoperabilidad JavaScript-Python**: Usando `pyodide.registerJsModule`,
  creamos un puente entre JavaScript y Python. Esto permite que Python llame a
una función de JavaScript (`displayResponse`), que actualiza el cuadro de chat
con las respuestas de GPT-3.5 Turbo.

- **Carga de la Lógica del Backend**: La lógica del backend se encapsula en
  Python e integra a través de `pyodide.runPythonAsync`. Esto permite que los
módulos definidos en Python sean transparentes para JavaScript como funciones
sincrónicas.

### Python: Manejo de Conversaciones con GPT-3.5 Turbo

El corazón de la aplicación involucra una serie de componentes de Python que
gestionan la comunicación con la API de OpenAI:

#### Backend de Python (`main.py`)

```python
import asyncio
import json
from urllib.parse import quote_plus

import httpx
import openai
from pyodide.ffi import create_proxy
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import js_module


class URLLib3Transport(httpx.AsyncBaseTransport):
    def __init__(self) -> None:
        self.pool = urllib3.PoolManager()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        payload = json.loads(request.content.decode("utf-8").replace("'", '"'))
        urllib3_response = self.pool.request(
            request.method,
            str(request.url),
            headers=request.headers,
            json=payload,
        )
        content = json.loads(
            urllib3_response.data.decode("utf-8")
        )
        stream = httpx.ByteStream(
            json.dumps(content).encode("utf-8")
        )
        headers = [(b"content-type", b"application/json")]
        return httpx.Response(200, headers=headers, stream=stream)


client: httpx.AsyncClient = httpx.AsyncClient(transport=URLLib3Transport())
openai_client: openai.AsyncOpenAI = openai.AsyncOpenAI(
    base_url="https://api.openai.com/v1/", api_key="", http_client=client
)
message_queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()
loop: asyncio.AbstractEventLoop | None = None


async def handle_message(api_key: str, message: str) -> None:
    openai_client.api_key = api_key
    response = await openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": quote_plus(message),
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=4096,
        temperature=0.2,
    )
    await js_module.displayResponse(response.choices[0].message.content)


async def receiver() -> None:
    while True:
        api_key, message = await message_queue.get()
        await handle_message(api_key, message)


def sender(api_key: str, message: str) -> None:
    message_queue.put_nowait((api_key, message))


async def main() -> None:
    global loop

    loop = asyncio.get_running_loop()
    loop.create_task(receiver())
    while True:
        await asyncio.sleep(0.1)


sender_message_proxy = create_proxy(sender)
```

#### Funcionalidad Principal

- **Capa de Transporte Personalizada**: Una clase `URLLib3Transport`
  personalizada implementa `httpx.AsyncBaseTransport` para manejar solicitudes
de red sin depender de la API fetch nativa de JavaScript. Esta capa permite una
gestión flexible de solicitudes HTTP, incluyendo lógica de reintento y
gestión de sesiones.

- **Bucle de Eventos Asíncrono**: Al utilizar `asyncio`, la aplicación puede
  gestionar tareas asíncronas de manera eficiente, asegurando que la
aplicación siga siendo receptiva, incluso cuando se trata de interacciones
lentas de red.

- **Manejo de Mensajes**: La función `handle_message` gestiona la interacción
  con la API de OpenAI. Construye una solicitud usando la entrada del usuario,
la envía a GPT-3.5 Turbo, y devuelve la respuesta de la IA al frontend a
través de la función `displayResponse` proporcionada en `js_module`.

- **Conexión con JavaScript**: El `sender_message_proxy` es un puente
  proporcionado por Pyodide que permite que JavaScript encole mensajes para ser
procesados por el bucle de eventos de Python.

### Razonamiento y Alternativas

- **URLLib3Transport**: La elección de usar un transporte personalizado en
  lugar de clientes HTTP de nivel superior como `requests` se vuelve necesaria
debido a las limitaciones de Pyodide con las solicitudes de red, como en la
[solución del problema en
GitHub](https://github.com/pyodide/pyodide/issues/4292#issuecomment-1848861037).
Esta solución permite mayor flexibilidad y compatibilidad dentro del entorno
web en el que opera Pyodide.

- **Diseño de la Interfaz Interactiva**: Aunque la interfaz de usuario permanece
  minimalista en esta prueba de concepto, cumple con los objetivos actuales
mientras deja espacio para mejorar con interacciones más ricas, estilo o
soporte multicliente.

### Desafíos y Consideraciones

Construir esta aplicación presenta un conjunto único de desafíos:
- **Seguridad**: Gestionar una clave API dentro de una aplicación del lado del
  cliente plantea riesgos de seguridad. Los usuarios deben ser cautelosos y,
potencialmente, emplear proxies del lado del servidor para cualquier
implementación en vivo.

- **Rendimiento**: Las limitaciones del navegador y el estado alfa de Pyodide
  implican restricciones de rendimiento. Es aconsejable que esto permanezca en
estado de prueba de concepto pendiente una mayor optimización.

- **Sobrecarga de Instalación**: La necesidad de empaquetar archivos en formato
  wheel de Python hace que el proceso de carga inicial sea pesado. Se podrían
explorar técnicas para simplificar la entrega de paquetes a los clientes.

## Conclusión

La aplicación descrita aquí demuestra las posibilidades de combinar Pyodide y
GPT-3 en un entorno basado en la web, ofreciendo una interfaz interactiva para
experimentar con capacidades de IA. Aunque sigue siendo una prueba de concepto,
abre la puerta a futuras iteraciones hacia una aplicación robusta y lista para
producción.

```{note}

Puedes encontrar el código completo aquí: https://github.com/jpchauvel/pyodide-chat-gpt

[¡Pruébalo ahora!](https://chauvel.org/blog/pyodide-chat-gpt/)

```

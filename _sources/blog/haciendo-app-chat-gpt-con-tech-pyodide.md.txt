---
blogpost: true
date: May 13, 2026
author: hellhound
location: Lima, Perú
category: Tutorial
tags: pyodide, openai, gpt, httpx, python
language: Español
---
# Creación de una Aplicación de Chat Potenciada por Pyodide y GPT-5.4-mini: Una Prueba de Concepto

![OpenAI](/_static/images/openai.png){ align=center width=400px }

Construir una aplicación basada en la web que aproveche tanto el entorno de
Python como el modelo de lenguaje GPT-5.4-mini de OpenAI puede ser una empresa
emocionante. Este artículo explica la creación de una aplicación de chat como
prueba de concepto utilizando Pyodide, una herramienta que permite ejecutar
Python en el navegador web, e integrarla con GPT-5.4-mini para simular un
agente conversacional inteligente.

## El Panorama de la Integración entre Pyodide y GPT-5.4-mini

Con la capacidad de ejecutar Python directamente en los navegadores web, Pyodide
ofrece una oportunidad emocionante para llevar las capacidades poderosas de las
bibliotecas basadas en Python directamente a las aplicaciones del lado del
cliente. Esto incluye aplicaciones que pueden beneficiarse de estar cerca de los
usuarios, como herramientas interactivas y tableros de visualización de datos.

Esta prueba de concepto integra Pyodide con el modelo GPT-5.4-mini de OpenAI,
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
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            max-width: 640px;
            margin: 2rem auto;
            padding: 0 1rem;
            color: #1a1a1a;
        }
        h1 {
            font-size: 1.4rem;
            margin-bottom: 0.25rem;
        }
        #subtitle {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        #status {
            padding: 0.6rem 0.8rem;
            background: #f4f4f7;
            border: 1px solid #e0e0e6;
            border-radius: 6px;
            font-size: 0.9rem;
            color: #444;
            margin-bottom: 1rem;
        }
        #chatbox {
            border: 1px solid #d0d0d6;
            border-radius: 6px;
            height: 360px;
            overflow-y: auto;
            padding: 0.75rem;
            margin-bottom: 0.75rem;
            background: #fff;
        }
        .msg {
            padding: 0.5rem 0.75rem;
            margin-bottom: 0.5rem;
            border-radius: 6px;
            line-height: 1.4;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .msg.you {
            background: #e8f0ff;
            border-left: 3px solid #4a7dff;
        }
        .msg.ai {
            background: #f4f4f7;
            border-left: 3px solid #888;
        }
        .msg.err {
            background: #fdecea;
            border-left: 3px solid #d33;
            color: #8a1c1c;
        }
        #input-row {
            display: flex;
            gap: 0.5rem;
        }
        #user-input {
            flex: 1;
            padding: 0.5rem 0.75rem;
            border: 1px solid #d0d0d6;
            border-radius: 6px;
            font-size: 1rem;
        }
        #send-button {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 6px;
            background: #4a7dff;
            color: white;
            font-size: 1rem;
            cursor: pointer;
        }
        #send-button:disabled {
            background: #aac;
            cursor: not-allowed;
        }
    </style>
</head>
<body>

<h1>Pyodide Chat</h1>
<div id="subtitle">Python (via Pyodide) + OpenRouter, all in your browser.</div>

<div id="status">Initializing…</div>

<div id="app" hidden>
    <div id="chatbox"></div>
    <div id="input-row">
        <input id="user-input" type="text" placeholder="Type a message and press Enter…" autocomplete="off" />
        <button id="send-button">Send</button>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/pyodide/v0.29.4/full/pyodide.js"></script>
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
    const status = document.getElementById("status");
    const setStatus = (msg) => { if (status) status.textContent = msg; };

    setStatus("Loading Pyodide…");
    const pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.29.4/full/",
    });

    setStatus("Loading Python packages (openai, httpx, ssl)…");
    await pyodide.loadPackage(["openai", "httpx", "ssl"]);

    const jsModule = {
        async displayResponse(response) {
            const chatbox = document.getElementById("chatbox");
            const div = document.createElement("div");
            div.className = "msg ai";
            div.innerHTML = `<strong>AI:</strong> `;
            div.appendChild(document.createTextNode(response));
            chatbox.appendChild(div);
            chatbox.scrollTop = chatbox.scrollHeight;
            setSending(false);
        },
        async displayError(message) {
            const chatbox = document.getElementById("chatbox");
            const div = document.createElement("div");
            div.className = "msg err";
            div.innerHTML = `<strong>Error:</strong> `;
            div.appendChild(document.createTextNode(message));
            chatbox.appendChild(div);
            chatbox.scrollTop = chatbox.scrollHeight;
            setSending(false);
        },
    };
    pyodide.registerJsModule("js_module", jsModule);

    setStatus("Fetching app bundle…");
    await pyodide.runPythonAsync(`
        from pyodide.http import pyfetch
        response = await pyfetch("build/app.tar.gz")
        await response.unpack_archive()
        from main import sender_message_proxy
    `);

    const apiKey = window.prompt("Please enter your OpenRouter API key:");
    if (!apiKey) {
        setStatus("No API key provided. Reload to try again.");
        return;
    }

    setStatus("Ready.");
    document.getElementById("app").hidden = false;

    const sendMessageToPython = pyodide.globals.get("sender_message_proxy");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function setSending(isSending) {
        sendButton.disabled = isSending;
        userInput.disabled = isSending;
        sendButton.textContent = isSending ? "…" : "Send";
        if (!isSending) userInput.focus();
    }

    function send() {
        const text = userInput.value.trim();
        if (!text) return;
        userInput.value = "";

        const chatbox = document.getElementById("chatbox");
        const div = document.createElement("div");
        div.className = "msg you";
        div.innerHTML = `<strong>You:</strong> `;
        div.appendChild(document.createTextNode(text));
        chatbox.appendChild(div);
        chatbox.scrollTop = chatbox.scrollHeight;

        setSending(true);
        sendMessageToPython(apiKey, text);
    }

    sendButton.addEventListener("click", send);
    userInput.addEventListener("keypress", (event) => {
        if (event.key === "Enter") send();
    });
    userInput.focus();

    pyodide.runPythonAsync(`
        from main import main as py_main
        await py_main()
    `);
}

document.addEventListener("DOMContentLoaded", setupPyodide);
```

#### Aspectos Clave del Código JavaScript

- **Inicialización de Pyodide**: El script inicializa el entorno de Pyodide y
  asegura que los paquetes de Python necesarios estén disponibles a través de
`micropip`.

- **Solicitud de la Clave API**: Para asegurar la interacción con GPT-5.4-mini,
se requiere una clave API. Esto se obtiene a través de un aviso del
navegador cuando la aplicación se carga por primera vez.

- **Interoperabilidad JavaScript-Python**: Usando `pyodide.registerJsModule`,
  creamos un puente entre JavaScript y Python. Esto permite que Python llame a
una función de JavaScript (`displayResponse`), que actualiza el cuadro de chat
con las respuestas de GPT-5.4-mini.

- **Carga de la Lógica del Backend**: La lógica del backend se encapsula en
  Python e integra a través de `pyodide.runPythonAsync`. Esto permite que los
módulos definidos en Python sean transparentes para JavaScript como funciones
sincrónicas.

### Python: Manejo de Conversaciones con GPT-5.4-mini

El corazón de la aplicación involucra una serie de componentes de Python que
gestionan la comunicación con la API de OpenAI:

#### Backend de Python (`main.py`)

```python
"""Pyodide-side chat backend.

Runs inside the browser via Pyodide (WASM). Modern Pyodide (>= 0.27.2) ships
`openai`, `httpx`, and `urllib3` as bundled packages with built-in
Emscripten/Fetch transports, so no custom HTTP transport is needed anymore.
"""

import asyncio

import httpx
import openai
from pyodide.ffi import create_proxy

import js_module

MODEL = "openai/gpt-5.4-mini"
SYSTEM_PROMPT = (
    "You are a concise, friendly assistant running inside a Pyodide-powered "
    "browser chat. Keep answers short unless the user asks for detail."
)

# OpenRouter's CORS preflight rejects the openai SDK's auto-injected
# x-stainless-* headers. Strip them with an httpx request hook before send.
_STAINLESS_HEADERS = {
    "x-stainless-lang",
    "x-stainless-package-version",
    "x-stainless-os",
    "x-stainless-arch",
    "x-stainless-runtime",
    "x-stainless-runtime-version",
    "x-stainless-async",
    "x-stainless-retry-count",
    "x-stainless-read-timeout",
}


async def _strip_stainless(request: httpx.Request) -> None:
    request.headers = httpx.Headers(
        {k: v for k, v in request.headers.items() if k.lower() not in _STAINLESS_HEADERS}
    )


_http_client = httpx.AsyncClient(event_hooks={"request": [_strip_stainless]})

openai_client: openai.AsyncOpenAI = openai.AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="placeholder",
    http_client=_http_client,
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "Pyodide Chat GPT2",
    },
)

history: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]

message_queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()
loop: asyncio.AbstractEventLoop | None = None


async def handle_message(api_key: str, message: str) -> None:
    openai_client.api_key = api_key
    history.append({"role": "user", "content": message})
    try:
        response = await openai_client.chat.completions.create(
            model=MODEL,
            messages=history,
            max_completion_tokens=1024,
            temperature=0.2,
        )
        reply = response.choices[0].message.content or ""
        history.append({"role": "assistant", "content": reply})
        await js_module.displayResponse(reply)
    except Exception as exc:
        # Roll back the just-appended user turn so a retry doesn't duplicate it.
        if history and history[-1].get("role") == "user":
            history.pop()
        await js_module.displayError(f"{type(exc).__name__}: {exc}")


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
la envía a GPT-5.4-mini, y devuelve la respuesta de la IA al frontend a
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

Puedes encontrar el código completo aquí: https://github.com/jpchauvel/pyodide-chat-gpt2
(Con este código, puedes probarlo con tokens de OpenRouter).

[¡Pruébalo ahora!](https://chauvel.org/blog/pyodide-chat-gpt/)
(Necesitas un token de OpenAI)
```

---
blogpost: true
date: 08 Apr, 2024
author: hellhound
location: Lima, Perú
category: JupyterLite
tags: jupyterlite, sphinx
language: Español
---

# Explorando JupyterLite e integrándolo en tu blog de Sphinx

![JupyterLite](/_static/images/jupyterlite.png){ height=300px align=center }

## Introducción

Como desarrollador y entusiasta de data, siempre me encuentro explorando nuevas
tecnologías y herramientas para mejorar mis proyectos y documentación.
Recientemente, mi curiosidad me llevó a descubrir JupyterLite, una
implementación ligera de JupyterLab que se ejecuta completamente en el navegador
sin necesidad de un servidor. Intrigado por sus capacidades, decidí experimentar
con la integración de JupyterLite en mi blog de Sphinx utilizando la extensión
jupyterlite-sphinx. En esta publicación, compartiré mi experiencia de integrar
JupyterLite en mi documentación y los pasos que tomé para hacer que funcione sin
problemas con mi blog construido con Sphinx.

## Instalación y configuración

El primer paso para integrar JupyterLite en tu documentación de Sphinx es
instalar el paquete `jupyterlite-sphinx`. Puedes hacer esto fácilmente usando
pip:

```sh
pip install jupyterlite-sphinx
```

Después de instalar la extensión, necesitas agregarla a la lista de extensiones
en el archivo `conf.py` de tu proyecto de Sphinx:

```sh
extensions = [
    'jupyterlite_sphinx',
    # Otras extensiones de Sphinx
    # ...
]
```

Una vez que hayas agregado la extensión, JupyterLite debería aparecer
automáticamente en tu documentación en línea. Para previsualizarlo localmente,
puedes navegar al directorio de construcción (por ejemplo, `_build/html`) y
usar el servidor HTTP incorporado de Python para servir el sitio:

```sh
python -m http.server
```

Por defecto, jupyterlite-sphinx no instala un kernel de Python. Si quieres
tener un kernel de Python disponible en tu documentación, puedes instalar ya sea
`jupyterlite-pyodide-kernel` o `jupyterlite-xeus` con pip:

```sh
pip install jupyterlite-pyodide-kernel
```

## Configuración

JupyterLite-sphinx proporciona varias opciones de configuración que te permiten
personalizar cómo se comporta JupyterLite en tu documentación. Puedes incrustar
contenido personalizado, como cuadernos y archivos de datos, en tu construcción
de JupyterLite especificando la variable `jupyterlite_contents` en tu archivo
`conf.py`:

```python
jupyterlite_contents = ["./lugar/donde/estan/los/notebooks/", "mi_otro_notebook.ipynb"]
```

Si quieres cambiar el directorio de construcción predeterminado desde el
directorio `docs`, puedes especificar un directorio personalizado usando la
variable `jupyterlite_dir`:

```python
jupyterlite_dir = "/lugar/donde/esta/el/directorio/lite"
```

Para preinstalar paquetes de Python en el entorno del kernel, puedes usar
`jupyterlite-pyodide` con el kernel `pyodide-python`. Puedes definir las
dependencias en un archivo `environment.yml` en tu directorio de documentos:

```yaml
name: pyodide-python-kernel
channels:
  - https://repo.mamba.pm/emscripten-forge
  - https://repo.mamba.pm/conda-forge
dependencies:
  - numpy
  - matplotlib
  - ipycanvas
```

Además, jupyterlite-sphinx proporciona una directiva `replite` de Sphinx que
te permite incrustar una consola REPLite en tu documentación. Esta directiva
acepta varias opciones, incluyendo el tipo de kernel, altura, texto del prompt y
color del prompt:

```rst
.. replite::
   :kernel: python
   :height: 600px
   :prompt: ¡Prueba Replite!
   :prompt_color: #dc3545

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2 * np.pi, 200)
   y = np.sin(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)
   plt.show()
```

## Conclusión

En conclusión, experimentar con JupyterLite e integrarlo en mi blog de Sphinx
usando la extensión jupyterlite-sphinx ha sido una experiencia gratificante.
La capacidad de integrar de manera fluida notebooks interactivos de Jupyter y
consolas REPL en mi documentación ha añadido un nuevo nivel de interactividad y
compromiso para mis lectores. Siguiendo los pasos de instalación y las opciones
de configuración proporcionadas por jupyterlite-sphinx, es fácil mejorar tu blog
construido con Sphinx con las características de JupyterLite. Espero con ansias
explorar aún más las posibilidades que JupyterLite abre para crear experiencias
de documentación dinámicas e interactivas.

Blog post origingal en [https://www.chauvel.org/blog/embedding-jupyterlite-in-sphinx/](https://www.chauvel.org/blog/embedding-jupyterlite-in-sphinx/).

---
blogpost: true
date: Apr 4, 2024
author: hellhound
location: Lima, Perú
category: Tutorial
tags: tutorial, git, pull-request, ablog, sphinx
language: Español
---

# Cómo Redactar Posts en el Blog de Python Perú y no Morir en el Intento

Debo iniciar las líneas de este post dándoles la bienvenida a la comunidad de
Python Perú y a este Blog que marca el inicio de una nueva etapa de la
comunidad.

![Python Perú Logo](/_static/logo/logo.svg){.markdown-body width=200px align=center}

```{admonition} Repositorio de GitHub
:class: sidebar note
[https://github.com/pythonpe/pythonpe-blog](https://github.com/pythonpe/pythonpe-blog)
```

Cómo lo indicamos en la página [Acerca de Python Perú](/about.md), cualquier
persona que esté interesada en publicar a través de nosotros un post sobre
temas relacionados al lenguaje Python como pueden ser Meetups, la propia Pycon
Perú o bien sobre herramientas y frameworks que utilicen el lenguaje Python,
son bienvenidos a publicar en este Blog.


## Clonar el Repositorio de GitHub del Blog de Python Perú

Ahora, para poder escribir un post, lo primero que debes hacer es clonar
el repositorio del Blog que está alojado en GitHub.

```{admonition} Nota
Todas las operaciones que usemos en este tutorial emplearán el comando `gh`
por lo que te *recomendamos* descargarlo. [Link aquí](https://cli.github.com)
```

Cómo muestra la imágen (marcado en elípsis de color rojo), debes copiar el
comando de GitHub CLI y luego ejecutarlo en la terminal.

![Clone GitHub repo](/_static/images/clone-github-repo.png)


```{admonition} Nota
Si bien es cierto este tutorial recomienda el empleo de `gh` para poder hacer
todas las operaciones hasta que crees el Pull Request de GitHub, no
mencionaremos como configurarlo o como autenticarte ante GitHub usando ese
comando. Si deseas saber cómo autenticarte, pueder revisar la ayuda de la
línea de comandos de `gh` ejecutando: `gh auth login --help`.
```


## Crear el Branch Donde Irán tus Cambios

Ahora que has clonado el repositorio, debes crear un branch donde irán
tus cambios y por su puesto tu nuevo post.

En la terminal, ejecuta el siguiente comando:

```sh
git checkout -b el-nombre-de-tu-branch main
```

Debes reemplazar `el-nombre-de-tu-branch` por un nombre de branch. No tienes
que preocuparte demasiado por pensar en un nombre creativo. Un ejemplo podría
ser el nombre del post separado por guiones. Otro podría ser tu nickname.

```{admonition} Nota
Si bien es cierto se menciona la utilización del comando `git`, se sobrentiende 
que debe estar instalado en tu sistema ya que estamos utilizando GitHub. También
se asume que debes tener una cuenta de GitHub creada. Además, aunque este post 
explica el flujo que debes seguir para crear un post, no es exhaustivo en como 
debes usar `git` u otras herramientas.
```


## Firma de Autor

Este paso es escencial y preliminar a la edición de un post si es tu primera
vez posteando en este Blog. Debes editar el archivo `AUTHORS` que se encuentra
en la raíz del proyecto y poner tu nombre, tu nickname (este lo utilizarás para
firmar los posts) y tu email.

Añade una línea al final del archivo con la siguiente nomenclatura:

`Joe Doe(nickname) <joe.doe@example.com>`

Donde Joe Doe lo reemplazas por tus nombres y apellido, nickname será la "chapa"
que usas o por la que te conocen o te conocemos. joe.doe@example.com lo
reemplazas por tu dirección de correo electrónico.


## Creación del Post 

Ahora ya tienes todo preparado para iniciar la edición de tu Post. Pero
existen ciertos pasos que debes seguir (que son opcionales) en caso de que
desees correr el Blog localmente y ver como luciría tu post si estuviese
publicado en el Blog.

El post deberá estar en formato Markdown y deberá estar ubicado en el
directorio `blog/`. La extensión del mismo será `.md`. Es texto plano, solo
que Markdown utiliza una sintáxis especial para darle formato a la hora de
mostrarlo en el explorador.

El nombre del archivo deberá seguir esta nomenclatura:

`nombre-del-post-de-manera-abreviada.md`

```{admonition} Nota
Puedes referirte a esta guía en Español de Markdown para informarte más
sobre la sintáxis de este formato. [Link aquí](https://datosgobar.github.io/portal-andino/markdown-guide/)
```

¡Ojo! Debes iniciar tus posts con lo siguiente en Markdown:

```markdown
---
blogpost: true
date: Apr 4, 2024
author: nickname
location: Lima, Perú
category: Tutorial
tags: tag1, tag2, tag3
language: Español
---
```

Donde `blogpost` siempre será `true`. `date` tiene que tener ese formato de
fecha, lamentamentablemente tiene que ser escrita en inglés. Se escribe de la 
siguiente manera:

`Mes día, año`

El mes puede ser uno de los siguientes:

- Jan: Enero
- Feb: Febrero
- Mar: Marzo
- Apr: Abril
- Jun: Junio
- Jul: Julio
- Aug: Agosto
- Sep: Setiembre
- Oct: Octubre
- Nov: Noviembre
- Dec: Diciembre

`tags` tiene que ser una lista de etiquetas separadas por comas. si tienes una
etiqueta que está comprendida por más de una palabra, únelas con guiones.

`category` es el nombre de la categoría del post. Puede ser cualquier cosa
que se te ocurra, mientras corresponda a lo que redactaste en el post,  y
puede estar comprendido por palabras separadas por espacios en blanco.

`language` siempre será "Español". Esto es debatible pero el público objetivo
del Blog es hispanoparlante en su mayoría. Así que es obligatorio redactar en
Español los posts.


## Instalación Local del Blog y Ejecución del Mismo (Opcional)

### Instalación

1. Instalemos poetry:

```sh
pip install -U poetry
```

2. Estando en la raíz del repositorio, instalemos las dependencias del Blog:

```sh
poetry install
```

### Construcción de las Páginas HTML

Estando en la raíz del repositorio:

```sh
poetry run ablog build
```

### Ejecución del Blog

Estando en la raíz del repositorio:

```sh
poetry run ablog serve
```

```{admonition} Nota
Se sobrentiende que debe estar instalado en el sistema `pip` y `python` en su
versión 3.12 como mínimo.
```


## Creación del Pull Request

Finalmente ya tienes tu post listo y deseas crear el pull request para ser
revisado por {ref}`author-soloidx`, {ref}`author-hellhound` o {ref}`author-nefi`.

Lo primero que debes hacer es avisar a {ref}`author-soloidx`, 
{ref}`author-hellhound` o {ref}`author-nefi` sobre la redacción de tu post en el
grupo de [WhatsApp](https://chat.whatsapp.com/D9bPvUrddvSBUIkMSoTqrk).

Una vez conseguida la autorización y que te hayan incluido al grupo de bloggers 
de la organización Python Perú en GitHub, lo que debes hacer es ejecutar el
siguiente comando especificando un título para tu PR y un cuerpo para el mismo.
Ssi no deseas poner un cuerpo solo obvia esa opción.

```sh
gh pr create --title "Aquí iría tu título del PR" --body "Aquí el cuerpo de tu PR"
```

Recuerda que siempre debes ejecutar este comando cerciorándote de que estés en
tu branch. Si no estás en tu branch siempre puedes cambiarte de branch usando
este comando:

```sh
git checkout tu-branch
```

Una vez ejecutado el comando `gh` y siguiendo las indicaciones del mismo ¡Abrás
creado satisfactoriamente el PR! Debes comunicar de su creación de inmediato
a  {ref}`author-soloidx`, {ref}`author-hellhound` o {ref}`author-nefi` en el
grupo de [WhatsApp](https://chat.whatsapp.com/D9bPvUrddvSBUIkMSoTqrk) para que
revisen tus cambios en el pull request y subsecuentemente hagan merge de estos
en la rama `main`.


Puedes ver tu PR creado yendo a [https://github.com/pythonpe/pythonpe-blog](https://github.com/pythonpe/pythonpe-blog)
y luego seleccionando el tab "Pull Requests" como muestra en la imágen.

![Pull Requests](/_static/images/pull-requests-github.png)

¡Y listo! Ya publicaste tu primer post.

```{admonition} Nota
Nuevo post que explica como hacer lo mismo pero con forks [aquí](/blog/como-redactar-posts-con-fork.md)
```

---
blogpost: true
date: Apr 14, 2024
author: hellhound
location: Lima, Perú
category: Tutorial
tags: tutorial, git, fork, pull-request, ablog, sphinx
language: Español
---

# Cómo Hacer Fork y Pull Request en el Blog de Python Perú

Bienvenidos a la comunidad de Python Perú y a este Blog que marca el inicio de
una nueva etapa de la comunidad.

![Python Perú Logo](/_static/logo/logo.svg){.markdown-body width=200px align=center}

```{admonition} Repositorio de GitHub
:class: sidebar note
[https://github.com/pythonpe/pythonpe-blog](https://github.com/pythonpe/pythonpe-blog)
```

En este tutorial, te enseñaremos cómo hacer un fork del repositorio del Blog de
Python Perú y luego crear un pull request.

## Hacer Fork del Repositorio de GitHub del Blog de Python Perú

Primero, debes hacer un fork del repositorio del Blog que está alojado en
GitHub. Para hacer esto, ve al repositorio y haz clic en el botón "Fork" en la
parte superior derecha de la página.

![Fork GitHub repo](/_static/images/fork-github-repo.png)
![Create GitHub fork](/_static/images/create-github-fork.png)

Una vez que hayas hecho el fork, tendrás tu propia copia del repositorio en tu
cuenta de GitHub.

## Clonar el Repositorio de GitHub del Blog de Python Perú

Ahora, para poder escribir un post, lo primero que debes hacer es clonar el
repositorio del Blog que está alojado en tu cuenta de GitHub.

```{admonition} Nota
Todas las operaciones que usemos en este tutorial emplearán el comando `gh`
por lo que te *recomendamos* descargarlo. [Link aquí](https://cli.github.com)
```

Cómo muestra la imágen (marcado en elípsis de color rojo), debes copiar el
comando de GitHub CLI y luego ejecutarlo en la terminal.

![Clone GitHub repo](/_static/images/clone-github-repo.png)

## Crear el Branch Donde Irán tus Cambios

Ahora que has clonado el repositorio, debes crear un branch donde irán tus
cambios y por su puesto tu nuevo post.

En la terminal, ejecuta el siguiente comando:

```sh
git checkout -b el-nombre-de-tu-branch main
```

Debes reemplazar `el-nombre-de-tu-branch` por un nombre de branch. No tienes que
preocuparte demasiado por pensar en un nombre creativo. Un ejemplo podría ser el
nombre del post separado por guiones. Otro podría ser tu nickname.

## Creación del Post 

Sigue las instrucciones en el [post original](/blog/como-redactar-posts.md)
para crear tu post.

## Creación del Pull Request

Finalmente ya tienes tu post listo y deseas crear el pull request para ser
revisado por {ref}`author-soloidx`, {ref}`author-hellhound` o
{ref}`author-nefi`.

Lo primero que debes hacer es avisar a {ref}`author-soloidx`,
{ref}`author-hellhound` o {ref}`author-nefi` sobre la redacción de tu post en el
grupo de [WhatsApp](https://chat.whatsapp.com/D9bPvUrddvSBUIkMSoTqrk).

Una vez conseguida la autorización y que te hayan incluido al grupo de bloggers
de la organización Python Perú en GitHub, lo que debes hacer es ejecutar el
siguiente comando especificando un título para tu PR y un cuerpo para el mismo.
Si no deseas poner un cuerpo solo obvia esa opción.

Debes incluir la opción `--web` para abrir el PR en el navegador y poder
seleccionar el destino del PR (el destino será "python.pe/pythone-blog").

```sh
gh pr create --title "Aquí iría tu título del PR" --body "Aquí el cuerpo de tu PR" --web
```

```{admonition} Nota
Recuerda que siempre debes ejecutar este comando cerciorándote de que estés en
tu branch. Si no estás en tu branch siempre puedes cambiarte de branch usando
este comando:
```

```sh
git checkout tu-branch
```

![Compare across forks](/_static/images/compare-across-forks.png)
![Selecting fork origin](/_static/images/selecting-fork-origin.png)


Una vez ejecutado el comando `gh` y siguiendo las indicaciones del mismo ¡Abrás
creado satisfactoriamente el PR! Debes comunicar de su creación de inmediato a 
{ref}`author-soloidx`, {ref}`author-hellhound` o {ref}`author-nefi` en el grupo
de [WhatsApp](https://chat.whatsapp.com/D9bPvUrddvSBUIkMSoTqrk) para que revisen
tus cambios en el pull request y subsecuentemente hagan merge de estos en la rama
`main`.

---
blogpost: true
date: Jul 01, 2024
author: Less
location: Paipa, Colombia
category: Tutorial
tags: flet, flutter, python, app, multiplatform, python-flutter
language: Español
---

<p align="center">
    <img src="https://github.com/Less-dev/gitLearn/assets/166412593/ab475342-26b4-431e-9aae-f302e0f3fc57"
width="1000" height="300">
</p>


# Desarrollando una pequeña aplicación con flet
<p align="center">
    <img src="https://github.com/Less-dev/gitLearn/assets/166412593/3f8dd67d-23c3-490e-b8de-16018a562b75" width="150">
</p>


<h3 align="center"> Más que un framework</h3>


<p align="center">
<img src="https://user-images.githubusercontent.com/74038190/212744287-14f66c13-5458-40dc-9244-8ff533fc8f4a.gif" width="1000">
</p>

1. [`Qué es flet`](#que-es-flet)
  
   1.1 [Por qué usar flet](#por-que-usar-flet)
    
   1.2 [Configuración de nuestro entorno de desarrollo](#configuracion-de-nuestro-entorno-de-desarrollo)

2. [`Conceptos Básicos de flet`](#conceptos-basicos-de-flet)
   
   2.1[Primera aplicación con flet](#primera-aplicacion-con-flet)

3.[Conclusión](#conclusion)

<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="1000">
</p>

# Que es flet
  ### **[Flet](https://flet.dev/docs/) es un framework de desarrollo de aplicaciones multiplataforma que utiliza Python. Te permite crear aplicaciones web, de escritorio y móviles sin necesidad de experiencia previa en desarrollo frontend.**

### **Piensa en [Flet](https://flet.dev/docs/) como una herramienta que te facilita la construcción de interfaces de usuario (UI) atractivas y funcionales para tus aplicaciones.  Flet se encarga de la parte visual de la aplicación, mientras que tú te concentras en la lógica y funcionalidad usando código Python.**

<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000" height="2">
</p>

# Por que usar flet

  ### 1.  Si conoces Python, puedes comenzar a usar Flet de inmediato. No necesitas aprender lenguajes web como HTML, CSS o JavaScript.
  ### 2. Flet te permite crear interfaces de usuario de forma rápida y sencilla, gracias a sus widgets declarativos y su sistema de diseño flexible.
  ### 3.  Con Flet, puedes escribir menos código para lograr el mismo resultado que con otros frameworks. Esto se traduce en un desarrollo más rápido y eficiente.
  ### 4. Flet proporciona herramientas de depuración integradas que te facilitan encontrar y solucionar problemas en tu código.
  ### 5. Flet te permite ver los cambios en tu código al instante sin necesidad de reiniciar la aplicación. Esto te ayuda a ahorrar tiempo y ser más productivo.

<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000" height="2">
</p>


# Configuracion de nuestro entorno de desarrollo

   ## Linux/Ubuntu
1. Crea un entorno virtual: Abre una terminal y navega hasta el directorio donde deseas instalar Flet. Luego, crea un entorno virtual ejecutando el siguiente comando:
    ```
   python3 -m venv .venv 
    ```

2. Activa el entorno virtual: Para activar el entorno virtual, ejecuta el siguiente comando:
   ```
   source .venv/bin/activate
   ```
3. Instala Flet: Una vez activado el entorno virtual, puedes instalar Flet ejecutando el siguiente comando:
   ```
   pip install flet
   ```

4. Verifica la instalación: Para verificar que Flet se haya instalado correctamente, ejecuta el siguiente comando:
   ```
   flet --version
   ```

  ## MacOs
 1. Crea un entorno virtual: Sigue los mismos pasos que para la instalación en Linux, utilizando el comando ```python3 -m venv .venv``` para crear un entorno virtual.

2. Activa el entorno virtual: Activa el entorno virtual ejecutando el comando 
```
source .venv/bin/activate
```

3. Instala Flet: Instala Flet utilizando el comando 
```
pip install flet
```

4. Verifica la instalación: Verifica la instalación ejecutando el comando 
```
flet --version
```

   ## Windows


1. Crea un entorno virtual: Sigue los mismos pasos que para la instalación en Linux y macOS, utilizando el comando ```python3 -m venv .venv ``` para crear un entorno virtual

2. Activa el entorno virtual: Activa el entorno virtual ejecutando el comando source .venv/bin/activate

3. Instala Flet: Instala Flet utilizando el comando 
```
pip install flet
```

4. Verifica la instalación: Verifica la instalación ejecutando el comando 
```
flet --version
```



<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000" height="2">
</p>

# Conceptos Básicos de flet

# 1. Widgets:
### Los widgets son los elementos básicos de la interfaz de usuario en Flet. Hay una gran variedad de widgets disponibles, como botones, etiquetas, campos de entrada, imágenes, listas, etc. Cada widget tiene sus propias propiedades y métodos que puedes usar para personalizar su apariencia y comportamiento.

# 2. Diseño de la interfaz de usuario:
### Flet utiliza un sistema de diseño declarativo para crear interfaces de usuario. Esto significa que describes la estructura y el diseño de tu interfaz de usuario en código Python, y Flet se encarga de generar el HTML, CSS y JavaScript necesarios para que funcione en diferentes plataformas.

# 3. Eventos:
### Los eventos son acciones que ocurren en la interfaz de usuario, como clics del mouse, pulsaciones de teclas o cambios en el valor de un campo de entrada. Puedes asociar funciones a los eventos para que se ejecuten cuando ocurran.

# 4. Rutas:
### Las rutas te permiten navegar entre diferentes pantallas de tu aplicación. Puedes definir diferentes rutas y asociarlas a diferentes widgets o acciones.

# 5. Estado:
### El estado de tu aplicación se almacena en variables. Puedes acceder y modificar el estado desde tu código Python.

# 6. API:
### Flet proporciona una API completa que te permite acceder a las funciones y funcionalidades del framework. La API está bien documentada y es fácil de usar.

# 7. Comunidad:
### Flet tiene una comunidad de desarrolladores en crecimiento que está siempre dispuesta a ayudar. Puedes encontrar ayuda en el foro de la comunidad, en los canales de redes sociales o en los repositorios de GitHub de Flet.


<p align="center">
<img src="https://user-images.githubusercontent.com/74038190/212744287-14f66c13-5458-40dc-9244-8ff533fc8f4a.gif" width="1000">
</p>


> (Opcional) Complemente la información  anterior con este video:

```{youtube} bRqbHpXklPU
```


<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000" height="2">
</p>

# Primera aplicación con flet

### 1. Para este curso cree esta estructura de archivos que mantendremos vigente en todos los proyectos.

![image](https://github.com/compose-projects/socialLocal/assets/124411052/ceb5303d-a880-4d5a-8953-371cc1dce450)

<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000" height="2">
</p>

### 2.Importe flet a su proyecto para poder usarlo:
![image](https://github.com/compose-projects/socialLocal/assets/124411052/20be3308-9cf2-4474-8a37-f7040e12b1a0)

### 3. Declare una función main y conozca el método `page` el cual es de suma importancia comprender, porque será usado en todo el curso.

![image](https://github.com/compose-projects/socialLocal/assets/124411052/dd271347-5b8e-4814-aa8e-cc6552e6bd01)

### 4. Para nuestra primera aplicación con flet haremos un contador simple, para ello agregue la siiguiente lógica dentro de su función main. PD: Flet es hijo de flutter y sus componentes tambien, entonces si conoce de flutter va a comprender flet.
![image](https://github.com/compose-projects/socialLocal/assets/124411052/e89cbb4e-c0cd-4b2a-9bde-17509d9ec56b)

### 5. Por último cree la aplicación: 
![image](https://github.com/compose-projects/socialLocal/assets/124411052/2eb9046c-a631-45a7-8f6a-fc0b3199874f)

 ### 6. Abra su terminal y ejecute:
![image](https://github.com/compose-projects/socialLocal/assets/124411052/c9b189ce-afc1-4da7-96dc-5aff660a7a65)


### Resultado: 
[Grabación de pantalla desde 01-07-24 06:53:38.webm](https://github.com/compose-projects/socialLocal/assets/124411052/ba564751-c414-4666-922f-c6c25c36bb06)


# Conclusion:
### Flet pese al poco tiempo de su creación es un framework que tiene mucho potencial para ser realmente utilizado por grandes masas, gracias a su fácil uso con python. Esta fue una pequeña introducción a flet [1/3] Espero que haya sido de su agrado,

- ult vez 01 jul 18:13



#### by: [Less](https://github.com/less-dev/)
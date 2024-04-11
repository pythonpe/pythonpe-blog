---
blogpost: true
date: Apr 11, 2024
author: gnrfan
location: Lima, Perú
category: Tutorial
tags: tutorial, criptografia, seguridad, principiantes
language: Español
---

# Introducción a la criptografía con Python

## Motivación de este artículo

Para poder implementar correctamente las medidas mínimas de seguridad en tus proyectos con Python,
en particular las aplicaciones web, iremos desarrollando una serie de artículos en donde el objetivo
no es simplemente decirte que paquetes utilizar y que te vueltas un experto en copiar y pegar sino
que, por el contrario, entiendas los conceptos más básicos que te permitan apreciar y evaluar de
forma más efectiva y ¿porque no decirlo? profesional el nivel de seguridad de tu código.

## Algunos conceptos básicos y un poco de contexto

### ¿Qué es la criptografía? (versión para desarrolladores apurados)

Es la disciplina que estudia las técnicas para transformar la información desde su formato original
a otro que permita protegerla del acceso por parte de usuarios no autorizados de forma que se pueda
prevenir cualquier adulteración y certificar su procedencia.

### ¿Qué objetivos buscamos con el uso de la criptografía?

Por lo general buscamos lograr 3 cosas con la criptografía:

* **Confidencialidad:** Asegurar que la información sea consultada y utilizada solo por aquellas
personas que deban poder hacerlo según la voluntad del propietario o creador de la misma.
* **Integridad:** Garantizar que la información no sea alterada sin autorización.
* **Irrenunciabilidad:** Comprobar que las partes que participan en una trasacción son efectivamente
aquellas que dicen serlo y al mismo tiempo evitar que puedan negarlo.

### Principales aplicaciones

* **Seguridad informática:** Proteger datos de usuarios almacenandándo de forma cifrada (encriptada) en
medios sistemas de archivos o bases de datos, proteger las comunicaciones en comunicaciones en línea,
como el tráfico de la web o los correo electrónicos, etc.
* **Comercio electrónico y finanzas en línea:** Protección de las transacciones en línea, en particular cuando
tienen que ver con dinero: compras, ventas, préstamos, cambio de divisas, etc. 
* **Firma digital:**  Verificación de la autenticidad de documentos electrónicos de manera digital, algo que
en el Perú ya tiene valor legal desde que entró en vigencia la [Ley 27269: Ley de Firmas y Certificados Digitales](https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/292289-27269)
* **Criptomonedas y cadenas de bloques:** Las monedas digitales que utilizan la criptografía para garantizar
la seguridad y transparencia de las transacciones pero la tecnología subyacente de [cadena de bloques](https://es.wikipedia.org/wiki/Cadena_de_bloques?useskin=vector)
se utiliza justamente para asegurar la integridad e irrenunciabilidad de información legal, industrial y
comercial, algo que [ya](https://andina.pe/agencia/noticia-minsur-utiliza-blockchain-para-hacer-trazable-toda-su-produccion-estano-955107.aspx) [empieza](https://gestion.pe/economia/empresas/minera-poderosa-incorpora-blockchain-para-abordar-conflictos-sociales-minera-poderosa-incorpora-blockchain-blockchain-noticia/)
[a](https://es.cointelegraph.com/news/peruvian-vanilla-farm-adopts-blockchain-to-improve-traceability-and-quality) [ocurrir](https://medium.com/@stamping.io/certificado-de-vacunaci%C3%B3n-covid-del-per%C3%BA-utilizastamping-io-para-evidencias-blockchain-9b57dee42228)
en el Perú, sobretodo en los sectores mineros, agroindustriales y salud soportando procesos de trazabilidad de documentos y transacciones.

### Regulaciones y normas legales que exigen el uso de la criptografía en el Perú

Como la mayoría de paises del mundo, el Perú ya tiene en vigencia regulaciones y leyes que exigen el uso
de la criptografía en las aplicaciones y por lo tanto afectan nuestro trabajo diario.

La principal es la [Ley 29733: Ley de Protección de Datos Personales](https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733)
que ya entró en vigor hace más de 10 años y que en sus artículos 39 al 41 se ocupa de detalles como la implementación
de controles de acceso (inicio de sesión, gestión de privilegios) y el empleo de cifrado, firmas digitales y sumas de
verificación, en particular para el almacenamiento y transferencia de datos personales de ciudadanos peruanos entre
distintas organizaciones.

Esta misma ley hace referencia a la norma técnica peruana [NTP-ISO/IEC 17799](https://spij.minjus.gob.pe/Graficos/Peru/2007/agosto/25/RM-246-2007-PCM_25-08-07.pdf)
del 2007 que no solo menciona técnicas criptográficas como las que estamos buscando hacer más conocidas en este artículo
sino también buenas prácticas sobre otros aspectos de la seguridad informática y la continuidad del negocio como la 
gestión de las brechas de seguridad, el reporte de vulnerabilidades y el análisis de riesgos.

### ¿Cómo te impacta como desarrollador?

* Requiriendo que sepas implementar correctamente mecanismos de autenticación y autorización.
* Requiriendo que sepas como almacenar adecuadamente contraseñas y otros secretos en bases de datos.
* Requiriendo que sepas como inyectar secretos en tu código en tiempo de ejecución y durante el despliegue
sin que los mismos sean parte de tu código fuente y mucho menos sean incluidos en repositorios bajo
control de versiones.
* Requiriendo que puedas utilizar sumas de verificación y firmas digitales en tus procesos de IT para
garantizar la integridad y no repudio de los datos.

### Tipos de criptografía que nos interesan

* **Criptografía de clave simétrica:** Se utiliza una única clave para cifrar y descifrar la información.
Es eficiente para comunicaciones donde las partes confían entre sí.
* **Criptografía de clave asimétrica:** Se utilizan dos claves diferentes, una pública y otra privada.
La clave pública se utiliza para cifrar la información, y la clave privada para descifrarla.
Es ideal para comunicaciones donde no hay confianza previa entre las partes.
* **Funciones hash:** Se utilizan para generar un resumen digital de la información.
Este resumen permite verificar la integridad de la información sin necesidad de descifrarla.

### A ver explícamelo pero más facilito y con ejemplos

* Cuando colocas una clave en un archivo comprimido con un programa como WinZip estas utilizando una clave simétrica
porque todos los que sepan esa clave podrán revertir el proceso de cifrado y obtener los archivos originales.
* Cuando utilizas PGP o GPG en tus correos o creas una billetera crypto estas utilizando una clave asimétrica.
De hecho, en el caso de las criptomonedas la dirección de la billetera se deriva de la llave pública.
* Otro ejemplo de es criptografía de clave asimétrica nos debería resultar familiar de cuando descargamos paquetes
de Linux desde un repositorio autorizado y conocido, ya que primero hay que descargar y registrar una llave pública
que permite verificar que los paquetes provienen de una fuente oficial de la distribución o del proyecto opensource
y no de una tercera parte que podría incluir en ellos código malicioso.
* Finalmente, un ejemplo muy conocido del uso de funciones de hashes para realizar sumas de verificación que te
debería resultar familiar, consiste en descargar una imagen ISO que nos permite instalar un sistema operativo como
Windows o alguna distribución de Linux empleando una memoria USB. Como el archivo es grande y puede tener varios
gigabytes el riesgo de que la información este corrupta por problemas en la descarga aumenta y antes de perder tiempo
intentando hacer la instalación con una imagen producto de una descarga fallida calculamos la suma de verificación
[MD5](https://es.wikipedia.org/wiki/MD5) ó [SHA-256](https://es.wikipedia.org/w/index.php?title=Secure_Hash_Algorithm&useskin=vector)
y confirmamos la integridad del archivo descargado comprobando que tenemos la descarga correcta.

### Algunas ideas adicionales importantes antes de pasar a programar

* Cifrado o encriptación es lo mismo. Según la [Real Academia de la Lengua Española](https://www.rae.es/)
los términos [cifrar](https://dle.rae.es/encriptar) y [encriptar](https://dle.rae.es/cifrar) son sinónimos y
la principal acepción que aparece listada es bastante clara: _Transcribir en guarismos, letras o símbolos, de acuerdo
con una clave, un mensaje o texto cuyo contenido se quiere proteger_.  
* Los datos en binario no necesariamente estan cifrados en el sentido de que no se han transformado para protegerlos,
simplemente estan representados en su forma digital más sencilla posible empleando cifras binarias como el 0 y el 1.
* La codificación de secuencias de datos binarios en formatos que simplemente los cambian de base como
[Base 64](https://es.wikipedia.org/wiki/Base64) tampoco constituyen una forma de criptografía y se pueden revertir
de inmediato de manera directa ya se trata simplemente de un sistema de numeración posicional que utiliza los caracteres
imprimibles de la tabla ASCII original para definir un alfabeto con símbolos que se emplean para representar las cifras
del 1 al 64. Lo mismo sucede al representar datos binarios en formato [hexadecimal](https://es.wikipedia.org/wiki/Hexadecimal):
podría tratarse de información cifrada o en **texto plano** que es como se llama a la información que no esta siendo
cifrada para ser protegida.
* En criptografía un **secreto** es cualquier pieza de información que justamente, como su nombre lo dice, debe mantenerse
en secreto por parte de sus usuarios y no debería ser compartida con terceras personas, salvo en el caso de los llamados
secretos compartidos en donde dos o más partes utilizan el mismo secreto para verificar algo. Esto ocurre on los códigos de
6 u 8 dígitos empleados la autenticación por segundo factor empleando OTPs o contraseñas descartables en cuyo caso el mismo
secreto o semilla está almacenado tanto por el dispositivo que genera el código como en la infraestructura en la nube de
la página web o servicio en linea que lo verifica.
* Muchos de los algoritmos criptográficos hacen uso de números aleatorios o [pseudo-aleatorios](https://es.wikipedia.org/wiki/N%C3%BAmero_pseudoaleatorio)
ya que estos son la entrada para general llaves o actuan como las claves en los algorítmos de cifrado simétrico. 

## Ahora si manos a la obra con un poco de Python

Las [funciones Hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) se inventaron originalmente para poder indexar y buscar información dentro de estructuras de datos en memoria de forma que las características de los datos como los valores más frecuentes no creen una distribución poco uniforme pero rápidamente encontraron otros usos, especialmente para comparar datos de forma más simple sin tener que comparar todo el contenido de una cadena o archivo sino solo los resultados devueltos por la función hash, que dado que se producen por un proceso determinístico sin aleatoriedad, siempre van a dar el mismo resultado.

Cuando empecé a aprender un poco de estos temas rápidamente confirmé una intuición matemática: ¿si el conjunto de valores de entrada es infinito pero el conjunto de valores de salida es finito no vamos a obtener valores repetidos? Sí. Cualquier función de hash puede tener teóricamente infinitos valores que devuelvan el mismo resultado y por lo tanto, infinitas **colisiones** como se llaman a los casos en donde el resultado es idéntico.

La gracia está en que, en la práctica, los algoritmos de hashing que usamos emplean internamente series de matrices que descomponen los bits de la entrada y los mandan por distintos "circuitos" que reducen muy significativamente el riesgo de encontrar una colisión en nuestro dia a dia. Cuando un cierto algoritmo empieza a tener un número potencialmente problemático de colisiones para usos reales del dia a dia, se suele dejar de utilizar y es reemplazado por otro más robusto, asi esto implique hacer más cálculos y por lo tanto gastar un poco más de energía y dinero para computar el resultado.

Es asi, que por ejemplo, a pesar de que el nombre MD5 aún suena y es popular, hoy por hoy en pleno 2024 se recomienda en su lugar el uso de SHA-256 ó SHA-512 para sumas de verificación que comprueban la integridad de archivos. El algoritmo [BLAKE2b](https://en.wikipedia.org/wiki/BLAKE_(hash_function)) es otro un poco más nuevo que ofrece un buen balance entre velocidad (complejidad del cómputo) y seguridad (probabilidad de obtener una colisión).

### Computando el hash de una simple cadenita de texto

La librería estándar de Python incluye implementaciones para las principales funciones hash en el [módulo hashlib](https://docs.python.org/es/3/library/hashlib.html).

A continuación una pequeña demo de como usar estas funciones:

```python
import hashlib

cadenas = ["", "Hola mundo"]

for cadena in cadenas:
    print(f"Cadena: {cadena}")
    
    # Calcular hashes
    hash_md5 = hashlib.md5(cadena.encode()).hexdigest()
    hash_sha1 = hashlib.sha1(cadena.encode()).hexdigest()
    hash_sha256 = hashlib.sha256(cadena.encode()).hexdigest()
    hash_sha512 = hashlib.sha512(cadena.encode()).hexdigest()
    hash_blake2b = hashlib.blake2b(cadena.encode()).hexdigest()
    
    # Imprimir resultados
    print(f"MD5: {hash_md5}")
    print(f"SHA-1: {hash_sha1}")
    print(f"SHA-256: {hash_sha256}")
    print(f"SHA-512: {hash_sha512}")
    print(f"Blake2b: {hash_blake2b}")
    print()
```

**Salida:**

```
Cadena:
MD5: d41d8cd98f00b204e9800998ecf8427e
SHA-1: da39a3ee5e6b4b0d3255bfef95601890afd80709
SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
SHA-512: cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
Blake2b: 786a02f742015903c6c6fd852552d272912f4740e15847618a86e217f71f5419d25e1031afee585313896444934eb04b903a685b1448b755d56f701afe9be2ce

Cadena: Hola mundo
MD5: f822102f4515609fc31927a84c6db7f8
SHA-1: c083106c930790151165b95bd11860724e3836cb
SHA-256: ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c
SHA-512: 34ddb0edac59e441459e07cf33bd628f53fbbf752141125f069f32081b169f933666c71b2f1b83031da66bc905a1e72af7c6cfd779fc197513639a098f94c641
Blake2b: d716858301360c6ba4619931eacd9ccb3f18c99b7dbc872c95fabb5f6e8e8f88560497234c51b230fad8bcae894977ee0448e4d16078a67406222f84e1406343
```

Nótese que en todos los casos utilizamos el método `hexdigest` para obtener una representación en forma de cadena de texto con dígitos hexadecimales ya que la salida en si de la función es una secuencia de datos binaria. El formato hexadecimal es baste cómodo para inspeccionar secuencias binarias ya que cada cifra representa un [nibble](https://es.wikipedia.org/wiki/Nibble) o "medio byte", es decir, 4 ceros o unos de los 8 que componen un byte. 

Si deseas, ejecuta el script varias veces y comprueba que los valores computados siempre son los mismos. Esa es una de las características importantes de las funciones de hash.

Prueba tu mismo modificando el programa para calcular los hashes de cadenas prácticamente idénticas y verás que el resultado es totalmemnte distinto:

```
Cadena: Hola mundo
MD5: f822102f4515609fc31927a84c6db7f8
SHA-1: c083106c930790151165b95bd11860724e3836cb
SHA-256: ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c
SHA-512: 34ddb0edac59e441459e07cf33bd628f53fbbf752141125f069f32081b169f933666c71b2f1b83031da66bc905a1e72af7c6cfd779fc197513639a098f94c641
Blake2b: d716858301360c6ba4619931eacd9ccb3f18c99b7dbc872c95fabb5f6e8e8f88560497234c51b230fad8bcae894977ee0448e4d16078a67406222f84e1406343

Cadena: hola mundo
MD5: 0ad066a5d29f3f2a2a1c7c17dd082a79
SHA-1: 459567d3bde4418b7fe302ff9809c4b0befaf7dd
SHA-256: 0b894166d3336435c800bea36ff21b29eaa801a52f584c006c49289a0dcf6e2f
SHA-512: e361ecc31f2aac2066a3103d3b14dc63b5984b028f9f2d09dee67460ce2702bc81673acf58109b553324852c62a227d9a75d4c2f686580270fe143048f47c33c
Blake2b: a7f66e229a2bcc6a4e6ec009c08994a958842e592883a30826f81135437719a0408a9f21ea252c3cee582cd05f254b5fb7e6c06db0fa0c8c9f2682051451a275
```

Esa es, justamente, otra de las características importantes de las funciones hash. 

Si buscamos una representación mas corta, lo que podría ser útil si el valor calculado se va a incluir en URLs o compartir con terceras personas, la solida podría representarse también en formato binario, octal y otras representaciones populares como [Base58](https://bitcoinwiki.org/wiki/base58) que es lo que usa Bitcoin para mejorar la legibilidad de las direcciones de las billeteras evitando costosos errores (como potencialmente transferir a la dirección equivocada) al eliminar símbolos que se pueden confundir entre si como al `0` y la `O` (letra "O" mayúscula) o el `1` y la letra `l` (letra "L" minúscula).

```python
import hashlib
import base64
from base58 import b58encode

# Calcular el hash SHA-256
hash_sha256 = hashlib.sha256("Hola mundo".encode()).digest()

# Convertir el hash a base58
hash_base58 = b58encode(hash_sha256)

# Convertir el hash a base64
hash_base64 = base64.b64encode(hash_sha256).decode()

# Imprimir resultados
print(f"SHA-256: {hash_sha256.hex()}")
print(f"Base58: {hash_base58.decode()}")
print(f"Base64: {hash_base64}")
```

**Salida:**

```
SHA-256: ca8f60b2cc7f05837d98b208b57fb6481553fc5f1219d59618fd025002a66f5c
Base58: EdiADfcJoH3PNhpomw1FsTXuNCJ1DTKzsFzDAg18YbmM
Base64: yo9gssx/BYN9mLIItX+2SBVT/F8SGdWWGP0CUAKmb1w=
```

En este último ejemplo si estamos usando el paquete [Base58](https://pypi.org/project/base58/) de [Pypi](https://pypi.org/) que puedes instalar ejecutando `pip install base58` para instalarlo dentro de tu entorno virtual de Python.

Si no sabes como, acá una guia muy rápida con los comandos que tienes que ejecutar en tu shell:

```sh
python -m venv env
source env/bin/activate
pip install base58
python ejemplo_02.py
```

### Verificando un archivo .iso

Imagineremos que tienes a la mano el archivo ISO de Ubuntu 20.04 que se puede descargar de [acá](https://releases.ubuntu.com/22.04.4/ubuntu-22.04.4-desktop-amd64.iso): (cuidado que son 4.7 GB y puede tomar algunos minutos).

El código fuente para poder calcular el hash es el que sigue:

```python
import argparse
import hashlib

def calcular_hash_sha256(ruta_archivo):
    """
    Calcula el hash SHA-256 de un archivo.

    Args:
        ruta_archivo (str): Ruta al archivo.

    Returns:
        str: Hash SHA-256 del archivo.
    """
    with open(ruta_archivo, "rb") as archivo:
        hash_sha256 = hashlib.sha256()
        for bloque in iter(lambda: archivo.read(4096), b""):
            hash_sha256.update(bloque)
        return hash_sha256.hexdigest()

def main():
    # Crear un analizador de argumentos
    parser = argparse.ArgumentParser(description="Calcular el hash SHA-256 de un archivo")
    parser.add_argument("ruta_archivo", help="Ruta al archivo")

    # Parsear los argumentos
    args = parser.parse_args()

    # Si no se ha pasado la ruta al archivo, mostrar la ayuda
    if not args.ruta_archivo:
        parser.print_help()
        return

    # Calcular el hash SHA-256 del archivo
    hash_sha256 = calcular_hash_sha256(args.ruta_archivo)

    # Imprimir el hash SHA-256
    print(f"Hash SHA-256 del archivo {args.ruta_archivo}: {hash_sha256}")

if __name__ == "__main__":
    main()
```

Por favor, presta atención a algunos detalles de la implementación:

* Estamos empleando un [gestor de contexto](https://python-intermedio.readthedocs.io/es/latest/context_managers.html)
para abrir el archivo y cerrarlo automáticamente al final.
* El archivo original se esta leyendo en bloques de 4096 bytes a la vez y en modo binario.
* Estamos creando un objeto [iterador](https://python-intermedio.readthedocs.io/es/latest/generators.html?highlight=iterador#iterador) a partir de una función anónima para poder emplear un bucle `for`
* La función `sha256` del módulo `hashlib` devuelve un objeto que permite computar parcialmente el hash a partir
de la función de hash seleccionada que en nuestro caso es SHA-256. Internamente, por razones de eficiencia Python
está empleando a su vez funciones criptográficas de la librería de código abierto [OpenSSL](https://www.openssl.org/).
* La naturaleza de los algoritmos de hashing permite que el contenido se vaya procesando en bloques lo que cual
facilita mucho las cosas porque no tenemos que cargar los 4.7 GB en memoria. Esto se logra con el método `update`. 

**Ejecución:**

```sh
python calcular_hash_sha1.py ubuntu-22.04.4-desktop-amd64.iso
```

**Salida:**

```
Hash SHA-256 del archivo ubuntu-22.04.4-desktop-amd64.iso: 071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd
```

El valor obtenido es el correcto como puedes comparar dando una mirada al contenido de este archivo:

https://releases.ubuntu.com/22.04.4/SHA256SUMS

```
071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd *ubuntu-22.04.4-desktop-amd64.iso
45f873de9f8cb637345d6e66a583762730bbea30277ef7b32c9c3bd6700a32b2 *ubuntu-22.04.4-live-server-amd64.iso
```

Para darte una mejor idea de que tan pesadas pueden ser estas operaciones con archivos grandes yo si descargué el 
archivo ISO original y ejecuté el script con Python 3.11.3 en una PC bastante modesta con un procesador Intel Core i3
corriendo a 3.70 Ghz corriendo en Ubuntu 22.04 en WSL2 y me demoró casi 5 minutos:

```
time python calcular_hash_sha256.py ubuntu-22.04.4-desktop-amd64.iso
Hash SHA-1 del archivo ubuntu-22.04.4-desktop-amd64.iso: 071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd

real    4m59.383s
user    0m29.578s
sys     0m8.694s
```

El comando `sha256sum` que viene incluido con Ubuntu permite realizar el proceso de forma sustancialmente más sencilla y rápida tomando esta vez 
1 minuto y 16 segundos:

```sh
time sha256sum ubuntu-22.04.4-desktop-amd64.iso
071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd  ubuntu-22.04.4-desktop-amd64.iso

real    1m16.814s
user    0m22.480s
sys     0m1.465s
```

Acá lo importante es hacernos una idea de la diferencia de tiempos ya que en este caso el cómputo del hash se completó aproximadamente
unas 4 veces más rápido.

## ¿Cómo se ve una implementación de la funcion SHA-256 en Python puro?

Más o menos así:

```python
#!/usr/bin/python
__author__ = 'Thomas Dixon'
__license__ = 'MIT'

import copy
import struct
import sys


def new(m=None):
    return sha256(m)

class sha256(object):
    _k = (0x428a2f98L, 0x71374491L, 0xb5c0fbcfL, 0xe9b5dba5L,
          0x3956c25bL, 0x59f111f1L, 0x923f82a4L, 0xab1c5ed5L,
          0xd807aa98L, 0x12835b01L, 0x243185beL, 0x550c7dc3L,
          0x72be5d74L, 0x80deb1feL, 0x9bdc06a7L, 0xc19bf174L,
          0xe49b69c1L, 0xefbe4786L, 0x0fc19dc6L, 0x240ca1ccL,
          0x2de92c6fL, 0x4a7484aaL, 0x5cb0a9dcL, 0x76f988daL,
          0x983e5152L, 0xa831c66dL, 0xb00327c8L, 0xbf597fc7L,
          0xc6e00bf3L, 0xd5a79147L, 0x06ca6351L, 0x14292967L,
          0x27b70a85L, 0x2e1b2138L, 0x4d2c6dfcL, 0x53380d13L,
          0x650a7354L, 0x766a0abbL, 0x81c2c92eL, 0x92722c85L,
          0xa2bfe8a1L, 0xa81a664bL, 0xc24b8b70L, 0xc76c51a3L,
          0xd192e819L, 0xd6990624L, 0xf40e3585L, 0x106aa070L,
          0x19a4c116L, 0x1e376c08L, 0x2748774cL, 0x34b0bcb5L,
          0x391c0cb3L, 0x4ed8aa4aL, 0x5b9cca4fL, 0x682e6ff3L,
          0x748f82eeL, 0x78a5636fL, 0x84c87814L, 0x8cc70208L,
          0x90befffaL, 0xa4506cebL, 0xbef9a3f7L, 0xc67178f2L)
    _h = (0x6a09e667L, 0xbb67ae85L, 0x3c6ef372L, 0xa54ff53aL,
          0x510e527fL, 0x9b05688cL, 0x1f83d9abL, 0x5be0cd19L)
    _output_size = 8
    
    blocksize = 1
    block_size = 64
    digest_size = 32
    
    def __init__(self, m=None):        
        self._buffer = ''
        self._counter = 0
        
        if m is not None:
            if type(m) is not str:
                raise TypeError, '%s() argument 1 must be string, not %s' % (self.__class__.__name__, type(m).__name__)
            self.update(m)
        
    def _rotr(self, x, y):
        return ((x >> y) | (x << (32-y))) & 0xFFFFFFFFL
                    
    def _sha256_process(self, c):
        w = [0]*64
        w[0:16] = struct.unpack('!16L', c)
        
        for i in range(16, 64):
            s0 = self._rotr(w[i-15], 7) ^ self._rotr(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = self._rotr(w[i-2], 17) ^ self._rotr(w[i-2], 19) ^ (w[i-2] >> 10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFFL
        
        a,b,c,d,e,f,g,h = self._h
        
        for i in range(64):
            s0 = self._rotr(a, 2) ^ self._rotr(a, 13) ^ self._rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = self._rotr(e, 6) ^ self._rotr(e, 11) ^ self._rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + self._k[i] + w[i]
            
            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFFL
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFFL
            
        self._h = [(x+y) & 0xFFFFFFFFL for x,y in zip(self._h, [a,b,c,d,e,f,g,h])]
        
    def update(self, m):
        if not m:
            return
        if type(m) is not str:
            raise TypeError, '%s() argument 1 must be string, not %s' % (sys._getframe().f_code.co_name, type(m).__name__)
        
        self._buffer += m
        self._counter += len(m)
        
        while len(self._buffer) >= 64:
            self._sha256_process(self._buffer[:64])
            self._buffer = self._buffer[64:]
            
    def digest(self):
        mdi = self._counter & 0x3F
        length = struct.pack('!Q', self._counter<<3)
        
        if mdi < 56:
            padlen = 55-mdi
        else:
            padlen = 119-mdi
        
        r = self.copy()
        r.update('\x80'+('\x00'*padlen)+length)
        return ''.join([struct.pack('!L', i) for i in r._h[:self._output_size]])
        
    def hexdigest(self):
        return self.digest().encode('hex')
        
    def copy(self):
        return copy.deepcopy(self)
```

Este código [ha sido tomado](https://github.com/thomdixon/pysha2/blob/master/sha2/sha256.py) el repositorio [https://github.com/thomdixon/pysha2] de [Thom Dixon](https://github.com/thomdixon).

Como puedes ver, no es una implementación trivial. Por lo general -y siguiendo con el ejemplo de MD5-, en el mundo de la seguridad informática,
estos algortimos son presentados en congresos académicos como [CRYPTO 1991](https://www.iacr.org/cryptodb/data/conf.php?year=1991&venue=crypto)
y buscan ser ampliamente difundidos para poder detectar vulnerabilidades en el mismo diseño.

El diseñador de este algoritmo, [Ronald Rivest](https://en.wikipedia.org/wiki/Ron_Rivest), que es la "R" de [RSA](https://www.rsa.com/), lo
difundió a través de un memo recogido en el [RFC 1321](https://www.rfc-es.org/rfc/rfc1321-es.txt) publicado en 1992 y tan pronto como en 1993
ya empezaron a aparecer [varios](https://link.springer.com/content/pdf/10.1007/3-540-48285-7_26.pdf) [otros](https://ftp.arnes.si/packages/crypto-tools/rsa.com/cryptobytes/crypto2n2.pdf.gz) 
[papers](https://web.archive.org/web/20090521001714/http://www.infosec.sdu.edu.cn/uploadfile/papers/How%20to%20Break%20MD5%20and%20Other%20Hash%20Functions.pdf) 
señalando las vulnerabilidades y como implementar ataques.

Contar con implementaciones de código abierto de funciones criptográficas y herramientas de seguridad es importante ya que, a pesar de que pueden [ser explotadas](https://nvd.nist.gov/vuln/detail/CVE-2020-22916) ingeniosamente por atacantes que incluyen código malicioso en proyectos infiltrándose en el equipo de mantenedores como pasó como [las herramientas XZ](https://es.wikipedia.org/wiki/XZ_Utils), es la propia naturaleza abierta y la capacidad de escrutinio del opensource lo que permitió a [Andrés Freund](https://www.linkedin.com/in/andres-freund/), un desarrollador alemán del equipo de [Postgres](https://www.postgresql.org/) y empleado de Microsoft a [descubrir la puerta trasera](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) que había sido implantada años antes y que podría haber facilitado muy serios ciberataques de escala global como lo reportó la prensa [internacional](https://arstechnica.com/security/2024/04/what-we-know-about-the-xz-utils-backdoor-that-almost-infected-the-world/) y [nacional](https://elcomercio.pe/tecnologia/ciberseguridad/como-un-ingeniero-evito-un-ciberataque-global-al-notar-que-un-programa-demoraba-medio-segundo-mas-en-cargar-linux-seguridad-informatica-vulnerabilidad-noticia/).

## Ejercicio propuesto

¿Quieres aplicar tu nuevo conocimiento sobre las funciones de hashing a un problema concreto? ¡Intenta resolver este reto!

Diseña un programa en Python que encuentre y reporte archivos contenido duplicado en una carpeta y todas sus subcarpetas.

Aquí algunas sugerencias:

* Emplee una función de hashing como SHA-256 para computar el hash del contenido de cada archivo.
* Utiliza estos hashes como las llaves de un diccionario que mantenga listas con las rutas absolutas de los archivos que tienen
el mismo contenido.
* Reporta aquellas listas que tengan dos o más archivos, es decir, donde existan archivos con contenido duplicado.
* Utiliza la función [glob](https://docs.python.org/es/3/library/hashlib.html) para iterar sobre todos los archivos presentes
en la carpeta actual y sus subcarpetas.
* Apóyate en herramientas de inteligencia artificial generativa como ChatGPT, Gemini o Claude para general el código o depurarlo
si te quedas atorado o tienes problemas para depurarlo.

## Repaso, conclusiones y cierre

### Repaso

Lo más importante que debes recordar de este artículo es que la criptografía ayuda a proteger la información contra actores potencialmente maliciosos y esto se logra empleando distintos algoritmos que transforman los datos de forma reversible pero también irreversible. Ambas cosas son útiles y tienen una gran variedad de aplicaciones en un gran número de casos de uso. 

Hay 3 tipos de algoritmos critográficos que nos interesan más como desarrolladores: aquellos que usan claves simétricas y son reversibles, como cifrar un archivo empleando un password, aquellos que usan claves asimétricas, como una pareja de claves pública y privada que es la base de las firmas y certificados digitales como los que protegen el tráfico web o las conexiones por SSH y las funciones hash que nos permiten verificar la integridad de los archivos o comprobar contraseñas almacenándolas en un formato cifrado con técnicas que mitigan el riesgo de ataques.

### Conclusiones

* La librería estándar de Python incluye implementaciones razonablemente eficientes de las principales funciones de hashing integrandose con librerías (bibliotecas) como OpenSSL.
* El cómputo de sumas de verificación con funciones hash se puede realizar de manera incremental sobre archivos bastante grandes.
* La implementación de estas funciones no es algo trivial, exige mucha investigación y diseño y se beneficia del exhaustivo escrutinio de los investigadores en ciberseguridad y la implementación por parte de proyectos de código abierto que permiten que el código sea auditable.

### Cierre

Si no conocías mucho de estos temas o si ya te estabas olvidando de lo que aprendiste alguna vez, espero que este artículo te haya servido como una introducción
ó te haya ayudado a recordar algunos de estos conceptos que hoy por hoy son tan fundamentales.

En un siguiente artículo explicaremos como emplear funciones hash para almacenar contraseñas en bases de datos con un nivel de seguridad adecuada.

**SPOILER:** No es tan sencillo como computar directamente una de estas funciones y ya sino que hay que combinarlas con otras técnicas y aplicarlas cientos o miles de veces sobre la salida de ellas mismas para aumentar el costo computacional de un eventual ataque por fuerza bruta.

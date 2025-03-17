---
blogpost: true
date: Apr 2, 2024
author: soloidx
location: Lima, Perú
category: Snippets
tags: utilidades
language: Español
---

# Manejo de time zones en Python

Una de las tareas muy frecuentes para un desarrollador es el manejo de fechas, y siempre es un dolor de cabeza manejar los time zones, si bien, actualmente existen librerías que nos ayudan enormemente en este proceso podemos repasar básicamente cómo implementar time zones por nosotros mismos.

![Python developer](/_static/images/ia_developer_datetime.jpg)

## Uso simple con UTC:

Normalmente se puede hacer uso de la librería `datetime.timezone` para obtener el timezone UTC:

```python
from datetime import datetime, timezone
foo = datetime.now(timezone.utc)
bar = datetime(hour=12, minute=11, tzinfo=timezone.utc)
```

El módulo `timezone` tiene sólo UTC (+00hrs) pero podemos tenemos otras alternativas para insertar otros time zones:

## Usando ZoneInfo:

Python (3.9+) también incluye un módulo con time zones llamado `zoneinfo` que contiene una lista de implementaciones de time zones estándar: 

```python
from zoneinfo import ZoneInfo

lima_tz = ZoneInfo("America/Lima")
lima_time = datetime.now(lima_tz)

print(lima_time)
# 2024-04-02 21:30:27.906895-05:00
```


## Crear timezones mas complejos


Si en algún momento necesitamos crear un time zone más complicado, podemos crear una subclase de `tzinfo` y ponerle las propiedades que queramos:


```python
from datetime import datetime, timedelta, tzinfo

class LimaTZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-5)
	def dst(self, dt):
	    return timedelta(0)
    def tzname(self, dt):
        return "PET"

lima_tz = LimaTZ()
lima_time = datetime.now(lima_tz)
```

Éste es un ejemplo de un timezone creado para la ciudad de Lima, Perú (-5:00hrs)

## Usando Pytz:

Y para terminar este post ponemos la solución más básica utilizando Pytz (necesita ser instalado independientemente) la ventaja de Pytz es que nos permite el soporte para versiones de python antiguas a 3.9:

```python
from datetime import datetime

from pytz import timezone

lima_tz = timezone("America/Lima")
lima_time = datetime.now(lima_tz)
```

Ya para terminar, espero que este artículo les haya resultado de utilidad y en un futuro publicaré otro artículo sobre el manejo de fechas con Python junto con algunas otras librerías externas que nos puedan ayudar. 

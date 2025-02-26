---
blogpost: true
date: Feb 26, 2025
author: soloidx
location: Lima, Perú
category: Tutorial
tags: AI, openai, GPT, PyMuPDF, llm, PDF
language: Español
---

# Potencia tu CV con Python y OpenAI (I): De PDF a Datos Estructurados en Minutos

Últimamente he estado pensando en cómo mejorar mi proceso de solicitud de empleo. ¿Sabes lo frustrante que es tener que reformatear constantemente tu CV para diferentes ofertas? Con cada empresa tenía que adaptar para que mi CV haga tenga el mejor fit para el puesto de trabajo. Estaba cansado de editar manualmente la misma información una y otra vez.

![Python developer](/_static/images/CV-python-openai.png)


Así que este fin de semana, decidí construir una pequeña herramienta que pudiera extraer automáticamente todos los datos estructurados de mi CV. Usando Python y GPT-4 de OpenAI, creé un script que toma un CV en PDF y lo convierte en una estructura JSON limpia que puedo usar en cualquier lugar. ¿La mejor parte? Me tomó menos de una hora programarlo, y ahora puedo integrarlo con otra solucion para construir el mejor CV para cada oferta de trabajo. ¡Déjame mostrarte cómo lo construí!

## Estructura del Proyecto

Primero, vamos a configurar la estructura de nuestro proyecto. Necesitamos un entorno virtual, algunos directorios para nuestros datos y salida, y nuestras dependencias.

```bash
# Create project directory
mkdir cv_improver_poc
cd cv_improver_poc

# Create virtual environment
python -m venv venv

# Activate virtual environment (on macOS/Linux)
source venv/bin/activate

# Create directories
mkdir -p data output src
```

Luego instalamos los paquetes necesarios:

```bash
pip install pymupdf openai python-dotenv
pip freeze > requirements.txt
```

Tu estructura de proyecto debería verse así:
```
cv_improver_poc/
├── data/           # Coloca tu CV en PDF aquí
├── output/         # La salida JSON irá aquí
├── src/            # Código Python
├── venv/           # Entorno virtual
└── requirements.txt
```

Agregué `python-dotenv` para que pudiera leer el API key de OpenAI desde un archivo en local (en vez de insertarlo directamente en el código o exportarlo cada vez que lo ejecuto) este es el contenido de mi archivo `.env`

```text
OPENAI_API_KEY=sk-proj-sigue la llave privada...
```

## Lectura y Análisis del PDF

Ahora vamos a escribir el código para leer el PDF. Estoy usando PyMuPDF (importado como `pymupdf`) que hace muy fácil extraer texto de PDFs:

```python
import os
import pymupdf
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

doc = pymupdf.open(os.path.join(ROOT_DIR, "../data", "Ider Delzo CV.pdf"))

output_text = ""

for page in doc:
    text = page.get_text()
    output_text += text
    output_text += "\n"
```

Este código es bastante sencillo:
1. Importamos las bibliotecas necesarias
2. Cargamos las variables de entorno (para nuestra clave API de OpenAI)
3. Abrimos el archivo PDF desde el directorio de datos
4. Recorremos cada página, extraemos el texto y lo concatenamos en una sola cadena

## Creando el Prompt

La magia ocurre en el prompt que enviamos a OpenAI. Necesitamos ser muy específicos sobre lo que queremos:

```python
# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create the prompt
prompt = f"""
You are an expert CV analyzer. Your task is to extract structured information
from the given CV text and format it as a JSON object. Be meticulous, precise,
and comprehensive in your extraction.

CV Text:
{output_text}

Instructions:
1. Extract and structure the information exactly as specified in the JSON schema below.
2. Ensure all dates are in YYYY-MM format. If only the year is available, use YYYY-01.
3. For ongoing experiences, use 'Present' as the end date.
4. List all experiences and education entries in reverse chronological order (most recent first).
5. If information for a field is not present in the CV, use an empty string ("") or empty list ([]) as appropriate.
6. Be as detailed as possible, especially for job descriptions, milestones, and skills.
7. Infer skills from job descriptions if not explicitly listed.
8. Ensure consistency in formatting and capitalization.

JSON Schema:
{{
  "name": "Full name of the person",
  "contactInfo": {{
    "email": "Email address",
    "phone": "Phone number with country code if available",
    "location": "City, State/Province, Country",
    "linkedin": "Full LinkedIn profile URL",
    "github": "Full Github profile URL",
  }},
  "summary": "A concise professional summary, capturing key skills and career objectives",
  "experience": [
    {{
      "date": {{
        "start": "Start date in YYYY-MM format",
        "end": "End date in YYYY-MM format or 'Present' if current"
      }},
      "company": "Full company name",
      "position": "Exact job title",
      "description": "Detailed job description, including responsibilities and technologies used",
      "milestones": [
        "Specific, quantifiable achievements or significant projects",
        "Use metrics and numbers where possible"
      ],
      "skills": [
        "Technical skills",
        "Soft skills",
        "Tools and technologies used"
      ]
    }}
  ],
  "education": [
    {{
      "date": {{
        "start": "Start date in YYYY-MM format",
        "end": "End date in YYYY-MM format"
      }},
      "institution": "Full name of the educational institution",
      "degree": "Complete degree title",
      "fieldOfStudy": "Specific field of study or major",
      "achievements": [
        "Notable academic achievements",
        "Relevant coursework",
        "Projects or thesis topics"
      ]
    }}
  ],
  "skills": [
    "Comprehensive list of all skills mentioned throughout the CV",
    "Include both technical and soft skills"
  ],
  "languages": [
    {{
      "language": "Language name",
      "proficiency": "Proficiency level (e.g., Native, Fluent, Intermediate, Basic)"
    }}
  ],
  "certifications": [
    {{
      "name": "Full name of the certification",
      "issuer": "Issuing organization",
      "date": "Date obtained in YYYY-MM format",
      "expiryDate": "Expiry date in YYYY-MM format, if applicable"
    }}
  ]
}}

Provide the extracted information strictly in the JSON format specified above, without any additional explanation or commentary.
"""
```

He diseñado este prompt para que sea muy detallado porque quiero que la IA extraiga información específica en un formato consistente. El esquema JSON define exactamente qué campos quiero y cómo deben estructurarse. También lo puse intencionalmente en inglés para obtener mejores resultados.

## Llamando a la API de OpenAI y Obteniendo los Resultados

Ahora vamos a llamar a la API de OpenAI y procesar los resultados:

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that extracts and structures CV information accurately.",
        },
        {"role": "user", "content": prompt},
    ],
    temperature=0.1,
)

# Parse the response
content = response.choices[0].message.content
if isinstance(content, str):
    cv_data = json.loads(content)
    print(json.dumps(cv_data, indent=2))

    with open(os.path.join(ROOT_DIR, '../output', 'structured_cv_hybrid.json'), 'w') as f:
        json.dump(cv_data, f, indent=2)
```

En esta parte final:
1. Llamamos a la API de OpenAI con nuestro prompt
2. Establecemos una temperatura baja (0.1) para obtener resultados más consistentes
3. Analizamos la respuesta JSON
4. La imprimimos en la consola y la guardamos en un archivo en nuestro directorio de salida

## Resultado final

Puedes revisar el resultado final en [este archivo](https://raw.githubusercontent.com/soloidx/cv_improver_poc/refs/heads/main/output/structured_cv_hybrid.json)

Puedes revisar el código en este proyecto: [cv_improver_poc](https://github.com/soloidx/cv_improver_poc)

## Conclusión

¡Y eso es todo! Con solo unas pocas líneas de código Python, he creado una herramienta que puede transformar mi CV de un PDF estático a un formato JSON flexible y estructurado. Ahora puedo pasar a otra etapa en donde analyzaré las ofertas de empleo y generaré tanto CVs como cartas de presentaíon a medidas para cada empresa.
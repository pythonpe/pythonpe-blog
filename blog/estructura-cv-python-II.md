---
blogpost: true
date: Mar 16, 2025
author: soloidx
location: Lima, Perú
category: Tutorial
tags: AI, NLP, ML, Data Science, Spacy
language: Español
---

# Potencia tu CV con Python (II): Usando NLP para hacer match con ofertas

¡Hola de nuevo! En este [artículo anterior](https://blog.python.pe/blog/estructura-cv-python-I/) les conté cómo desarrollé un sistema para estructurar y analizar mi CV utilizando inteligencia artificial. Hoy quiero compartir la segunda parte de este proyecto: el análisis de compatibilidad entre mi CV y las ofertas laborales.

![Python developer](/_static/images/CV-python-openai.png)


Después de lograr estructurar mi CV de manera eficiente, me di cuenta de que el siguiente paso lógico era determinar qué tan compatible soy con las ofertas de trabajo que encuentro. ¿De qué sirve tener un CV bien estructurado si no sabemos a cuáles ofertas vale la pena aplicar?

## Procesamiento bilingüe

La primera característica en la que pensé es que pueda trabajar tanto con ofertas en español como en inglés. Esto es crucial para quienes buscamos trabajo en mercados internacionales:


```python
class JobMatcher:
    def __init__(self):
        # Cargar el modelo de spaCy para ingles
        # Si necesitas otro idioma, cambia 'en_core_web_sm' por el modelo correspondiente
        # Por ejemplo, 'es_core_news_sm' para español
        try:
            self.nlp_es = spacy.load("es_core_news_md")
            self.nlp_en = spacy.load("en_core_web_md")
        except OSError:
            # Si los modelos no están instalados, descárgalos
            print("Descargando modelos de spaCy...")
            os.system("python -m spacy download es_core_news_md")
            os.system("python -m spacy download en_core_web_md")
            self.nlp_es = spacy.load("es_core_news_md")
            self.nlp_en = spacy.load("en_core_web_md")

```

El sistema detecta automáticamente el idioma del texto analizando palabras comunes:

```python
    def get_language_nlp(self, text: str) -> str:
        es_words = ["el", "la", "los", "las", "y", "en", "de", "para", "con", "por"]
        en_words = ["the", "and", "in", "of", "to", "for", "with", "by", "on", "at"]

        text_lower = text.lower()
        es_count = sum(1 for word in es_words if f" {word} " in f" {text_lower} ")
        en_count = sum(1 for word in en_words if f" {word} " in f" {text_lower} ")

        return "es" if es_count > en_count else "en"

    def get_doc(self, text: str) -> Doc:
        text_language = self.get_language_nlp(text)
        if text_language == "es":
            return self.nlp_es(text)
        return self.nlp_en(text)
```

## El algoritmo de compatibilidad

Ahora comenzamos con el core de la lógica, vamos a definir la compatibilidad usando el título de la oferta (Ej. Senior Python Developer) y también la lista de skills definidos (Python, Flask, SQL) asi que los extraemos y los calculamos por separado:

```python
def analyze_job_offer(self, cv_data: dict, job_data: dict) -> dict:
    position_score = self.analyze_positions(cv_data, job_data)
    skills_score = self.analyze_skills(cv_data, job_data)
    
    overall_score = position_score * 0.5 + skills_score * 0.5

    return {
        "overall_score": overall_score,
        "position_score": position_score,
        "skills_score": skills_score,
    }
```

Ahora veremos la implementación de ambos scores individualmente:

### 1. Compatibilidad de posición

comparemos el título del puesto ofrecido con mis experiencias laborales previas, buscando la mejor coincidencia:

```python
def analyze_positions(self, cv_data: dict, job_data: dict) -> float:
    scores = []
    experience = cv_data.get("experience", [])

    for exp in experience:
        position_score = self.get_position_score(
            job_data.get("job_title", ""), exp.get("position", "")
        )
        scores.append(position_score)
    
    max_score = max(scores) if scores else 0.0
    return max_score
```

Lo interesante aquí es que no solo busca coincidencias exactas, sino que utiliza la similitud semántica para entender si mi experiencia es relevante para el puesto. Además, considera el nivel de seniority:

```python
    def get_position_score(self, job_post_title: str, exp_position: str) -> float:
        if not job_post_title or not exp_position:
            return 0.0
        job_doc = self.get_doc(job_post_title)
        exp_doc = self.get_doc(exp_position)

        # Calcular la similitud vectorial entre el título de trabajo y la posición del empleado
        similarity = float(exp_doc.similarity(job_doc))

        seniority_levels = {
            "intern": 1,
            "junior": 2,
            "associate": 2,
            "i": 2,
            "ii": 3,
            "mid": 3,
            "intermediate": 3,
            "iii": 4,
            "senior": 5,
            "sr": 5,
            "lead": 6,
            "principal": 7,
            "staff": 7,
            "architect": 8,
            "director": 9,
            "head": 9,
            "chief": 10,
        }

        # extraer el niver de seniority
        job_seniority = 0
        exp_seniority = 0

        for token in job_doc:
            if token.text in seniority_levels:
                job_seniority = seniority_levels[token.text]
                break

        for token in exp_doc:
            if token.text in seniority_levels:
                exp_seniority = seniority_levels[token.text]
                break

        # Calcular la diferencia de niveles de senioridad y aplicar un penalizador
        seniority_diff = abs(job_seniority - exp_seniority)
        seniority_penalty = min(seniority_diff * 0.1, 0.5)  # Cap penalizador a 0.5

        similarity *= 1 - seniority_penalty

        return similarity
```

### 2. Compatibilidad de habilidades

Esta parte es crucial: ¿tengo las habilidades técnicas que la empresa está buscando?

```python
    def analyze_skills(self, cv_data: dict, job_data: dict) -> float:
        # Obtengo las habilidades del CV y las de cada emperiencia
        skills = set(cv_data.get("skills", []))
        for exp in cv_data.get("experience", []):
            skills.update(exp.get("skills", []))
        job_skills = set(job_data.get("skills", {}).get("technologies", []))

        # Calcular el match directo
        direct_matches = skills.intersection(job_skills)
        direct_matches_score = (
            len(direct_matches) / len(job_skills) if job_skills else 0.0
        )

```

Pero aquí viene lo realmente interesante. ¿Qué pasa con las habilidades que no coinciden exactamente pero están relacionadas? Por ejemplo, si la oferta pide "React.js" y yo tengo "React" en mi CV, o si piden "AWS" y yo tengo "Amazon Web Services".
Para resolver esto, implementé un análisis de similitud semántica:

```python

        # Podemos tambien calcular los matches semanticos que no coinciden directamente
        remaining_job_skills = skills - direct_matches
        if not remaining_job_skills:
            return 1.0

        semantic_match_score = 0.0
        remaining_cv_skills = skills - direct_matches
        semantic_matches = 0

        # Definir un umbral de similitud para los matches semanticos
        skill_similarity_threshold = 0.75

        for job_skill in remaining_job_skills:
            job_doc = self.get_doc(job_skill)
            best_similarity = 0.0

            for cv_skill in remaining_cv_skills:
                cv_doc = self.get_doc(cv_skill)
                similarity = job_doc.similarity(cv_doc)

                if similarity > best_similarity:
                    best_similarity = similarity

            if best_similarity >= skill_similarity_threshold:
                semantic_matches += 1
        semantic_match_score = (
            semantic_matches / len(remaining_job_skills)
            if remaining_job_skills
            else 0.0
        )

        final_score = 0.8 * direct_matches_score + 0.2 * semantic_match_score
        return final_score
```

Y gracias a esto puedo generar un score más preciso, por ahora tengo un resultado decente, en algún momento pensé en implementar OpenAI para un análisis mas semantico pero eso puede dar mas espacio para otro artículo. 


Puedes revisar el código en este proyecto: [02_job_match_compatibility.py](https://github.com/soloidx/cv_improver_poc/blob/main/src/02_job_match_compatibility.py)

También implementé un script para estructurar una oferta laboral usando OpenAI [02_extract_job_information.py](https://github.com/soloidx/cv_improver_poc/blob/main/src/02_extract_job_information.py)
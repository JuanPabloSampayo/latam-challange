# Data Engineer Challenge
​
## Descripción General
Bienvenido al desafío para Ingenieros de Datos. En esta ocasión, tendrás la oportunidad de acercarte a parte de la realidad del rol, demostrar tus habilidades y conocimientos en procesamiento de datos con python y diferentes estructuras de datos.
​
## Instrucciones
1. Tu solución debe estar en un repositorio público de la plataforma github. 
2. Para enviar tu desafío, debes hacer un `POST` request a `https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer`. Esto es un ejemplo del cuerpo que debes enviar:
```json
    {
      "name": "Juan Perez",
      "mail": "juan.perez@example.com",
      "github_url": "https://github.com/juanperez/latam-challenge.git"
    }
```

3. El plazo máximo de entrega del challenge son **5 días corridos completos** a partir de la recepción del challenge. Por ejemplo: Si recibiste el challenge el día jueves 21 de Septiembre a las 3 pm, tienes plazo hasta el martes 26 de septiembre a las 23:59.
3. Puedes utilizar las tecnologías y técnicas que prefieras para el procesamiento de datos. ¡Valoraremos tus conocimientos en plataformas cloud!. En tal caso, procura seguir el paso a paso en tus archivos **SIN** agregar las credenciales de acceso a los distintos servicios.
4. Los desafíos que posean un orden claro, sean explicativos, modulares, eficientes y creativos serán mejor rankeados. 
5. ¡Recuerda que no estamos en tu cabeza! Escribe los supuestos que estás asumiendo. Además, incluye las versiones de las librerías que estás usando en el archivo `requirements.txt`. Por favor, `NO BORRAR` lo que ya viene escrito en el archivo.
6. Para este desafío te recomendamos que describas claramente cómo mejorar cada parte de tu ejercicio en caso de que tenga opción de mejora.
7. Debes utilizar los datos contenidos en el [siguiente archivo](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing).
8. Puedes utilizar la [documentación oficial de twitter](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) para entender la estructura de los datos.
9. Evaluaremos positivamente las buenas prácticas de uso de git. Tus commits, branches, pull requests. 
10. Usa la rama main para cualquier versión final que quieras que revisemos. Te recomendamos que uses alguna práctica de [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). NOTA: No borres tus ramas de desarrollo.
10. Recuerda considerar el manejo de errores y casos borde.
11. Recuerda que vas a trabajar a la par con más desarrolladores, por lo que la mantenibilidad, legibilidad y escalabilidad de tu código es esencial.
12. Una buena documentación del código siempre ayuda al lector.

​
## Challenge
En el [archivo](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing) encontrarás un conjunto aproximado de 398MBs. Se pide resolver los siguientes problemas implementando funciones, usando **2 enfoques por cada problema**: Uno en el que se optimice el tiempo de ejecución, y otro en que se optimice la memoria en uso.

Tu desafío debe tener al menos 6 archivos python en la carpeta `src`. Cada uno de estos archivos correspondiente a la función del mismo nombre, con el mismo formato que se indica en las instrucciones de más abajo. Solo deja la función. Además de eso, debes tener un archivo `.ipynb` donde expliques con mayor claridad tu código. En este jupyter notebook puedes ejecutar tus funciones, medir el tiempo de ejecución, memoria en uso y explayarte según estimes conveniente. Te recomendamos fuertemente que utilices celdas markdown para que expliques el paso a paso de tu código.

**NOTA:** los archivos `.py` y `.ipynb` de interés ya están creados en la estructura del desafío, solo debes completarlos con tu solución y/o agregar los archivos que estimes convenientes.
​
1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```
​
2. Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
```
3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. Debe incluir las siguientes funciones:
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```
​
## Sugerencias
* Para medir la memoria en uso te recomendamos [memory-profiler](https://pypi.org/project/memory-profiler/) o [memray](https://github.com/bloomberg/memray)
* Para medir el tiempo de ejecución te recomendamos [py-spy](https://github.com/benfred/py-spy) o [Python Profilers](https://docs.python.org/3/library/profile.html)

---

## Notas de trabajo - Juan Pablo Sampayo

### flujo de trabajo
1. **EDA** — primero explore el dataset para entender la estructura, los campos relevantes y los datos faltantes. todo esta documentado en src/challenge.ipynb
2. **implementacion** — resolvi cada pregunta en su propia branch (feature/q1, feature/q2, feature/q3), con dos variantes por pregunta: una optimizada en tiempo y otra en memoria
3. **branching** — use gitflow: main para version final, develop como integracion, y feature branches para cada pieza de trabajo. las branches no se borran
4. **CI** — agregue una github action que valida que todos los imports funcionen en cada push/PR

### enfoque general
- uso orjson para parsear el JSON (mas rapido que json estandar)
- todas las funciones leen el archivo en modo streaming (linea a linea) usando el formato JSON Lines
- extraigo la fecha como string ([:10]) sin parsear a datetime, mas rapido y suficiente para agrupar

### decisiones tecnicas
- Q1: la variante _time guarda todos los usuarios en memoria con defaultdict(Counter). la variante _memory hace dos pasadas al archivo, solo trackeando usuarios de las top 10 fechas
- Q2: use emoji.emoji_list() en ambas variantes por precision (regex es 14x mas rapido pero falla con emojis compuestos). la diferencia real esta en memoria: _time precarga contenido (39 MB), _memory hace streaming (0.9 MB)
- Q3: uso el campo mentionedUsers del JSON en vez de regex sobre el texto, porque ya viene pre-parseado por snscrape

### consideraciones cloud

si este dataset creciera a escala produccion (millones de tweets, actualizacion diaria), el enfoque local no escala. una arquitectura cloud podria ser:

**ingesta y almacenamiento**
- subir los JSON a Google Cloud Storage (GCS)
- usar un formato columnar como Parquet para reducir tamaño y acelerar queries

**procesamiento**
- BigQuery: cargar los datos y resolver las 3 preguntas con SQL puro, sin preocuparme por memoria ni tiempo — BigQuery escala automaticamente
- alternativa: Apache Spark en Dataproc o EMR para procesamiento distribuido si necesito transformaciones mas complejas

**orquestacion**
- Cloud Composer (Airflow) o Cloud Functions para automatizar la ingesta y el procesamiento diario

**Conclusion**

no implemente la version cloud porque el dataset actual (389MB) se procesa en menos de 10 segundos localmente, pero la arquitectura esta pensada para escalar.
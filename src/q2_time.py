from typing import List, Tuple
from collections import Counter
import orjson
import emoji


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """top 10 emojis mas usados con su conteo.
    enfoque: optimizado en tiempo, precarga todo el contenido en memoria
    para procesar emojis con mejor localidad de cache.
    usa ~39 MB pero es mas rapido por acceso secuencial."""

    # precargo todo el contenido en una lista
    contenidos = []
    with open(file_path, 'rb') as f:
        for line in f:
            contenidos.append(orjson.loads(line).get('content', ''))

    conteo = Counter()
    for content in contenidos:
        for e in emoji.emoji_list(content):
            conteo[e['emoji']] += 1

    return conteo.most_common(10)
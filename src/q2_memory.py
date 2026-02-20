from typing import List, Tuple
from collections import Counter
import orjson
import emoji


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """top 10 emojis mas usados con su conteo.
    enfoque: optimizado en memoria, streaming linea a linea.
    usa ~0.9 MB (97% menos que la version _time) con resultados identicos."""

    conteo = Counter()

    with open(file_path, 'rb') as f:
        for line in f:
            t = orjson.loads(line)
            for e in emoji.emoji_list(t.get('content', '')):
                conteo[e['emoji']] += 1

    return conteo.most_common(10)
from typing import List, Tuple
from collections import Counter
import orjson


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """top 10 usuarios mas mencionados con su conteo.
    enfoque: optimizado en memoria, streaming linea a linea.
    solo mantiene el Counter en memoria (~0.5 MB)."""

    conteo = Counter()

    with open(file_path, 'rb') as f:
        for line in f:
            t = orjson.loads(line)
            if t.get('mentionedUsers'):
                for u in t['mentionedUsers']:
                    conteo[u['username']] += 1

    return conteo.most_common(10)
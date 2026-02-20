from typing import List, Tuple
from collections import Counter
import orjson


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """top 10 usuarios mas mencionados con su conteo.
    enfoque: optimizado en tiempo, precarga todo en memoria
    para procesar con mejor localidad de cache (~50 MB)."""

    tweets = []
    with open(file_path, 'rb') as f:
        for line in f:
            tweets.append(orjson.loads(line))

    conteo = Counter()
    for t in tweets:
        if t.get('mentionedUsers'):
            for u in t['mentionedUsers']:
                conteo[u['username']] += 1

    return conteo.most_common(10)
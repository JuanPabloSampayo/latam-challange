from typing import List, Tuple
from collections import Counter
import orjson


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """top 10 usuarios mas mencionados con su conteo.
    enfoque: optimizado en tiempo, precarga solo las listas de
    mentionedUsers (no el tweet completo) para procesar mas rapido
    sin desperdiciar memoria en campos que no necesitamos."""

    menciones = []
    with open(file_path, 'rb') as f:
        for line in f:
            users = orjson.loads(line).get('mentionedUsers')
            if users:
                menciones.append(users)

    conteo = Counter()
    for users in menciones:
        for u in users:
            conteo[u['username']] += 1

    return conteo.most_common(10)
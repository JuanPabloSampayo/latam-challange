from typing import List, Tuple
from datetime import datetime
from collections import Counter
import orjson


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """top 10 fechas con mas tweets + usuario que mas publico ese dia.
    enfoque: optimizado en memoria, dos pasadas al archivo."""

    tweets_x_fecha = Counter()
    # primera pasada: solo cuento tweets por fecha
    with open(file_path, 'rb') as f:
        for line in f:
            t = orjson.loads(line)
            tweets_x_fecha[t['date'][:10]] += 1

    top_fechas = set(f for f, _ in tweets_x_fecha.most_common(10))

    # segunda pasada: solo para las top 10, cuento usuarios
    users_x_fecha = {f: Counter() for f in top_fechas}
    with open(file_path, 'rb') as f:
        for line in f:
            t = orjson.loads(line)
            fecha = t['date'][:10]
            if fecha in top_fechas:
                users_x_fecha[fecha][t['user']['username']] += 1

    resultado = []
    for fecha, _ in tweets_x_fecha.most_common(10):
        top_user = users_x_fecha[fecha].most_common(1)[0][0]
        resultado.append((datetime.strptime(fecha, '%Y-%m-%d').date(), top_user))

    return resultado
from typing import List, Tuple
from datetime import datetime
from collections import Counter, defaultdict
import orjson


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """top 10 fechas con mas tweets + usuario que mas publico ese dia.
    enfoque: optimizado en tiempo, carga todo en memoria de una."""

    tweets_x_fecha = Counter()
    users_x_fecha = defaultdict(Counter)

    with open(file_path, 'rb') as f:
        for line in f:
            t = orjson.loads(line)
            fecha = t['date'][:10]
            user = t['user']['username']
            tweets_x_fecha[fecha] += 1
            users_x_fecha[fecha][user] += 1

    resultado = []
    for fecha, _ in tweets_x_fecha.most_common(10):
        top_user = users_x_fecha[fecha].most_common(1)[0][0]
        resultado.append((datetime.strptime(fecha, '%Y-%m-%d').date(), top_user))

    return resultado
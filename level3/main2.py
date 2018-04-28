from pprint import pprint
from collections import namedtuple, defaultdict
import numpy as np
start, end, nimages = map(int, input().split())
Image = namedtuple('Image', ['timestamp'])
asteroids = defaultdict(lambda:[])

for i in range(nimages):
    timestamp, rows, cols = map(int, input().split())
    image = []
    for j in range(rows):
        image.append(list(map(lambda x: 1 if x else 0, map(int, input().split()))))

    if any(any(row) for row in image):
        npimage = np.array(image, dtype=np.int, ndmin=2)
        npimage = np.array(npimage[:, ~np.all(npimage==0, axis=0)])
        npimage = np.array(npimage[~np.all(npimage==0, axis=1)])
        idarray = np.array2string(npimage)
        asteroids[idarray].append(timestamp)

def back(lista, accdiff, totaldiff, result, end):

    head = lista[0]

    if len(lista) > 1:

        nothead = lista[1]
        diff = nothead - head

        # El siguiente elemento a la cabeza tiene la misma diferencia
        if diff == accdiff:
            return result.append(head) + back(lista[1:], totaldiff, totaldiff)
        # El siguiente elemento a la cabeza tiene menor diferencia
        elif diff < accdiff:
            return result + back(lista[0] + lista[:2], accdiff - diff, totaldiff)
        # El siguiente elemento a la cabeza tiene mayor diferencia
        else:
            return result

    else:

        if head + accdiff > end:
            return result.append(head)
        else:
            return []

head = asteroids.items()[0]

for tailhead in asteroids.items()[:1]:
    diff = tailhead - head
    pprint(back(asteroids.items(), diff, diff, [], end))

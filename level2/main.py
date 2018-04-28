from pprint import pprint
from collections import namedtuple
import numpy as np
start, end, nimages = map(int, input().split())
Image = namedtuple('Image', ['data', 'mintime', 'maxtime', 'counter'])

images = {}

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
        if not idarray in images:
            images[idarray] = Image(npimage, timestamp, timestamp, 1)
        else:
            if images[idarray].maxtime < timestamp:
                images[idarray] = images[idarray]._replace(maxtime=timestamp, counter=images[idarray].counter + 1)

for _, image in images.items():
    print(image.mintime, image.maxtime, image.counter)
 
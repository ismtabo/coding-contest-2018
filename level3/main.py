import sys
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

viewed_asteroids = []
for idasteroid, timestamps in asteroids.items():
    used = set()
    for i, timestamp in enumerate(timestamps[:-3]):
        if timestamp in used:
            continue
        else:
            used.add(timestamp)
        for j, othertimestamp in enumerate(timestamps[i+1:], start=i+1):
            print(f"#{i} Min {timestamp}", end=' ',file =sys.stderr)
            iter_used = {timestamp, othertimestamp}
            delta = othertimestamp - timestamp
            print(f"Next #{j} {othertimestamp} Delta {delta}",file =sys.stderr)
            start = j
            end = j+1
            while end < len(timestamps):
                timestart = timestamps[start]
                timeend = timestamps[end]
                if timeend in used:
                    end += 1
                    continue
                print(f"Comparing #{start}({timestart})-#{end}({timeend}) = {timeend-timestart} == {delta}", end=' ', file=sys.stderr)
                if timestamps[end] - timestamps[start] == delta:
                    print(f"It's in", file=sys.stderr)
                    start, end = end, end + 1
                    iter_used.add(timestart)
                elif timestamps[end] - timestamps[start] > delta:
                    print(f"Super Nope", file=sys.stderr)
                    break
                else:
                    print(f"Nope", file=sys.stderr)
                    end += 1
            iter_used.add(timestamps[start])
            if not (len(iter_used) < 4) and (timestamps[start] + delta > end) and (timestamp - delta <= start):
                print(f"Found {(timestamp, timestamps[start], len(iter_used))}", file=sys.stderr)
                viewed_asteroids += [(timestamp, timestamps[start], len(iter_used))]
                used = used | iter_used
                break
            print(f"\n\nUsed {sorted(used)}", file=sys.stderr)
        assert sorted(used) == sorted(timestamps), "Sth goes wrong"

    print(f"\n\nThis is not my final form\n\n", file=sys.stderr)


for start, end, counter in sorted(viewed_asteroids, key=lambda x: x[0]):
    print(start, end, counter)
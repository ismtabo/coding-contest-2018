start, end, nimages = map(int, input().split())

images = []

for i in range(nimages):
    timestamp, rows, cols = map(int, input().split())
    image = []
    for j in range(rows):
        image += map(int, input().split())
    if start <= timestamp <= end:
        if any(image):
            print(timestamp)
 
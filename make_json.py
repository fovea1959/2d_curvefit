import csv
import json

rows = []
with open('Cargo Acquisition.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        r0 = {}
        for k, v in row.items():
            if v != '':
                r0[k] = float(v)
        rows.append(r0)

o_x = []
o_y = []
o_a = []
o_d = []

for r1 in rows:
    print(r1)
    o_x.append((r1['screen.x'], r1['screen.y'], r1['ball.x']))
    o_y.append((r1['screen.x'], r1['screen.y'], r1['ball.y']))
    o_a.append((r1['screen.x'], r1['screen.y'], r1['angle']))
    o_d.append((r1['screen.x'], r1['screen.y'], r1['distance_in']))

    if False and r1['angle'] != 0:
        sx = 1 - r1['screen.x']
        o_x.append((sx, r1['screen.y'], r1['ball.x']))
        o_y.append((sx, r1['screen.y'], r1['ball.y']))
        a = -r1['angle']
        o_a.append((sx, r1['screen.y'], a))
        o_d.append((sx, r1['screen.y'], r1['distance_in']))

o_x.sort(key=lambda r: (r[0], r[1]))
o_y.sort(key=lambda r: (r[0], r[1]))
o_a.sort(key=lambda r: (r[0], r[1]))
o_d.sort(key=lambda r: (r[0], r[1]))

data = {
    'x': o_x,
    'y': o_y,
    'a': o_a,
    'd': o_d
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

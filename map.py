BLANK=0
ROAD=1
DIM=10
tiles = [BLANK,ROAD]

map=[{"value": -1,"options":[BLANK,ROAD]} for _ in range(DIM*DIM)]


for i in range(0,DIM):
    for j in range(0,DIM):
        tile = map[j + i * DIM]
        if tile["value"] == -1:
            index=tile["options"][0]

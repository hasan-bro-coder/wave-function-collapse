import random

BLANK=0
UP_ROAD=1
DOWN_ROAD=2
LEFT_ROAD=3
RIGHT_ROAD=4


DIM=2
tiles = [BLANK,UP_ROAD,RIGHT_ROAD,DOWN_ROAD,LEFT_ROAD]
rules = {
    "BLANK":[
        [BLANK,UP_ROAD]
        [BLANK,RIGHT_ROAD]
        [BLANK,DOWN_ROAD]
        [BLANK,LEFT_ROAD]
    ],
    "UP_ROAD":[
        [RIGHT_ROAD,DOWN_ROAD,LEFT_ROAD]
        [LEFT_ROAD,UP_ROAD,DOWN_ROAD]
        [BLANK,DOWN_ROAD]
        [RIGHT_ROAD,DOWN_ROAD,UP_ROAD]
    ],   
    "RIGHT_ROAD": [
        [RIGHT_ROAD, DOWN_ROAD, LEFT_ROAD],   # Top
        [UP_ROAD, LEFT_ROAD, DOWN_ROAD],     # Left
        [UP_ROAD, LEFT_ROAD, RIGHT_ROAD],   # Bottom
        [BLANK,LEFT_ROAD]     # Left
    ],
    "DOWN_ROAD": [
        [BLANK, UP_ROAD],                   # Top
        [LEFT_ROAD, UP_ROAD, DOWN_ROAD],    # Right
        [RIGHT_ROAD, UP_ROAD, LEFT_ROAD],   # Bottom
        [RIGHT_ROAD, DOWN_ROAD, UP_ROAD]    # Left
    ],
    "LEFT_ROAD": [
        [LEFT_ROAD, RIGHT_ROAD, DOWN_ROAD],   # Top
        [BLANK, RIGHT_ROAD]                  # Left
        [RIGHT_ROAD, LEFT_ROAD, UP_ROAD], # Right
        [RIGHT_ROAD, UP_ROAD, DOWN_ROAD],    # Bottom
    ]
}
map=[{"value": False,"options":[BLANK,UP_ROAD,DOWN_ROAD,LEFT_ROAD,RIGHT_ROAD]} for _ in range(DIM*DIM)]
map[3]={"value": True,"options":[BLANK,UP_ROAD]}

def checkValid(options,valid):
    for i in range(len(options), 0, -1):
        if options[i] in valid:
            print(i)

mapCopy = map.copy()
mapCopy = sorted(mapCopy, key=lambda x: len(x["options"]))

lent = len(mapCopy[0]["options"])
stopindex = 0

for i in range(0,len(mapCopy)):
    if len(mapCopy[i]["options"]) > lent:
        stopindex = i
        break
    stopindex = i

mapCopy=mapCopy[0:stopindex]
cell = random.choice(mapCopy)
cell["value"] = 1
pick = random.choice(cell["options"])
cell["options"] = [pick]
print(mapCopy)

for i in range(0,DIM):
    for j in range(0,DIM):
        tile = map[j + i * DIM]
        if tile["value"] == False:
            index=tile["options"][0]


nextTiles = []
for i in range(0,DIM):
    for j in range(0,DIM):
        index = j + i * DIM
        if map[index]["value"] == True:
            nextTiles[index] = map[index]
        else:
            options = [BLANK,UP_ROAD,RIGHT_ROAD,DOWN_ROAD,LEFT_ROAD]
            #up 
            if i > 0:
                up = map[j + (i-1) * DIM]
                for option in up["options"]:
                    valid = rules[option][2]
                    checkValid(option,valid)
        
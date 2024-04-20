#!/usr/bin/env python3
import struct
tiles = []
items = []
width = 52
height = 100
def decode(head, tack):
    return tack<<8|head
    return (head*95+tack)

for z in range(1, 51):
    with open("./LEV01.MAP".format(z), "rb") as f:
        for x in range(4):
            for y in range(height):
                tiles.append(161)
            for y in range(18):
                tiles.append(161)
        
        for x in range(width):
            tiles.extend([161]*10)
            for y in range(height):
                tiles.append(decode(f.read(1)[0],f.read(1)[0]) + 500)
            tiles.extend([161]*8)
        
        tiles.extend(([161]*(118*64)))
        tiles = tiles[:118*64]
        
        for x in range(4):
            for y in range(height):
                items.append(0)
            for y in range(18):
                items.append(0)
        
        for x in range(width):
            items.extend([0]*10)
            for y in range(height):
                i = decode(f.read(1)[0],f.read(1)[0])
                if i == 0:
                    items.append(0)
                else:
                    items.append(i + 2399)
            items.extend([0]*8)
        
        items.extend(([0]*(118*64)))
        items = items[:118*64]

    with open("lev01.map".format(z), "wb") as f:
        f.write(b"""MAP V01.30 Furcadia
height=118
width=64
revision=646
patcht=1
name=DSPIRE15
patchs=./
encoded=0
allowjs=1
allowlf=1
allowfurl=1
swearfilter=0
nowho=0
forcesittable=0
allowshouts=1
rating=Teen+
allowlarge=0
notab=0
nonovelty=0
parentalcontrols=1
nowho=0
ismodern=1
BODY
""")
        f.write(struct.pack("<{}H".format(len(tiles)), *tiles))
        f.write(struct.pack("<{}H".format(len(items)), *items))
        walls = []
        t = 0
        def getAtXY(x, y):
            return tiles[(x * 118) + y]
        for x in range(64):
            for y in range(118):
                walls.extend([0, 0])
                t += 1
        f.write(struct.pack("<{}B".format(len(walls)), *walls))
#!/usr/bin/env python3
from PIL import Image
import struct
import random

palette = b"".join([
    bytes.fromhex("000034"),
    bytes.fromhex("343451"),
    
    bytes.fromhex("ae0000"),
    bytes.fromhex("d76161"),
    
    bytes.fromhex("497d28"),
    bytes.fromhex("69a610"),
    
    bytes.fromhex("cb924d"),
    bytes.fromhex("e7db4d"),
    
    bytes.fromhex("0000ae"),
    bytes.fromhex("6565db"),
    
    bytes.fromhex("920092"),
    bytes.fromhex("be45cf"),
    
    bytes.fromhex("515175"),
    bytes.fromhex("61929e"),
    
    bytes.fromhex("b2cfeb"),
    bytes.fromhex("ffefeb"),
])

sSpriteCount = struct.Struct("<H")
sSpriteInfo = struct.Struct("<BB")
sSpriteSize = struct.Struct("<BB")
sprites = []

with open("AARGH.OOF", "rb") as f:
    spriteCount, = sSpriteCount.unpack(f.read(sSpriteCount.size))
    sprites = [None]*spriteCount
    for i in range(spriteCount):
        x, y = sSpriteInfo.unpack(f.read(sSpriteInfo.size))
        sprites[i] = {
            "offset": [x,y],
            "size": [0,0],
            "data": b""
        }
    
    for i in range(spriteCount):
        w,h = sSpriteSize.unpack(f.read(sSpriteSize.size))
        src = f.read(w*h)
        sprites[i]["size"] = [w,h]
        data = bytearray(w*h)
        for x in range(w):
            for y in range(h):
                data[(y*w)+x] = src[(x*h)+y]
        sprites[i]["data"] = data

def createSprite(sprite):
    print(sprite["offset"])
    im = Image.new("L", tuple(sprite["size"]))
    im.putdata(sprite["data"])
    im.putpalette(palette)
    return im

i = 0
for sprite in sprites:
    createSprite(sprite).save("sprites/sprite_{:0>3}.gif".format(i),transparency = 0x0b)
    im = Image.open("sprites/sprite_{:0>3}.gif".format(i))
    #This is a dumb hack to get alpha to load properly in PNG
    im = im.convert("RGBA")
    im.save("sprites/sprite_{:0>3}.png".format(i))
    i+=1
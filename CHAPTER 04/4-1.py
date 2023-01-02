{\rtf1\ansi\ansicpg949\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 n = input()\
direc = input().split()\
coord_x = 1\
coord_y = 1\
\
for i in range(len(direc)):\
    if direc[i] == "L":\
        if not (coord_y - 1 < 1):\
            coord_y -= 1\
    if direc[i] == "R":\
        if not (coord_y + 1 < 1):\
            coord_y += 1\
    if direc[i] == "U":\
        if not (coord_x - 1 < 1):\
            coord_x -= 1\
    if direc[i] == "D":\
        if not (coord_x + 1 > 5):\
            coord_x += 1\
\
print(coord_x, coord_y)}
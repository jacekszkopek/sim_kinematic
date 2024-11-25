import numpy as np
from math import *

def rotX(angle):
    rotTab = np.array([[1,   0,              0],
                     [0,    cos(angle),  -sin(angle)],
                     [0,    sin(angle),  cos(angle)]])
    return rotTab


def rotY(angle):
    rotTab = np.array([[cos(angle),   0,  sin(angle)],
                     [0,                1,  0],
                     [-sin(angle),   0,  cos(angle)]])
    return rotTab


def rotZ(angle):
    rotTab = np.array([[cos(angle),   -sin(angle),   0],
                     [sin(angle),    cos(angle),   0],
                     [0,                0,              1]])
    return rotTab


def rotZY(z,y):
    rotTab = np.array([[cos(z)*cos(y),  -sin(z),    cos(z)*sin(y),  0],
                       [sin(z)*cos(y),  cos(z),     sin(z)*sin(y),  0],
                       [-sin(y),        0,          cos(y),         0],
                       [0,              0,          0,              1]])
    return rotTab


def rotYZtranX(ry,rz,tx):
    rotTab = np.array([[cos(rz)*cos(ry),    -sin(rz),   cos(rz)*sin(ry),    tx*cos(rz)*cos(ry)  ],
                       [sin(rz)*cos(ry),    cos(rz),    sin(rz)*sin(ry),    tx*sin(rz)*cos(ry)  ],
                       [-sin(ry),           0,          cos(ry),            -tx*sin(ry)         ],
                       [0,                  0,          0,                  1                   ]])
    return rotTab


def rotYtranX(ry,tx):
    tab = np.array([[cos(ry),   0,  sin(ry),    tx * cos(ry)    ],
                    [0,         1,  0,          0               ],
                    [-sin(ry),  0,  cos(ry),    -tx * sin(ry)   ],
                    [0,         0,  0,          1               ]])
    return tab


def tranrot(tx,ty,tz,rx,ry,rz):
    tab = np.array([[cos(ry) * cos(rz), -cos(ry) * sin(rz), sin(ry), tz * sin(ry) + tx * cos(ry) * cos(rz) - ty * cos(ry) * sin(rz)],
                    [cos(rx) * sin(rz) + cos(rz) * sin(rx) * sin(ry), cos(rx) * cos(rz) - sin(rx) * sin(ry) * sin(rz), -cos(ry) * sin(rx),
                        tx * (cos(rx) * sin(rz) + cos(rz) * sin(rx) * sin(ry)) + ty * (
                        cos(rx) * cos(rz) - sin(rx) * sin(ry) * sin(rz)) - tz * cos(ry) * sin(rx)],
                    [sin(rx) * sin(rz) - cos(rx) * cos(rz) * sin(ry), cos(rz) * sin(rx) + cos(rx) * sin(ry) * sin(rz), cos(rx) * cos(ry),
                        tx * (sin(rx) * sin(rz) - cos(rx) * cos(rz) * sin(ry)) + ty * (
                        cos(rz) * sin(rx) + cos(rx) * sin(ry) * sin(rz)) + tz * cos(rx) * cos(ry)],
                    [0, 0, 0, 1]])
    return tab


def tran3d(arr1,arr2):
    arr1[0] += arr2[0]
    arr1[1] += arr2[1]
    arr1[2] += arr2[2]
    return arr1
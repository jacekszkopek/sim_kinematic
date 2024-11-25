import numpy as np
import math as mh
import matplotlib.pyplot as plt
from matrices import *

BASE = 0
MCP = 1
PIP = 2
DIP = 3
class Finger:
    digits = 3

    basePos = np.zeros(3)
    baseRot = np.zeros((3,3))

    mcpPos = np.zeros(3)
    mcpRot = np.zeros((3,3))

    pos = np.zeros(4)

    def __init__(self, bPos, bRot, mcp_len, pip_len, dip_len, mcp_abd, mcp_flex, pip_flex, dip_flex):
        len = [mcp_len, pip_len, dip_len]
        angles = [mcp_abd, mcp_flex, pip_flex, dip_flex]

        self.basePos = bPos.copy()
        self.baseRot = bRot.copy()

        self.mcpPos = self.basePos.copy()
        self.mcpPos = tran3d(self.mcpPos,[((mcp_len*mh.cos(mcp_abd))*mh.cos(mcp_flex)),mcp_len*mh.sin(mcp_abd),-mcp_len*mh.sin(mcp_flex)])
        self.mcpRot = np.dot(self.baseRot,(np.dot(rotZ(mcp_abd),rotY(mcp_flex))))

        self.pos = [self.basePos.copy(),self.mcpPos.copy(),self.basePos.copy(),self.mcpPos.copy()]
        print(self.pos)
        self.pos = np.transpose(self.pos)
        print(self.pos)


    def show_finger(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d', proj_type='ortho')

        ax.plot3D([self.basePos[0], self.mcpPos[0]], [self.basePos[1], self.mcpPos[1]], [self.basePos[2], self.mcpPos[2]],
                  color='gray', marker='o')
        ax.plot3D(self.basePos[0], self.basePos[1], self.basePos[2], color='red', marker='o')

        ax.set_xlabel('$X$', fontsize=30)
        ax.set_ylabel('$Y$', fontsize=30)
        ax.set_zlabel('$Z$', fontsize=30)

        ax.axes.set_xlim3d(left=0.0, right=19.8)
        ax.axes.set_ylim3d(bottom=0.0, top=19.8)
        ax.axes.set_zlim3d(bottom=0.0, top=19.8)

        plt.show()



    @staticmethod
    def dh_table(a, alfa, d, theta):
        dh_tab = np.array(
            [[mh.cos(theta), -mh.sin(theta) * mh.cos(alfa), mh.sin(theta) * mh.sin(alfa), a * mh.cos(theta)],
             [mh.sin(theta), mh.cos(theta) * mh.cos(alfa), -mh.cos(theta) * mh.sin(alfa), a * mh.sin(theta)],
             [0, mh.sin(alfa), mh.cos(alfa), d],
             [0, 0, 0, 1]])
        return dh_tab

    A1 = np.array

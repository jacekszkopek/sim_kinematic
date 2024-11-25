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

    def __init__(self, palm, mcp_len, pip_len, dip_len, mcp_abd, mcp_flex, pip_flex, dip_flex):
        self.base = palm
        self.mcp = np.dot(self.base, rotYZtranX(mcp_flex,mcp_abd,mcp_len))
        self.pip = np.dot(self.mcp, rotYtranX(pip_flex,pip_len))
        self.dip = np.dot(self.pip, rotYtranX(dip_flex, dip_len))
        self.pos = self.get_pos()
        self.rot = [mcp_abd,mcp_flex,pip_flex,dip_flex]
        self.len = [mcp_len, pip_len, dip_len]

    def get_pos(self):
        tab = np.reshape(self.base[0:3,3],(3,1))
        tab = np.concatenate([tab,np.reshape(self.mcp[0:3,3],(3,1))],axis=1)
        tab = np.concatenate([tab, np.reshape(self.pip[0:3, 3], (3, 1))], axis=1)
        tab = np.concatenate([tab, np.reshape(self.dip[0:3, 3], (3, 1))], axis=1)
        #print(tab)
        return tab



    def move(self,mcp_abd,mcp_flex,pip_flex,dip_flex):
        self.mcp = np.dot(self.base, rotYZtranX(self.rot[1]+mcp_flex,self.rot[0]+mcp_abd, self.len[0]))
        self.pip = np.dot(self.mcp, rotYtranX(self.rot[2]+pip_flex,self.len[1]))
        self.dip = np.dot(self.pip, rotYtranX(self.rot[3] + dip_flex, self.len[2]))
        #update orientation
        self.pos = self.get_pos()
        self.rot = [self.rot[0]+mcp_abd, self.rot[1]+mcp_flex, self.rot[2]+pip_flex, self.rot[3]+dip_flex]
        #print(self.rot)


    def show_finger(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d', proj_type='ortho')

        ax.plot3D(self.pos[0,:],self.pos[1,:],self.pos[2,:],
                  color='gray', marker='o')
        ax.plot3D(self.pos[0][0], self.pos[1][0], self.pos[2][0], color='red', marker='o')

        ax.set_xlabel('$X$', fontsize=30)
        ax.set_ylabel('$Y$', fontsize=30)
        ax.set_zlabel('$Z$', fontsize=30)

        ax.axes.set_xlim3d(left=-10, right=10)
        ax.axes.set_ylim3d(bottom=-10, top=10)
        ax.axes.set_zlim3d(bottom=0.0, top=10)

        plt.show()



    @staticmethod
    def dh_table(a, alfa, d, theta):
        dh_tab = np.array(
            [[mh.cos(theta), -mh.sin(theta) * mh.cos(alfa), mh.sin(theta) * mh.sin(alfa), a * mh.cos(theta)],
             [mh.sin(theta), mh.cos(theta) * mh.cos(alfa), -mh.cos(theta) * mh.sin(alfa), a * mh.sin(theta)],
             [0, mh.sin(alfa), mh.cos(alfa), d],
             [0, 0, 0, 1]])
        return dh_tab

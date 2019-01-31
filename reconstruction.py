# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:06:26 2018

@author: Deimos
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:47:13 2018

@author: Yusuke Ogasawara
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.font_manager import FontProperties
fp_name = FontProperties(fname=r'C:\WINDOWS\Fonts\BRADHITC.TTF', size=25)
import os, subprocess


"""
パラメータ
"""

# 角速度
angular_velocity = 0.15

# 位相のずれ
dev_phase = 0.4

# 円の数
n_circle = 15

# 画像の切り替え時間
interval = 100

# 半径決定のアルゴリズム
radius_type_list = ["arithmetic_sequence", "geometric_sequence"]
radius_type = radius_type_list[0]
if radius_type == "geometric_sequence":
    radius_list = [1.2**(n_circle - j) for j in range(1, n_circle+1)]
else:
    radius_list = [(n_circle - j) for j in range(1, n_circle+1)]

# 名前
name = "Yusuke Ogasawara"

# 時間の進み方
time = "random"

"""
# 意味ない．比が大事．
# 円周同士の距離
distance = 1
"""
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1)

def update(i):
    if i != 0:
        plt.cla()

    ax.set_aspect('equal')
    ax.set_ylim(-max(radius_list)-2, max(radius_list)+2)
    ax.set_xlim(-max(radius_list)-2, max(radius_list)+2)
    ax.tick_params(labelbottom="off",bottom="off") # x軸の削除
    ax.tick_params(labelleft="off",left="off") # y軸の削除
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    if time == "random":
        plt.title("Time : " + "{:>6.1f} s".format(np.random.rand()*100).ljust(6), fontsize= 40)
    else:
        plt.title("Time : " + "{:>6.1f} s".format(i*interval*0.001).ljust(6), fontsize=40)
    for j in range(1, n_circle+1):
        x = np.cos(i*angular_velocity+j*dev_phase)
        y = np.sin(i*angular_velocity+j*dev_phase)
        c = plt.Circle(xy=(x, y), radius=radius_list[j-1], fc=None, fill=False, ec="b")
        ax.add_patch(c)
    
    ax.text(0.99*ax.get_xlim()[0], 0.95*ax.get_ylim()[0], name, color="black", fontproperties=fp_name)
        
ani = animation.FuncAnimation(fig, update, #fargs = ('Initial Animation! ', 2.0), \
    interval = interval, frames = 150, repeat=True)

filename = 'Duchamp_angvel_{}_devphase_{}_ncirc_{}_interval_{}_radtype_{}_name_{}_time_{}'.format(angular_velocity, dev_phase, n_circle, interval, radius_type, name.replace(" ", ""), time)
ani.save('../gif/' + filename + ".gif", writer='ffmpeg')

cmd = "ffmpeg -i {} -pix_fmt yuv420p {}".format("../gif/"+filename+".gif", "../mp4/"+filename+".mp4")
returncode = subprocess.call(cmd.split(), shell=True)

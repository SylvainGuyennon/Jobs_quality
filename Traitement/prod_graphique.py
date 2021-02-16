# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:37:04 2021

@author: Syl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv("df_agg", index_col=0)

df.index = range(0, len(df))

sample_size = len(df)
originals = len(df.drop_duplicates(ignore_index = True))
                
duplicates = sample_size - originals
labels = ["Annonces", "duplicatas"]
data = [originals,duplicates]

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct

k = 2*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 100

x = np.linspace(xmin, xmax, nbx)


fig = plt.figure() # initialise la figure
plt.figure(figsize =(10,8))
plt.pie([originals,duplicates], explode = (0 ,0.1), labels = labels, shadow =True, autopct=make_autopct(data))
line, = plt.plot([],[]) 

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=True, interval=20, repeat=False)

plt.show()


# df = df.drop_duplicates(ignore_index = True)

# df['xp']
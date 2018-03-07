import numpy as np
import matplotlib.pyplot as pl
import matplotlib.gridspec as grsp

x = np.arange(0,2*np.pi,0.0006284)
x = np.append(x,2*np.pi)
print(len(x))
y = np.cos(x)
n = np.random.normal(0,0.1,10000)
z = y + n


#draw
fig = pl.figure(figsize=(8, 6)) 
frame = grsp.GridSpec(2, 1, height_ratios=[1, 1]) 
ax0 = pl.subplot(frame[0])
ax0.plot(x,z,linewidth = 0.5)
ax0.plot(x,y,'w--')
ax0.set_title("cosine wave in noise [0:6]")
ax0.set_ylabel("values")
ax0.legend(['signal + noise','signal'],loc='lower right',facecolor='#00FFCC')
"""
the function <GridSpecFromSubplotSpec> could divide subplot into sections
Do not iteration GridSpec or subplot directly
"""
sub_frame = grsp.GridSpecFromSubplotSpec(1, 2,
                    subplot_spec=frame[1])

bx0 = pl.subplot(sub_frame[0])
bx0.plot(x,z)
bx0.plot(x,y,'w--')
bx0.axis([1,1.5,0,1])
bx0.set_title("cosine wave in noise [1:1.5]")
bx0.set_ylabel("values")
bx0.legend(['signal + noise','signal'],loc='upper right',facecolor='#00FFCC')
bx1 = pl.subplot(sub_frame[1])
bx1.plot(x,z)
bx1.plot(x,y,'r--')
bx1.axis([1,1.05,0.2,1.2])
bx1.set_title("cosine wave in noise [0.2:1.2]")
bx1.set_ylabel("values")
bx1.legend(['signal + noise','signal'],loc='upper right')
pl.show()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

x = np.linspace(0, np.pi/2, 200)
fig = plt.figure(figsize=(10,7), dpi=80)
ax = fig.add_subplot(111)
ax.set_title(' f(x) = sin(x)',fontsize=18)

plt.plot(x, np.sin(x))
plt.xlabel('x [rad]')
plt.ylabel('sin(x)')
plt.xlim(0, np.pi/2)
plt.ylim(0, 1)
plt.grid()
t1 = 0
t2 = np.pi/6
t3 = np.pi/3
t4 = np.pi/2

red_patch = mpatches.Patch(color='blue', label='sin(x)')
plt.legend(bbox_to_anchor=(1, 0.95),handles=[red_patch])

plt.scatter([t1],[np.sin(t1)], 20, color ='blue')
plt.scatter([t2],[np.sin(t2)], 20, color ='blue')
plt.scatter([t3],[np.sin(t3)], 20, color ='blue')
plt.scatter([t4],[np.sin(t4)], 20, color ='blue')

plt.scatter([t1],0, 20, color ='red')
plt.scatter([t2],0, 20, color ='red')
plt.scatter([t3],0, 20, color ='red')
plt.scatter([t4],0, 20, color ='red')
plt.xticks([0,np.pi/6,np.pi/3, np.pi/2],
       [r'$0$',r'$+\pi/6$',r'$+\pi/3$', r'$+\pi/2$'])

plt.yticks([0, +0.5, +0.86602, +1],
       [r'$0$',r'$+0.5$',r'$+0.86602$', r'$+1$'])

plt.savefig('seccion9/graficos/fig2.pdf', format='pdf')
print(r"""
\begin{figure}[htbp]
    \centering
    \includegraphics[width=8cm]{seccion9/graficos/fig2.pdf}
    \label{fig:comparison}
\end{figure}
""")


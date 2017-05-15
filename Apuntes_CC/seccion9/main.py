import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def filled_arc(center, radius, theta1, theta2, ax, color):

    circ = mpatches.Wedge(center, radius, theta1, theta2, fill=False, color=color)
    pt1 = (radius * (np.cos(theta1*np.pi/180.)) + center[0],
           radius * (np.sin(theta1*np.pi/180.)) + center[1])
    pt2 = (radius * (np.cos(theta2*np.pi/180.)) + center[0],
           radius * (np.sin(theta2*np.pi/180.)) + center[1])
    pt3 = center
    pol = mpatches.Polygon([pt1, pt2, pt3], color=ax.get_axis_bgcolor(),
                           ec=ax.get_axis_bgcolor(), lw=2 )
    ax.add_patch(circ)
    ax.add_patch(pol)

def Chebyshev(n,ax=None):
    x = [np.cos(((2*i-1)*np.pi)/(2*n)) for i in range(1,n+1)]
    y = [np.sin(((2*i-1)*np.pi)/(2*n)) for i in range(1,n+1)]
    if ax == None:
        return np.array(x)
    ax.set_ylim(-0.1,1.1)
    ax.set_xlim(-1.1,1.1)
    ax.plot(np.cos(np.linspace(0,np.pi)),np.sin(np.linspace(0,np.pi)),'k-')
    ax.plot([-2,2],[0,0],'k-')
    ax.plot([0,0],[-1,2],'k-')
    for i in range(len(y)):
        ax.plot([x[i],x[i]],[0,y[i]],'r-')
        ax.plot([0,x[i]],[0,y[i]],'r-')
        ax.annotate(str("%.4f" % x[i]), xy=(x[i], -0.07), xytext=(x[i], -0.07))

    ax.plot(x,[0]*len(x),'ro')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot(x,y,'ro')

    filled_arc((0,0), 0.8, 0, 180-18 , ax1, "black")
    ax.text(-0.55, 0.4, r"$\theta_5$", fontsize=25)

    filled_arc((0,0), 0.7, 0, 180-54 , ax1, "black")
    ax.text(-0.17, 0.53, r"$\theta_4$", fontsize=25)

    filled_arc((0,0), 0.6, 0, 90 , ax1, "black")
    ax.text(0.12, 0.43, r"$\theta_3$", fontsize=25)

    filled_arc((0,0), 0.5, 0, 54 , ax1, "black")
    ax.text(0.3, 0.23, r"$\theta_2$", fontsize=25)

    filled_arc((0,0), 0.4, 0, 18, ax1, "black")
    ax.text(0.28, 0.015, r"$\theta_5$", fontsize=25)

    plt.savefig('seccion9/graficos/fig3.pdf', format='pdf')
    print(r"""
    \begin{figure}[htbp]
       \centering
        \includegraphics[width=18cm]{seccion9/graficos/fig3.pdf}
        \label{fig:comparison}
    \end{figure}
    """)


f, (ax1) = plt.subplots(1, figsize=(10,5))
f.suptitle('Grafica con 5 puntos de chevishev', fontsize=14)
Chebyshev(5,ax1)


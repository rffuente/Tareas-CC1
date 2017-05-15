import numpy as np
import matplotlib.pyplot as plt

#funcion a utilizar para el ejemplo

def fun(x):
    return x**3 - 2*(x**2) + (4*x)/3 - (8./27)

#usaremos el metodo de la biseccion para ejemplo de FE y BE
def bisect(f, a, b, tol=10e-8):
    fa = f(a)
    fb = f(b)
    i = 0
    xa = []
    fxa = []

    if np.sign(f(a)*f(b)) >= 0:
        print('f(a)f(b)<0 not satisfied!')
        return None

    while(b-a)/2 > tol:
        c = (a+b)/2.
        fc = f(c)
        xa.append(c)
        fxa.append(fc)
        if fc == 0:
            break
        elif np.sign(fa*fc) < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        i += 1

    xc = (a+b)/2.
    return xa,fxa

f = lambda x: x**3 - 2*(x**2) + (4*x)/3 - (8./27)
x = np.linspace(0.5,0.7,15)
y = []
xa = []
fxa = []
forward_error_grafico = []
backward_error_grafico = []
for i in range(0,len(x)):
    y.append(fun(x[i]))
xa,fxa = bisect(f, 0.5, 0.7)
iteration = []
for i in range(1,16):
    iteration.append(i)

for i in range(0,len(xa)):
    forward_error_grafico.append(abs((2/3.) - xa[i]))
for i in range(0,len(fxa)):
    backward_error_grafico.append(abs((f(2/3.)) - fxa[i]))

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))
ax1.scatter(x, y)
ax1.plot(x,y,label='f (x)')
ax1.set_title('grafica f(x) con 15 puntos en intervalo [0.5 , 0.7]')
ax1.grid(True)
ax1.set_xlabel('eje x')
ax1.set_ylabel('eje y')
ax1.legend(loc=0)

ax2.set_xlabel('Iteration')
ax2.set_ylabel('Error')
ax2.semilogy(iteration, forward_error_grafico ,marker='o', linestyle='--', color='b',label='Forward error')
ax2.semilogy(iteration, backward_error_grafico ,marker='o', linestyle='--', color='r',label='Backward error')
ax2.grid(True)
ax2.set_title('Forward y Backward error con 15 iteraciones de f(x)')
ax2.legend(loc=0)

plt.savefig('images/fig1.pdf', format='pdf')
print(r"""
\begin{figure}[htbp]
    \centering
    \includegraphics[width=18cm]{images/fig1.pdf}
    \label{fig:comparison}
\end{figure}
""")



#205654445 חכים דביר
#201407830אוהד שאול 
#פרוייקט בקורס מולכים למחצה קיץ 2021

import matplotlib.pyplot as plt 
import numpy as np 
import math

b=2*(10**(-10))
h= 6.63 * (10**(-34))
E_max= 100*(1.6*(10**(-19)))
h_bar = (h/ (2*np.pi))
c= 3 *(10**8)
m=9.11*(10**(-31))
p=1.5*np.pi
E= np.linspace(E_max,-E_max,100000)
Beta = (np.sqrt(2*m*E))/h_bar

func=((p/(Beta*b))* np.sin(Beta*b))+ np.cos(Beta*b)
func1 = np.ones(len(Beta))
func2 = func1*-1

plt.figure()
plt.title('energy level singularity')
plt.plot(Beta,func,-Beta,func,Beta,func1,-Beta,func1,Beta,func2,-Beta,func2,color = 'b')       

func1=((p/(Beta*b))* np.sin(Beta*b))+ np.cos(Beta*b)
kd = np.arccos(func1)

plt.figure()
plt.title('energy level bound ')
plt.xlabel('kd')
plt.ylabel('E[J]')
plt.plot(kd,E,'g',-kd,E,'g')

plt.show()
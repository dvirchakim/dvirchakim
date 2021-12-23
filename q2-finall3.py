#205654445 חכים דביר
#201407830אוהד שאול 
#פרוייקט בקורס מולכים למחצה קיץ 2021







# שאלה 2

# הגדרת תיקיות משתמש
import matplotlib.pyplot as plt
import numpy as np
import math

from numpy.typing import _128Bit

#הגדרת משתנים
p=1.5*np.pi
h= 4.135 * (10 ** -15)
H_bar = (h/ (2*np.pi))
c= 3 *(10**8)
m=9.11*(10**(-31))
b=2*(10**(-10))

E_max= 100*(1.6*(10**(-19)))
E= np.linspace(E_max,-E_max,100000)
Beta = (np.sqrt(2*m*E))/H_bar
E = np.linspace(-3,3,num = 600) 
conductionband = 0.56
valenceband = -0.56
m0 = 9.11 * (10 ** -31)
m0 = 5.1099 * (10 ** 5)
H_bar = 4.135 * (10 ** -15) / (2*np.pi)
G_const = ( (m0 ** 3/2) * np.sqrt(2) ) / ( (np.pi**2) * (H_bar**3) )
Gconduction = G_const * np.sqrt(E-conductionband)
Gvalence = G_const * np.sqrt(valenceband-E)
Gconduction[0:357] = 0
Gvalence[242:598] = 0
T = 300
k = 8.62 * (10**-5) 
ENERGYF1 = 0
ENERGYF2 = 0.1
ENERGYF3 = 0.01
Ef4 = -0.1
Ef5 = -0.01


# הגדרת פונקציות
func1 = 1/(1+np.exp((E-ENERGYF1) / (k*T) ))
func2 = 1/(1+np.exp((E-ENERGYF2) / (k*T) ))
func3 = 1/(1+np.exp((E-ENERGYF3) / (k*T) ))
func4 = 1/(1+np.exp((E-Ef4) / (k*T) ))
func5 = 1/(1+np.exp((E-Ef5) / (k*T) ))


elec_num1 = func1*Gconduction   
elec_num2 = func2*Gconduction  
elec_num3 = func3*Gconduction   
elec_num4 = func4*Gconduction   
elec_num5 = func5*Gconduction   
hole_num1 = (1-func1)*Gvalence  
hole_num2 = (1-func2)*Gvalence    
hole_num3 = (1-func3)*Gvalence  
hole_num4 = (1-func4)*Gvalence   
hole_num5 = (1-func5)*Gvalence   

#הדפסת גרפים

plt.figure(1)
plt.xlabel(' states density [1/(ev*cm^3)]')
plt.ylabel('Energy [ev]')
plt.title('states density for electrons and Holes =300K')
plt.plot(Gconduction,E,'r',Gvalence,E,'g')

plt.show()

plt.figure(2)
plt.title('Fermi Function=300K')
plt.xlabel('f(E)')
plt.ylabel('E[ev]')
plt.axis([-0.1,1.1,-0.2,0.3])
plt.plot(func1,E,label = 'Ef = 0')
plt.plot(func2,E,label = 'Ef = 0.1')
plt.plot(func3,E,label = 'Ef = 0.01')

plt.show()

plt.figure(3)
plt.title('Fermi Function=300k')
plt.xlabel('f(E)')
plt.ylabel('E[ev]')
plt.axis([-0.1,1.1,-0.4,0.3])
plt.plot(func4,E,label = 'Ef = -0.1')
plt.plot(func5,E,label = 'Ef = -0.01')

plt.show()

plt.figure(4)
plt.xlabel('electrons and holes concentration=300k')
plt.ylabel('E')
plt.title('Fermi function energy as holes and electrons= 0=300k')
plt.plot(elec_num1,E,label = 'elec_num1',color = 'b')
plt.plot(hole_num1,E,label = 'hole_num1',color = 'r')

plt.show()

plt.figure(5)
plt.xlabel('electrons and holes concentration=300k')
plt.ylabel('E')
plt.title('Fermi function energy as holes and electrons = 0.1[ev]=300k')
plt.plot(elec_num2,E,label = 'elec_num2',color = 'b')
plt.plot(hole_num2,E,label = 'hole_num2',color = 'r')

plt.show()

plt.figure(6)
plt.xlabel('electrons and holes concentration=300k')
plt.ylabel('E')
plt.title('Fermi function energy as holes and electrons = 0.01[ev]=300k')
plt.plot(elec_num3,E,label = 'elec_num3',color = 'b')
plt.plot(hole_num3,E,label = 'hole_num3',color = 'r')

plt.show()

plt.figure(7)
plt.xlabel('electrons and holes concentration=300k')
plt.ylabel('E')
plt.title('Fermi function energy as holes and electrons = -0.1[ev]=300k')
plt.plot(elec_num4,E,label = 'elec_num4',color = 'b')
plt.plot(hole_num4,E,label = 'hole_num4',color = 'r')

plt.show()

plt.figure(8)
plt.xlabel('electrons and holes concentration=300k')
plt.ylabel('E')
plt.title('Fermi function energy as holes and electrons= -0.01[ev]=300k')
plt.plot(elec_num5,E,label = 'elec_num5',color = 'b')
plt.plot(hole_num5,E,label = 'hole_num5',color = 'r')

plt.show()



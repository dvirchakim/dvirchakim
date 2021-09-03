#הגדרת ספריות
from KP_solution import eband_kp
import numpy as np
import matplotlib as plt 
from KP_solution import KPM_soln,eband_kp

#משתנים
a=2.7
b=2.7
U0=5
eps_range =6 

epslist, f_eps = KPM_soln(a,b,U0,eps_range)
k, eps = eband_kp(epslist,f_eps)

klist = np.linespace(0,eps_range,10)
klist_min=klist*0-1
klist_max=klist*0+1

plt.figure(1,dpi=120)
plt.title("kronig-penny solution")
plt.xlabal("$\epsilon$")
plt.ylabel("f($\epsilon$)")
plt.ylim(-5,5)
plt.plot(epslist,f_eps,label="LHS")
plt.plot(klist,klist_min,linestyle="dashed",color="grey",label="RHS")
plt.plot(klist,klist_max,linestyle="dashed",color="grey")
plt.legend()


plt.fugure(2,dpi=120)
plt.title("kronig-penny energy bands")
plt.xlabel(r' k / $ \ frac{\pi}{(a+b)}$')
plt.ylabel("$\epsilon&")







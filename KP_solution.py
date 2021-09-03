

import numpy as np 

def KPM_soln(a,b,U0,eps_range):

    h_bar = 1.055*1e-34
    m = 9.109*1e-31
    alpha_0 = (2*m*U0*1.602*1e-19/h_bar**2)**(1/2)
   

    def KPM_p(eps):
       return (1-2*eps)/(2*(eps*(eps-1))**(1/2))*np.sin(alpha_0*a*1e-10*eps**(1/2))*np.sin(alpha_0*b*1e-10*(eps-1)**(1/2))+np.cos(alpha_0*a*1e-10*eps**(1/2))*np.cosh(alpha_0*b*1e-10*(1-eps)**(1/2))

    def KPM_m(eps):
        return ( (1-2*eps)/(2*(eps*(1-eps))**(1/2))*np.sin(alpha_0*a*1e-10*eps**(1/2))*np.sinh(alpha_0*b*1e-10*(1-eps)**(1/2))+np.cos(alpha_0*a*1e-10*eps**(1/2))*np.cosh(alpha_0*b*1e-10*(1-eps)**(1/2)))

    epslist = np.linespace(0,eps_range,200000)
    f_eps = np.piecewise(epslist, [epslist < 1 , epslist > 1],[KPM_m,KPM_p])

    return epslist , f_eps


def eband_kp(epslist,f_eps):
    k=[]
    bandlist=[]
    Eps=[]
    epsbuildlist=[]
    for i in range(len(f_eps)-1):
        if 1 >= f_eps[i] >=-1:
           bandlist.append(f_eps[i])
           epsbuildlist.append(epslist[i])
           if(1<f_eps[i+1] or -1>f_eps[i+1]):
             k.append(bandlist)
             Eps.append(epsbuildlist)
             bandlist=[]
             epsbuildlist=[]

    for i in range(len(k)):
        k[i]=np.arccos(k[i])/np.pi    
        if i % 2 == 0:
          Eps[i]=np.concatenate((Eps[i][::-1],Eps[i][::1]))
          k[i]=np.concatenate((-1*np.array(k[i],dtype=float)[::-1],k[i][::1]))
        else:
          k[i]=np.concatenate((k[i][::1],-1*np.array(k[i],dtype=float)[::-1]))
          Eps[i]=np.concatenate((Eps[i][::1],Eps[i][::-1]))
           
          return k ,Eps







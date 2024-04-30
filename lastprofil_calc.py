import numpy as np


def lastprofil_calc(n, Qa, Tmax, Tmin, Tmhp, Tu):
    'Belastungsgrad:'
    b=8760*(Tmax-Tmhp)/(Tmax-Tmin)
    'max. Erzeugerleistung' 
    Qmax=Qa*0.92/b #kW
    lastprofil = np.empty([8760,])
    for iteration in range(10000):                         
        for i in range(8760):
            lastprofil[i] = Qmax*(1-(Tu[i]-Tmin)/(Tmax-Tmin))**n
            
        n += 0.0001    
        if abs(np.nansum(lastprofil)-Qa) < 100:
            break        
        elif iteration >= 8759:
            lastprofil = np.zeros([8760,])
            print('Es konnte kein passender Wert für n gefunden werden')
            break
        
    print('n =', n)
    print('Total Energy Load =', np.nansum(lastprofil))
    return lastprofil
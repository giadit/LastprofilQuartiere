import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from heizgrenztemp import Heizgrenztemperatur
from plot import plotload

data = pd.read_csv('data_OBS_DEU_PT1H_T2M.csv', index_col=False, usecols=[2,3], nrows=8760)

Tu= data['Wert'].to_numpy()
'Jährlicher Wärmeverbrauch'
Qa=831000 #kWh/a

'mittlere Temperatur Heizperiode:'
Tmhp=data.mean(numeric_only=True).iloc[0]
'Auslegungstemperatur'
Tmin=data.min(numeric_only=True).iloc[0]
'Heizgrenztemperatur'
Tmax = Heizgrenztemperatur()

'Belastungsgrad:'
b=8760*(Tmax-Tmhp)/(Tmax-Tmin)
'max. Erzeugerleistung' 
Qmax=Qa*0.92/b #kW
lastprofil = np.empty([8760,])
n=1.5
for iteration in range(10000):                         
    for i in range(8760):
        lastprofil[i] = Qmax*(1-(Tu[i]-Tmin)/(Tmax-Tmin))**n
    if abs(np.nansum(lastprofil)-Qa) < 100:
        break
    n += 0.0001
'Lastprofil Plotten:'
plotload(lastprofil)  

print('n =', n)
print('Total Energy Load =', np.nansum(lastprofil))
plotload(lastprofil)
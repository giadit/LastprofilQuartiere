import pandas as pd
import numpy as np 

from plot import plotload
from quartier_erstellung import quartier_setup_k
from quartier_erstellung import quartier_setup_z
from lastprofil_calc import lastprofil_calc

data = pd.read_csv('data/data_OBS_DEU_PT1H_T2M.csv', index_col=False, usecols=[2,3], nrows=8760)

Tu= data['Wert'].to_numpy()
'Jährlicher Wärmeverbrauch'

Qa_k = quartier_setup_k()
Qa_z = quartier_setup_z()


'mittlere Temperatur Heizperiode:'
Tmhp=data.mean(numeric_only=True).iloc[0]
'Auslegungstemperatur'
Tmin=data.min(numeric_only=True).iloc[0]

n = float(input('Geben sie einen Anfangswert für n (<1.9) ein: '))
last_k = lastprofil_calc(1.5, Qa_k, 15, Tmin, Tmhp, Tu)
last_z = lastprofil_calc(n, Qa_z, 12, Tmin, Tmhp, Tu)

lastprofil = last_k + last_z

np.savetxt('results/loadprofile.csv', lastprofil, fmt='%1.3f', delimiter=',')
plotload(lastprofil)  

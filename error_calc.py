import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data_OBS_DEU_PT1H_T2M.csv', index_col=False, usecols=[2,3], nrows=8760)

Tu= data['Wert'].to_numpy()
'mittlere Temperatur Heizperiode:'
Tmhp=data.mean(numeric_only=True).iloc[0]
'Auslegungstemperatur'
Tmin=data.min(numeric_only=True).iloc[0]

Qa_k = 615.9*111*5
Qa_z = 615.9*34*5

b_k = 8760*(15-Tmhp)/(15-Tmin)
Qmax_k = Qa_k *0.92/b_k #kW
b_z = 8760*(12-Tmhp)/(12-Tmin)
Qmax_z = Qa_z *0.92/b_z #kW

lastprofil_k = np.empty([8760,])
lastprofil_z = np.empty([8760,])
#n = np.arange(0.5, 1.50001, 0.0001)

n = 0.5
n_array = []
err_k = []
err_z = []

for iteration in range(40001):
    n_array.append(n)
    for i in range(8760):
        lastprofil_k[i] = Qmax_k * (1 - (Tu[i] - Tmin) / (15 - Tmin)) ** n
        lastprofil_z[i] = Qmax_z * (1 - (Tu[i] - Tmin) / (12 - Tmin)) ** n
    n += 0.0001
    err_k.append(abs(np.nansum(lastprofil_k) - Qa_k))
    err_z.append(abs(np.nansum(lastprofil_z) - Qa_z))

zero = np.zeros([len(n_array),])

fig, ax = plt.subplots()
fig.set_size_inches(10,8)
ax.plot(n_array, zero, color = 'r' )
ax.plot(n_array, err_k, label = 'konventionell saniert')
ax.plot(n_array, err_z, label = 'zukunft. saniert')
ax.set_xticks(np.arange(0.5,4.6,0.1))
ax.legend()
ax.set_ylabel('Error Amount')
ax.set_xlabel('n-Value')

plt.savefig('results/error_calc_fig_2.png')
plt.show()

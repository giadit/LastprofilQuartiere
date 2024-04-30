import matplotlib.pyplot as plt
import numpy as np

def plotload(lastprofil):
    hours = np.arange(1, 8761)
    plt.plot(hours, lastprofil)

    plt.xlabel('Hour')
    plt.ylabel('Thermal Energy Load')
    plt.title('Load Profile')
    
    np.savetxt('loadprofile.csv', lastprofil, fmt='%1.3f', delimiter=',')

    plt.grid(True)
    plt.tight_layout()
    plt.show()
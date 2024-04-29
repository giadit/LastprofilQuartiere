# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:50:54 2024

@author: Giampaolo.DiTomassi
"""

def Heizgrenztemperatur():
    var = input('Ist die Wohnung zukunftsweisend saniert (z) oder konventionell saniert (k)?  ')
    if var == 'z':
            return 12
    elif var == 'k':
            return 15
    else:
            print('Bitte geben Sie einen gültigen Wert ein')
            return Heizgrenztemperatur()
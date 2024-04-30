import pandas as pd 
import numpy as np


def quartier_setup_k():
    data_k = pd.read_csv('DatenIWU2015.csv', sep=';', engine='python', index_col=False, skipfooter = 10, encoding='latin-1' )
    m2_k = data_k['beheizte Wohnfläche [m2]'].to_numpy()
    kW_k = data_k['Wärmeverbrauch Heizung [kWh/m2a]'].to_numpy()
    
    Qa = 0 
    while True:
        var = input('Wollen Sie konventionell sanierte Wohnungen zum Quartier hinzufügen? (y/n) ')
        
        if var == 'y':
            letter = input('Wähle das Gebäudetyp (A-J): ')
            letter = letter.lower()
            number = ord(letter) - 97
            if number >= 10:
                print('Fehler bei der Eingabe')
                continue
            n = int(input('Wie viele dieser Gebäude befinden sich im Quartier? ') )   
            
            Qa += n*kW_k[number]*m2_k[number]	
        
        elif var == 'n':         
            break
        else:
            print('Error: Falsche Eingabe')
    return Qa

def quartier_setup_z():
    data_z = pd.read_csv('DatenIWU2015.csv', sep=';', engine='python', index_col=False, names=['Gebäudetyp',
                                                                              'beheizte Wohnfläche [m2]',
                                                                              'Wärmeverbrauch Heizung [kWh/m2a]'] 
                         , skiprows = 10, encoding='latin-1' )
    m2_z = data_z['beheizte Wohnfläche [m2]'].to_numpy()
    kW_z = data_z['Wärmeverbrauch Heizung [kWh/m2a]'].to_numpy()
    
    Qa = 0 
    while True:
        var = input('Wollen Sie zukunftsweisend sanierte Wohnungen zum Quartier hinzufügen? (y/n) ')
        
        if var == 'y':
            letter = input('Wähle das Gebäudetyp (A-J): ')
            letter = letter.lower()
            number = ord(letter) - 97
            if number >= 10:
                print('Fehler bei der Eingabe')
                continue
            n = int(input('Wie viele dieser Gebäude befinden sich im Quartier? ') )   
            
            Qa += n*kW_z[number]*m2_z[number]	
        
        elif var == 'n':         
            break
        else:
            print('Error: Falsche Eingabe')
    return Qa
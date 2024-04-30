# LastprofilQuartiere
This script utilizes the outside temperature data from the DWD to calculate a load profile for a distric (specifically for districts in Berlin).

It allows the user to "build" their disctrict out of different apartment complexes through data from the IWU 
> [!NOTE]  
> The input prompts are in german, as this script was initially intended to calculate the results from a german M.Sc thesis.
> As such this README might also contain german terms for the theory section.

## How to run
Download and run main.py from your IDE of choice.

## How it works
The script asks the user for input on which building typology they would like to add and how many should be added.
At the moment only apartment buildings are supported.
Through this input the script sums up the required yearly heating load as new buildings are added.

The script then uses the yearly heating load to calculate the maximum power provided by the heaters.
That maximum power is then used in a simplified "Heizkörpergleichung" that calculates how much power the heater needs to produce based on outside temperature.
The exponent "n" (Heizkörperexponent) is iteratively determined by calculating a value for each hour of the year and then comparing the sum to the yearly heating load.


from Assignment1Data import *
import numpy as np
import matplotlib.pyplot as plt

# ================
# Global Settings
DeltaT = 3600   # s
# ================

# 1) Formulate a differential equation for NOx that includes the emissions and the NOx lifetime.

# 2) Give the formulas for converting
# a. volume mixing ratios into kg in the box.
# b. Air density in molec/cm3
# 3) Solve the differential equation by using the initial values as given. You may want to use the
# recommended 1-hour time step and the semi-implicit integration scheme. Use the units
# molec/cm3, as normally used in atmospheric chemistry and plot the temporal evolution of
# NOx over the 30 days in units kgN/box. Don’t forget to explain your steps (briefly).


# TODO Change units to molec/cm3
# 

NOx = Data['InitialValues']['NOxInitialValue']
NOxLog = [NOx]

# Run the simulation of the first period over the ocean
TimeOcean1 = 5*24*3600
for t in range(0,TimeOcean1,DeltaT):
    NOx = float(NOx * np.exp(-DeltaT/(Data['LifeTimeConstants']['NOxLifeTime']*24*3600)))
    NOxLog.append(NOx)

# Run the simulation of the period over land
TimeLand = 15*24*3600
MolsInBox = 1000**3*Data['EnvironmentalConstants']['AirDensity']/Data['MolecularMasses']['MolWeightAir']
# Assume that the molecular mass of NOx is the same as NO2
MolecularMassNOx = 1*Data['MolecularMasses']['MolWeightN'] + 2*Data['MolecularMasses']['MolWeightO']
MolsNOxPerDay = Data['EmissionConstants']['NOxEmissionLand'] / MolecularMassNOx
for t in range(0,TimeLand,DeltaT):
    NOx = float(NOx * (1 * np.exp(-DeltaT/(Data['LifeTimeConstants']['NOxLifeTime']*24*3600))) + ((MolsNOxPerDay/(24*3600)) * 10**12 / MolsInBox)*DeltaT)
    NOxLog.append(NOx)

# Run the simulation of the second period over the ocean
TimeOcean2 = 10*24*3600
for t in range(0,TimeOcean2,DeltaT):
    NOx = float(NOx * np.exp(-DeltaT/(Data['LifeTimeConstants']['NOxLifeTime']*24*3600)))
    NOxLog.append(NOx)

plt.plot(NOxLog)
plt.show()


# 4) How does the mass of other gases as CO and CH4 behave when transported in the same box?
# Do no calculation, just explain how the curve would look like and give reasons.
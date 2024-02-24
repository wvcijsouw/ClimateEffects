import numpy as np
from Assignment1Data import *

# ================
# Global Settings
DeltaT = 3600   # s
# ================

# Formulate differential equations for the temporal evolution of the concentration of O3 in the
# considered air parcel and use the following set of chemical reactions.
# NO + HO2 → NO2 + OH (leading to O3) (6)
# O3 + HO2 → 2 O2 + OH (7)
# O3 + OH → O2 + HO2 (8)

# Sooo O2 and O3 are the only ones that are varying

# Equation 6 is actually the reaction
# NO + HO2 -hv O2-> NO + OH + O3

# NOx needs to be imported from 1A
from Assignment1A import NOxLog


def SystemEvolution(O2,O3,NO,HO2,OH,DeltaT=DeltaT):
    dO2dt = 2*O3_HO2_to_2O2_OH()*O3*HO2 + O3_OH_to_O2_HO2()*O3*OH - NO_HO2_to_NO_OH_O3()*NO*HO2
    dO3dt = NO_HO2_to_NO_OH_O3()*NO*HO2 - O3_HO2_to_2O2_OH()*O3*HO2 - O3_OH_to_O2_HO2()*O3*OH
    dNOdt = NO_HO2_to_NO_OH_O3()*NO*HO2 - NO_HO2_to_NO_OH_O3()*NO*HO2 # So 0
    dHO2dt = O3_OH_to_O2_HO2()*O3*OH - O3_HO2_to_2O2_OH()*O3*HO2 - NO_HO2_to_NO_OH_O3()*NO*HO2
    dOHdt = NO_HO2_to_NO_OH_O3()*NO*HO2 + O3_HO2_to_2O2_OH()*O3*HO2 - O3_OH_to_O2_HO2()*O3*OH
    return float(dO2dt*DeltaT), float(dO3dt*DeltaT), float(dNOdt*DeltaT), float(dHO2dt*DeltaT), float(dOHdt*DeltaT)

O2 = 100
O3 = 10
NO = 10
HO2 = 10
OH = 10
O2Log = [O2]
O3Log = [O3]
NOLog = [NO]
HO2Log = [HO2]
OHLog = [OH]

for i in range(0,72*DeltaT,DeltaT):
    O2,O3,NO,HO2,OH = SystemEvolution(O2,O3,NO,HO2,OH)
    O2Log.append(O2)
    O3Log.append(O3)
    NOLog.append(NO)
    HO2Log.append(HO2Log)
    OHLog.append(OH)

# 2) Plot the net ozone production (=ozone production – ozone loss) in molec/cm3
# /s on the y-axis
# for all land data (excluding the first 5 and last 10 days) against the NOx volume mixing ratio
# (mol/mol on the x-axis). Use the differential equation for ozone set up in C.1) and the
# temporal evolution of the NOx calculated in A. 3). Apply a logarithmic x-axis. Plot also the
# individual production and loss terms of the net ozone production in the same manner.
# 3) There are three important different chemical regimes that can be seen in the plot. Identify
# them and the responsible chemical reaction. Additionally, explain how these regimes
# develop and how the chemical reactions interact.
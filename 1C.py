import numpy as np
import matplotlib.pyplot as plt
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


def O3Evolution(O3,NO,HO2,OH,DeltaT=DeltaT):
    # dO2dt = 2*O3_HO2_to_2O2_OH()*O3*HO2 + O3_OH_to_O2_HO2()*O3*OH - NO_HO2_to_NO_OH_O3()*NO*HO2
    P = NO_HO2_to_NO_OH_O3()*NO*HO2
    D = O3_HO2_to_2O2_OH()*O3*HO2 + O3_OH_to_O2_HO2()*O3*OH
    # dNOdt = NO_HO2_to_NO_OH_O3()*NO*HO2 - NO_HO2_to_NO_OH_O3()*NO*HO2 # So 0
    # dHO2dt = O3_OH_to_O2_HO2()*O3*OH - O3_HO2_to_2O2_OH()*O3*HO2 - NO_HO2_to_NO_OH_O3()*NO*HO2
    # dOHdt = NO_HO2_to_NO_OH_O3()*NO*HO2 + O3_HO2_to_2O2_OH()*O3*HO2 - O3_OH_to_O2_HO2()*O3*OH
    # return float(O3+dO3dt*DeltaT), float(NO+dNOdt*DeltaT), float(HO2+dHO2dt*DeltaT), float(dOHdt*DeltaT)
    return P*DeltaT, D*DeltaT

MolecAir1cm3 = (Data['EnvironmentalConstants']['AirDensity']*0.01**3/Data['MolecularMasses']['MolWeightAir'])*Data['PhysicalConstants']['AvogadoConstant']

O3 = MolecAir1cm3*Data['InitialValues']['OzoneInitialValue']*10**-9
NO = NOxLog[0]*(0.3/1.3)
HO2 = Data['ConstantValues']['HO2Value']
OH = Data['ConstantValues']['OHValue']
O3Log = []
O3PLog = []
O3DLog = []
NetProduction = []

# NOLog = [NO]
# HO2Log = [HO2]
# OHLog = [OH]

for NOx in NOxLog:
    NO = NOx*(0.3/1.3)
    P, D = O3Evolution(O3, NO, HO2, OH)
    O3 += P - D
    O3Log.append(O3)
    O3PLog.append(P)
    O3DLog.append(D)
    NetProduction.append(P-D)




# 2) Plot the net ozone production (=ozone production – ozone loss) in molec/cm3
# /s on the y-axis
# for all land data (excluding the first 5 and last 10 days) against the NOx volume mixing ratio
# (mol/mol on the x-axis). Use the differential equation for ozone set up in C.1) and the
# temporal evolution of the NOx calculated in A. 3). Apply a logarithmic x-axis. Plot also the
# individual production and loss terms of the net ozone production in the same manner.
# 3) There are three important different chemical regimes that can be seen in the plot. Identify
# them and the responsible chemical reaction. Additionally, explain how these regimes
# develop and how the chemical reactions interact.
    

# plt.plot(O3Log[0:20*24])
# plt.show()
    
# plt.plot(O3PLog[5*24:20*24],label='Production')
# plt.plot(O3DLog[5*24:20*24],label='Loss')
# plt.plot(NetProduction[5*24:20*24],label='Net')
# plt.legend()
# plt.show()
    
MMRNOx = [NOx*10**6*48/Data['EnvironmentalConstants']['AirDensity']/Data['PhysicalConstants']['AvogadoConstant'] for NOx in NOxLog]
VMRNOx = [MMR*29/48 for MMR in MMRNOx]

# plt.xlog(NetProduction[5*24:20*24],VMRNOx[5*24:20*24])
# plt.show()(

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
line, = ax.plot(VMRNOx[5*24:20*24],NetProduction[5*24:20*24])
ax.set_xscale('log')
plt.show()
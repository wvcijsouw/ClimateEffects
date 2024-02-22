import numpy as np
from Assignment1Data import *

# Formulate differential equations for the temporal evolution of the concentration of O3 in the
# considered air parcel and use the following set of chemical reactions.
# NO + HO2 → NO2 + OH (leading to O3) (6)
# O3 + HO2 → 2 O2 + OH (7)
# O3 + OH → O2 + HO2 (8)

# Sooo O2 and O3 are the only ones that are varying



# 2) Plot the net ozone production (=ozone production – ozone loss) in molec/cm3
# /s on the y-axis
# for all land data (excluding the first 5 and last 10 days) against the NOx volume mixing ratio
# (mol/mol on the x-axis). Use the differential equation for ozone set up in C.1) and the
# temporal evolution of the NOx calculated in A. 3). Apply a logarithmic x-axis. Plot also the
# individual production and loss terms of the net ozone production in the same manner.
# 3) There are three important different chemical regimes that can be seen in the plot. Identify
# them and the responsible chemical reaction. Additionally, explain how these regimes
# develop and how the chemical reactions interact.
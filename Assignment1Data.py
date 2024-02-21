from numpy import exp, log

# Copy of the first data table of assignment 1

Data = {

'EmissionConstants': 
{
'NOxEmissionOcean': 0.0,        # kgN/day
'NOxEmissionLand': 0.12,        # kgN/day
'COEmissionOcean': 0.0,         # kg/day
'COEmissionLand': 14.0,         # kg/day
'CH4EmissionOcean': 0.0,        # kg/day
'CH4EmissionLand': 0.21         # kg/day
},


'LifeTimeConstants': 
{
'NOxLifeTime': 1.5              # days
},


'InitialValues' : 
{
'NOxInitialValue': 15,          # pptv
'COIntialValue': 130,           # ppbv
'CH4InitialValue': 2100,        # ppbv
'OzoneInitialValue': 40         # ppbv
},


'ConstantValues' : 
{
'OHValue' : 1.8e6,              # molec/cm3
'HO2Value' : 510e6              # molec/cm3
},


'MoleculeRatios' : 
{
'RatioO3PtoO3' : 5.0e-6         # -
},


'EnvironmentalConstants' : 
{
'AirDensity' : 1.0,             # kg/m3
'Temperature' : 298             # K
},


'PhysicalConstants' : 
{
'AvogadoConstant' : 6.02E26    # molec/kmol
},

'MolecularMasses' : 
{
'MolWeightAir' : 29,            # kg/kmol
'MolWeightH' : 1,               # kg/kmol
'MolWeightC' : 12,              # kg/kmol
'MolWeightN' : 14,              # kg/kmol
'MolWeightO' : 16,              # kg/kmol
}
}


# Reaction Rate Constants

def CO_OH_to_H_CO2(c_air=(Data['EnvironmentalConstants']['AirDensity'] /
                         Data['MolecularMasses']['MolWeightAir'])*
                         Data['PhysicalConstants']['AvogadoConstant'] /
                         1e6):
    """Determines the reaction rate constant of the reaction \\
    CO + OH --> H + CO2

    Args:
        c_air (float, optional): Air density in molec/cm3. Defaults to (Data['EnvironmentalConstants']['AirDensity'] /
                                                                        Data['MolecularMasses']['MolWeightAir']) *
                                                                        Data['PhysicalConstants']['AvogadoConstant'] /
                                                                        1e6.

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """    
    return 1.57E-13 + c_air*3.54e-33


def CH4_OH_to_CH3_H2O(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    CH4 + OH --> CH3 + H2O

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """
    return 1.85E-20 * exp(2.82 * log(T) - (987/T))


def NO_HO2_to_NO_OH_O3(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    NO + HO2 -(hv O2)-> NO + OH + O3 \\
    
    (Resultant reaction, actual reaction is\\
    NO + HO2 --> NO2 + OH\\
    NO2 + hv --> NO + O\\
    O + O2 --> O3)

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """    
    return 3.3E-12 * exp(270.0/T)

def O3_OH_to_O2_HO2(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    O3 + OH --> O2 + HO2

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """
    return 1.7E-12 * exp(-940.0/T)


def O3_HO2_to_2O2_OH(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    O3 + HO2 --> 2 O2 + OH

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """
    return 1.0E-14 * exp(-490.0/T)


def NO_O3_to_NO2_O2(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    NO + O3 --> NO2 + O2

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """
    return 3.0E-12 * exp(-1500.0/T)


def NO2_O3P_to_NO_O2(T=Data['EnvironmentalConstants']['Temperature']):
    """Determines the reaction rate constant of the reaction \\
    NO2 + O(^3P) --> NO + O2

    Args:
        T (float, optional): Temperature in Kelvin. Defaults to Data['EnvironmentalConstants']['Temperature'].

    Returns:
        float: Reaction rate constant in cm3 / (molec * s)
    """
    return 5.1E-12 * exp(210.0/T)


def NO2_hv():
    """Determines the reaction rate constant of\\
    NO2 + hv

    Returns:
        float: Reaction rate constant in 1 / s
    """
    return 5.0E-3
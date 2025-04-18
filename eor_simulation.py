#%%

"""
Reservoir: Douala Basin, Cameroon
Lithology: Interbedded Lower Cretaceous Sandstone and Shale
Porosity: ~20%
Permeability: 100–500 mD
Trap Mechanism: Structural and stratigraphic
Crude Type: Light to medium
Primary Recovery Factor: 20–30%
Expected with EOR: up to ~50–60%
"""
import numpy as np
import matplotlib.pyplot as plt

# Define the oil recovery function
def oil_recovery(R_max, k, PVI_50, PVI):
    '''
    Simulate oil recovery using a logistic growth model.

    Parameters:
    - R_max: Maximum recovery factor (e.g. 0.8 for 80%)
    - k: Slope of the curve (how fast recovery increases)
    - PVI_50: PVI value at which 50% of R_max is recovered
    - PVI: Array of PVI values (pore volume injected)

    Returns:
    - R: Array of oil recovery values for each PVI
    '''
    R = R_max / (1 + np.exp(-k * (PVI - PVI_50)))
    return R

# Simulate pore volume injected and range
PVI = np.linspace(0, 5, 100)  # PVI from 0 to 5

# Gas injection parameters

gases = {
    'CO₂': {'R_max': 0.60, 'k': 3.0, 'PVI_50': 2.2},
    'CH₄': {'R_max': 0.52, 'k': 2.3, 'PVI_50': 2.4},
    'N₂':  {'R_max': 0.45, 'k': 2.8, 'PVI_50': 2.6},
}


plt.figure(figsize=(10, 6))
for gas, params in gases.items():
    R = oil_recovery (**params, PVI=PVI)
    plt.plot(PVI, R, label=f"{gas} Injection")


# Result
plt.title("Enhanced Oil Recovery Simulation for Douala Basin Reservoir")
plt.xlabel("Pore Volume Injected (PVI)")
plt.ylabel("Oil Recovery Factor")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %%

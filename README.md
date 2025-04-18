# Enhanced Oil Recovery Simulation – Douala Basin, Cameroon 

This project simulates enhanced oil recovery (EOR) performance using gas injection in a sandstone reservoir based on real-world parameters from the **Douala Basin** in Cameroon.

## 🛢️ Reservoir Background

- **Location**: Douala Basin, Southern Cameroon  
- **Formation**: Lower Cretaceous Sandstone & Shale  
- **Porosity**: ~20%  
- **Permeability**: 100–500 mD  
- **Trap Type**: Structural with stratigraphic components  
- **Crude Type**: Light to medium oil  
- **Typical Recovery Factor**:
  - Primary: 20–30%
  - Enhanced: 50–60% (via gas injection)

This reservoir was chosen for its real-world relevance, representing a moderately heterogeneous sandstone reservoir environment in a key hydrocarbon-producing region.



##  Project Objective

To **simulate and compare** the oil recovery performance of three gases used in EOR:
- CO₂ (Carbon Dioxide)
- CH₄ (Methane)
- N₂ (Nitrogen)

Each gas was modeled using a **logistic oil recovery function** based on realistic values of recovery factor, efficiency, and injection volume.



## Methodology

### Oil Recovery Function:
The model uses a sigmoid function to estimate oil recovery as a function of pore volume injected (PVI):

```python
R = R_max / (1 + exp(-k * (PVI - PVI_50)))

Where:

    R_max = Maximum recovery factor

    k = Curve steepness (efficiency of gas)

    PVI_50 = Pore volume at which 50% of R_max is achieved

Parameters Used

Gas	R_max	k	PVI_50	Notes
CO₂	0.60	3.0	2.2  	High miscibility & swelling
CH₄	0.52	2.3	2.4	  Moderate miscibility
N₂	0.45	2.8	2.6	  Limited miscibility


Results

The plot basically illustrates how each gas enhances recovery over time (PVI). CO₂ injection yields the highest recovery, while N₂ performs the least due to low miscibility with the reservoir oil.

    This result aligns with field evidence supporting CO₂ as the most effective gas for EOR in light-medium oil sandstone reservoirs.

Key Takeaways

    Realistic modeling of oil recovery is possible using Python.

    Reservoir characteristics heavily influence the effectiveness of different gases.


    This project helped me develop early-stage skills in:

        Petroleum reservoir modeling

        Python simulation

        Data visualization

        Research and documentation of basin-specific geological data

Future Work

    Expand model to include pressure, viscosity, or heterogeneity variables.

    Integrate with real field data or core samples.

    Extend simulation to carbonate reservoirs in the Logbaba or Rio del Rey basins.

Author

Mbole Ngome-Ngome
Petroleum & Natural Gas Engineering (B.Sc)
Aspiring Chemical Engineer | Python Learner | 🇨🇲 | Based in Dortmund, Germany
💬 Connect with Me

    LinkedIn

    GitHub

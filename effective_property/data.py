"""Material-property database and test matrix for water-based nanofluids.

Units: density [kg/m^3], viscosity [Pa.s], conductivity [W/(m.K)],
specific heat [J/(kg.K)] (water and nanoparticles are now consistent).
If you previously multiplied Cp_w by 1000 at the call site, drop that
factor -- it is no longer needed.

Sources for every value below are documented in reference.md.
"""


# ============================ Water (base fluid) ==========================
# Standard saturated-liquid water properties at 1 atm (textbook tables,
# e.g. Incropera & DeWitt Table A.6; Engineering Toolbox / ThermExcel).
# Keyed by temperature [degC]. Fields: density [kg/m^3], viscosity [Pa.s],
# cp [J/(kg.K)], conductivity [W/(m.K)].
water_properties = {
    20: {"density": 998.21, "viscosity": 1.002e-3, "cp": 4185, "conductivity": 0.598},
    25: {"density": 997.10, "viscosity": 8.91e-4,  "cp": 4179, "conductivity": 0.613},
    30: {"density": 995.65, "viscosity": 0.797e-3, "cp": 4180, "conductivity": 0.616},
    40: {"density": 992.22, "viscosity": 0.653e-3, "cp": 4179, "conductivity": 0.631},
    50: {"density": 988.05, "viscosity": 0.547e-3, "cp": 4180, "conductivity": 0.644},
    60: {"density": 983.21, "viscosity": 0.466e-3, "cp": 4183, "conductivity": 0.654},
    70: {"density": 977.78, "viscosity": 0.404e-3, "cp": 4188, "conductivity": 0.663},
    80: {"density": 971.80, "viscosity": 0.354e-3, "cp": 4196, "conductivity": 0.670},
}

# ============================== Nanoparticles ========================================
# Keyed by lowercase name. Fields: density [kg/m^3], Cp [J/(kg.K)],
# k [W/(m.K)], lamda (empirical length-scale param, currently unused).

nanoparticles = {
    
    "al2o3": {"density": 3970, "Cp": 765,   "k": 40,    "lamda": 0.85e-5}, # rho/Cp match Kaya (2022), Processes 10(12):2639, Table 1; k=40 is a common modeling value (literature range 25-46).
    "cuo":   {"density": 6500, "Cp": 535.6, "k": 76.5,  "lamda": 0.85e-5}, # Exact set (6500/535.6/76.5) used in Heliyon (2024) property tables; literature k range 20-76.5.
    "h-bn":  {"density": 2270, "Cp": 1610,  "k": 30,    "lamda": 0.40e-5}, # Cp/k match Dhairiyasamy et al. (2025), J. Environ. Nanotechnol. 14(4):54-71, Table 2; rho is the crystallographic h-BN density.
    "tio2":  {"density": 4250, "Cp": 686,   "k": 8.95,  "lamda": 0.90e-5}, # Within AZoM ranges (Cp 683-697, k 4.8-11.8); standard modeling pair.
    "sio2":  {"density": 2200, "Cp": 745,   "k": 1.4,   "lamda": 0.63e-5}, # rho = fused silica; k in AZoM range 1.3-1.5; Cp is the common modeling value.
    "fe3o4": {"density": 5200, "Cp": 670,   "k": 6.0,   "lamda": 1.30e-5}, # Standard magnetite set in ferrofluid modeling (rho 5180-5200, Cp 670, k 6-9.7 across papers).
}

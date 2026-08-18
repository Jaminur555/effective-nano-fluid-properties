# Reference: sources for the material-property values in `data.py`

Checked against published sources on 2026-08-18. Every value in `data.py`
either matches a published table exactly or sits inside the range commonly
used in the nanofluid literature. Overall verdict: **the values are
reasonable** -- they are the standard property sets used across nanofluid
modeling papers. The few places where the literature disagrees are listed
under "Caveats" at the end.

## Water (base fluid)

The table in `data.py` reproduces standard saturated-liquid water properties
at 1 atm -- the same numbers as textbook property tables (e.g. Incropera &
DeWitt, *Fundamentals of Heat and Mass Transfer*, Table A.6) and public
property tables:

- Engineering Toolbox, water thermal properties:
  https://www.engineeringtoolbox.com/water-thermal-properties--d_162.html
- ThermExcel, physical characteristics of water at atmospheric pressure:
  https://www.thermexcel.com/english/tables/eau_atm.htm

Spot checks (`data.py` vs typical table value):

| T [degC] | rho [kg/m^3]        | mu [Pa.s]              | cp [J/kg.K]        | k [W/m.K]      |
|----------|---------------------|------------------------|--------------------|----------------|
| 20       | 998.21 vs 998.2     | 1.002e-3 vs 1.002e-3   | 4185 vs ~4182      | 0.598 vs 0.598 |
| 40       | 992.22 vs 992.2     | 0.653e-3 vs ~0.653e-3  | 4179 vs ~4179      | 0.631 vs ~0.631|
| 80       | 971.80 vs 971.8     | 0.354e-3 vs ~0.355e-3  | 4196 vs ~4196      | 0.670 vs 0.670 |

The cp column also reproduces water's anomalous shallow minimum near
35 degC, which is a good sign the numbers were taken from real data and not
smoothed. (Minor: k = 0.613 at 25 degC matches the common 300 K textbook
row; the IAPWS-08 correlation gives 0.6071, about 1% lower.)

## Nanoparticles

### Al2O3 -- rho 3970, Cp 765, k 40 [data.py]
- rho = 3970 and Cp = 765 match Table 1 of Kaya (2022) exactly:
  Kaya, F., "Numerical Investigation of the Use of Boron Nitride/Water and
  Conventional Nanofluids in a Microchannel Heat Sink," *Processes* 10(12),
  2639, 2022. https://www.mdpi.com/2227-9717/10/12/2639 (doi:10.3390/pr10122639)
- k = 40 is a widely used modeling value; note Kaya uses 25 and other papers
  use 36-46 (see Caveats).
- Related experimental review: "Revisiting Thermo-Physical Property Models of
  Al2O3-Water Nanofluids," PMC10918198: https://pmc.ncbi.nlm.nih.gov/articles/PMC10918198/

### CuO -- rho 6500, Cp 535.6, k 76.5 [data.py]
- The exact set (6500, 535.6, 76.5) is used in published property tables,
  e.g. "Numerical study of the thermal performance of a single-channel"
  (Heliyon, 2024), whose nanoparticle table lists CuO k = 76.5 W/m.K and
  Cp = 535.6 J/kg.K: https://www.sciencedirect.com/science/article/pii/S2405844024114442
- Kaya (2022) (above) lists CuO as 6500 / 536 / 20 -- same density and Cp,
  very different k (see Caveats).

### h-BN -- rho 2270, Cp 1610, k 30 [data.py]
- Cp = 1610 and k = 30 match Table 2 of:
  Dhairiyasamy, R., et al., "Synergistic Enhancement of Automotive Radiator
  Performance Using Coated Surfaces and Hybrid Nanofluids," *J. Environ.
  Nanotechnol.* 14(4), 54-71, 2025, doi:10.13074/jent.2025.12.2531671.
- rho = 2270 kg/m^3 is the standard crystallographic density of hexagonal BN
  (2.27 g/cm^3); the paper above quotes 1.9 g/cm^3 for its coating powder
  (see Caveats). Kaya (2022) uses a different BN set (2300 / 1150 / 52).
- h-BN nanosheet review: https://pmc.ncbi.nlm.nih.gov/articles/PMC12844453/

### TiO2 -- rho 4250, Cp 686, k 8.95 [data.py]
- Within the manufacturer-database ranges of AZoM "Properties: Titanium
  Dioxide - Titania, TiO2": Cp 683-697 J/kg.K, k 4.8-11.8 W/m.K,
  rho (rutile) ~4250 kg/m^3: https://www.azom.com/properties.aspx?ArticleID=1179
- k = 8.95 (often quoted as 8.9538) and rho = 4250 are the standard pair in
  TiO2-nanofluid modeling papers.

### SiO2 -- rho 2200, Cp 745, k 1.4 [data.py]
- rho = 2200 kg/m^3 is the standard fused-silica density; k = 1.4 W/m.K sits
  in the AZoM range 1.3-1.5; Cp = 745 is the common modeling value (AZoM
  lists 680-730 for bulk material -- see Caveats).
- Experimental SiO2/water study: "Thermophysical Properties of Silicon Oxide
  Nanoparticles in Water-Based Nanofluids," *Fluids* 9(11), 261, 2024:
  https://www.mdpi.com/2311-5521/9/11/261

### Fe3O4 -- rho 5200, Cp 670, k 6.0 [data.py]
- Standard magnetite set in ferrofluid modeling (rho 5180-5200, Cp 670,
  k 6-9.7 across papers).
- Experimental context: "Experimental examination of the properties of
  Fe3O4/water nanofluid" (J. Mol. Liq., 2022):
  https://www.sciencedirect.com/science/article/abs/pii/S0167732222026897

## Effective-property model references (for the equations in `effective_properties.py`)

- Mixture rules for rho and rho*Cp: Pak, B.C., Cho, Y.I., "Hydrodynamic and
  heat transfer study of dispersed fluids with submicron metallic oxide
  particles," *Exp. Heat Transfer* 11, 151-170, 1998; and Xuan, Y.,
  Roetzel, W., "Conceptions for heat transfer correlation of nanofluids,"
  *Int. J. Heat Mass Transfer* 43, 3701-3707, 2000.
- Maxwell thermal-conductivity model: Maxwell, J.C., *A Treatise on
  Electricity and Magnetism*, Clarendon Press, Oxford, 1873.
- Brinkman viscosity model: Brinkman, H.C., "The viscosity of concentrated
  suspensions and solutions," *J. Chem. Phys.* 20, 571, 1952,
  doi:10.1063/1.1700493.

## Caveats (where the literature is not settled)

1. **Bulk k of Al2O3 and CuO varies a lot between papers.** Al2O3: 25-46
   W/m.K (data.py uses 40). CuO: 20-76.5 W/m.K (data.py uses 76.5). The
   Maxwell model is sensitive to the k_n/k_w ratio, so when comparing results
   against a specific paper, use that paper's particle k.
2. **h-BN density:** 2270 kg/m^3 (crystallographic, used in data.py) vs
   1.9-2.3 g/cm^3 for commercial powders in coating papers.
3. Nanoparticle properties are treated as temperature-independent, which is
   standard practice in this literature, and the "lamda" field in `data.py`
   is currently unused by any model.

# Effective Nanofluid Properties

A small Python calculator for the effective thermophysical properties of
water-based **mono** (single-particle) and **hybrid** (two-particle)
nanofluids, evaluated at every tabulated base-fluid temperature (20-80 degC).

## Models

| Property                  | Model                                                    |
|---------------------------|----------------------------------------------------------|
| Density `rho_nf`          | Volume-fraction mixture rule                             |
| Specific heat `Cp_nf`     | Energy-weighted mixture rule                             |
| Thermal conductivity `k`  | Maxwell model (spherical particles)                      |
| Dynamic viscosity `mu_nf` | Brinkman model                                           |

For hybrid nanofluids, viscosity applies the Brinkman term per particle and
thermal conductivity uses a two-step Maxwell suspension (particle 1 in water,
then particle 2 in that mixture). All inputs and outputs are in SI units.

## Supported nanoparticles

Al2O3, CuO, h-BN, TiO2, SiO2, Fe3O4 -- properties are defined in `data.py`,
alongside the water base-fluid table keyed by temperature.

## Usage

```bash
python effective_property/solver.py
```

1. Choose **M** (mono) or **D** (hybrid/di) mode.
2. Enter each particle as `<name> <vol%>`, e.g. `al2o3 1.5`.
   The value is divided by 100 and used directly as the particle volume
   fraction `phi` in the models.
3. The program prints density, specific heat, thermal conductivity, and
   viscosity at each tabulated temperature.

## Files

| File                                   | Purpose                       |
|----------------------------------------|-------------------------------|
| `effective_property/solver.py`         | Entry point                   |
| `effective_property/print_table.py`    | User input and results table  |
| `effective_property/regulation.py`     | Input validation helpers      |
| `effective_property/effective_properties.py` | Effective-property models |
| `effective_property/data.py`           | Material-property database    |
| `docs/reference.md`                    | Sources for models and data   |
| `LICENCE`                              | MIT licence                   |

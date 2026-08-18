"""Effective-property models for water-based mono and hybrid nanofluids.

Density and specific heat use volume-fraction mixture rules; thermal
conductivity uses the Maxwell model; dynamic viscosity uses the Brinkman
model. All inputs and outputs are in SI units.

Model references (full citations and links in reference.md):
- Maxwell, J.C. (1873), "A Treatise on Electricity and Magnetism",
  Clarendon Press, Oxford -- thermal-conductivity model.
- Brinkman, H.C. (1952), "The viscosity of concentrated suspensions and
  solutions", J. Chem. Phys. 20, 571 -- viscosity model.
- Mixture rules: Pak & Cho (1998), Exp. Heat Transfer 11, 151-170;
  Xuan & Roetzel (2000), Int. J. Heat Mass Transfer 43, 3701-3707.
"""


# Mono-nanoparticle nanofluid (single particle dispersed in water)
def eff_prop_mono(rho_w, Cp_w, k_w, mu_w,
                  rho_n, Cp_n, k_n, phi):
    """Effective properties of a single-particle (mono) nanofluid.

    Args:
        rho_w, Cp_w, k_w, mu_w: base-water density [kg/m^3], specific heat
            [J/(kg.K)], thermal conductivity [W/(m.K)], viscosity [Pa.s].
        rho_n, Cp_n, k_n: nanoparticle density [kg/m^3], specific heat
            [J/(kg.K)], thermal conductivity [W/(m.K)].
        phi: nanoparticle volume fraction (0 <= phi < 1).

    Returns:
        (rho_nf, Cp_nf, k_nf, mu_nf): effective nanofluid properties (SI).
    """
    rho_nf = (1 - phi) * rho_w + phi * rho_n                       # mixture rule (Pak & Cho 1998)

    Cp_nf = (((1 - phi) * rho_w * Cp_w + phi * rho_n * Cp_n)
                                                      / rho_nf)    # energy-weighted (Xuan & Roetzel 2000)

    k_nf = k_w * (                                                 # Maxwell (1873) model, spherical particles
        (k_n + 2*k_w - 2*phi*(k_w - k_n)) /
        (k_n + 2*k_w + phi*(k_w - k_n))
    )

    mu_nf = mu_w / (1 - phi) ** 2.5                                # Brinkman (1952) model

    return rho_nf, Cp_nf, k_nf, mu_nf


# Hybrid (di-nanoparticle) nanofluid (two particles in water)
def eff_prop_di(rho_w, Cp_w, k_w, mu_w,
                rho_n1, Cp_n1, k_n1, phi1,
                rho_n2, Cp_n2, k_n2, phi2):
    """Effective properties of a hybrid (two-particle) nanofluid.

    Args:
        rho_w, Cp_w, k_w, mu_w: base-water density [kg/m^3], specific heat
            [J/(kg.K)], thermal conductivity [W/(m.K)], viscosity [Pa.s].
        rho_n1, Cp_n1, k_n1, phi1: particle-1 properties + volume fraction.
        rho_n2, Cp_n2, k_n2, phi2: particle-2 properties + volume fraction.

    Returns:
    --------
        (rho_hf, Cp_hf, k_hnf, mu_hf): effective hybrid-nanofluid properties (SI).
    """
    phi_t = phi1 + phi2                                                                      # total volume fraction

    rho_hf = (1 - phi_t) * rho_w + phi1 * rho_n1 + phi2 * rho_n2                             # mixture rule (Pak & Cho 1998)
    rhoCp_hf = (1 - phi_t) * rho_w * Cp_w + phi1 * rho_n1 * Cp_n1 + phi2 * rho_n2 * Cp_n2
    Cp_hf = rhoCp_hf / rho_hf                                                               # energy-weighted (Xuan & Roetzel 2000)

    mu_hf = mu_w / (((1 - phi1) ** 2.5) * ((1 - phi2) ** 2.5))                                 # Brinkman (1952), applied per particle

    # Two-step Maxwell (1873): suspend particle 1 in water, then particle 2 in that mix
    knf = k_w * (
        (k_n1 + 2 * k_w - 2 * phi1*(k_w - k_n1))
        /
        (k_n1 + 2 * k_w + phi1 * (k_w - k_n1))
    )
    k_hnf = knf * (
        (k_n2 + 2 * knf - 2 * phi2*(knf - k_n2))
        /
        (k_n2 + 2 * knf + phi2 * (knf - k_n2))
    )

    return rho_hf, Cp_hf, k_hnf, mu_hf

from data import water_properties, nanoparticles
from effective_properties import eff_prop_mono, eff_prop_di
from regulation import prompt_particle, get_mode


def print_table(mode, particle_args):
    print("=" * 55)
    print("        Effective Nanofluid Properties")
    print("-" * 55)
    print(f"{'Temp(C)':<9}| {'Density':<10}| {'Cp(J/kgK)':<10}| {'k':<8}| {'Viscosity':<12}")
    print("-" * 55)
 
    for temp in sorted(water_properties):
        water = water_properties[temp]
        rho_w, mu_w, k_w = water["density"], water["viscosity"], water["conductivity"]
        Cp_w = water["cp"]  
 
        if mode == "d":
            (rho_n1, Cp_n1, k_n1, phi1,
             rho_n2, Cp_n2, k_n2, phi2) = particle_args
            rho_hf, Cp_hf, k_hf, mu_hf = eff_prop_di(
                rho_w, Cp_w, k_w, mu_w,
                rho_n1, Cp_n1, k_n1, phi1,
                rho_n2, Cp_n2, k_n2, phi2,
            )
        else:
            rho_n, Cp_n, k_n, phi = particle_args
            rho_hf, Cp_hf, k_hf, mu_hf = eff_prop_mono(
                rho_w, Cp_w, k_w, mu_w, rho_n, Cp_n, k_n, phi
            )
 
        print(f"{temp:<9}| {rho_hf:<10.2f}| {Cp_hf:<10.2f}| {k_hf:<8.4f}| {mu_hf:<12.6e}")
 
    print("-" * 55)

def main():
    mode = get_mode()

    if mode == 'd':
        print("Enter nanoparticles name and vol%, one per line (2 lines): ")
        nkey1, phi1 = prompt_particle(" Particle 1 (name vol%):")
        nkey2, phi2 = prompt_particle(" Particle 2 (name vol%):")

        if phi1 + phi2 >= 1:
            raise SystemExit("Error: phi1 + phi2 must be < 1 (100%)")

        n1, n2 = nanoparticles[nkey1], nanoparticles[nkey2]
        particle_args = (
            n1['density'], n1['Cp'], n1["k"], phi1,
            n2['density'], n2['Cp'], n2["k"], phi2,
        )
    else:
        nkey, phi = prompt_particle("Nano-particle name and vol% (name vol%): ")
        n = nanoparticles[nkey]
        particle_args =(n['density'], n['Cp'], n['k'], phi)

    print_table(mode, particle_args)
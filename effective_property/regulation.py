from data import nanoparticles


def prompt_particle (prompt_text):
    while True:
        raw = input(prompt_text).strip().lower().split()
        if len(raw) != 2:
            print(" Please enter exactly two values: <particle_name> <vol%>")
            continue
        name, pct_str = raw

        if name not in nanoparticles:
            print(f" Unlisted particle '{name}'. Options {', '.join(nanoparticles)}")
            continue

        try:
            pct = float(pct_str)
        except ValueError:
            print(" Percentage must be numeric, e.g., 'al2o3 1.5'")
            continue
        if not (0 <= pct <100):
            print(" Percentage must in [0, 100]")
            continue
        return  name, pct / 100


def get_mode():
    while True:
        choice = input("Is it Mono or Di NanoFluid? (M/D): ").strip().lower()
        if choice in ('m', 'd'):
            return choice
        print(" Please enter 'M' or 'D'.")
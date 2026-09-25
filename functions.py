import math
pi = 3.142
g = 9.81
h_planck = 6.626e-34      # J·s
c_light = 3.0e8           # m/s
k_boltz = 1.38e-23        # J/K
e_charge = 1.6e-19        # C
epsilon0 = 8.85e-12       # F/m
mu0 = 4 * math.pi * 1e-7  # T·m/A
R_gas = 8.314             # J/(mol·K)
N_A = 6.022e23            # /mol
sigma_sb = 5.67e-8        # W/(m²K⁴)
I0_sound = 1e-12  

def pendulum(length, unit_l):
    print(f"The length of the rope is: {length}{unit_l}")
    p = input("Do you want to find the period of the pendulum? (yes/no): ")
    if p.lower() in ["y", "yes"]:
        sqrt = math.sqrt(length / 9.81)
        period = 2 * pi * sqrt
        print(f"The period of the pendulum is: {period:.2f} seconds")
    f = input("Do you want to find the frequency of the pendulum? (yes/no): ")
    if f.lower() in ["y", "yes"]:
        sqrt = math.sqrt(length / 9.81)
        period = 2 * pi * sqrt
        frequency = 1 / period
        print(f"The frequency of the pendulum is: {frequency:.2f} Hz")


def projectile(v, θ, t):
    θ = math.radians(θ)

    eqn = input("Are you working with position equations, velocity equations, maximum height, time of flight, range, maximum range or equation of tranjectory(p, v, mh, t, r, mr, e: )").lower()
    if eqn == "p":
        position_eqn = input("Do you want to do horizontal or vertical postion (h or v): ")

        if position_eqn == "h":
            x = v * math.cos(θ) * t
            print(f"{x:.2f}")

        elif position_eqn == "v":
            y = v * math.sin(θ) * t - 0.5 * g * t**2
            print(f"{y:.2f}")
    elif eqn == "v":
        velocity_eqn = input("Do you want to find the horizontal or vertical velocity (h or v): ")
        if velocity_eqn == "h":
            x = v * math.cos(θ)
            print(f"The horizontal velocity is {x:.2f}")

        elif velocity_eqn == "v":
            y = v * math.sin(θ) - g*t
            print(f"The vertical velocity is {y:.2f}")
    elif eqn == "mh":
        h = (v ** 2 * math.sin(θ) ** 2) / (2 * g)
        print(f"The maximum height is {h:.2f}")
    elif eqn == "t":
        t = (2 * v * math.sin(θ)) / g
        print(f"The time of flight is {t:.2f}")
    elif eqn == "r":
        r = (v ** 2 * math.sin(2 * θ)) / g 
        if θ == 45:
            print(f"Maximum range is {r:.2f}")
        else:
            print(f"range is {r:.2f}")
    elif eqn == "mr":
        mr = (v ** 2) / g
        print(f"The maximum range is {mr:.2f}")
    elif eqn == "e":
        x = v * math.cos(θ) * t
        y = math.tan(θ) * x - (g * x ** 2) / (2 * v ** 2 * math.cos(θ) ** 2)
        print(f"The equation of trajectory is {y:.2f}")

def circuit():
    eqn = input("Are you working with Ohm's law, series resistance, parallel resistance, power, EMF/internal resistance or charge (ohms, series, parallel, power, emf, q): ").lower()

    if eqn == "ohms":
        find = input("Do you want to find voltage, current or resistance (v, i, r): ").lower()
        if find == "v":
            i = float(input("What is the current (A)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            v = i * r
            print(f"The voltage is {v:.2f} V")
        elif find == "i":
            v = float(input("What is the voltage (V)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            i = v / r
            print(f"The current is {i:.2f} A")
        elif find == "r":
            v = float(input("What is the voltage (V)?: "))
            i = float(input("What is the current (A)?: "))
            r = v / i
            print(f"The resistance is {r:.2f} Ω")

    elif eqn == "series":
        n = int(input("How many resistors are in series?: "))
        total = 0
        for x in range(n):
            r = float(input(f"Enter resistance {x + 1} (Ω): "))
            total += r
        print(f"The total series resistance is {total:.2f} Ω")

    elif eqn == "parallel":
        n = int(input("How many resistors are in parallel?: "))
        reciprocal_total = 0
        for x in range(n):
            r = float(input(f"Enter resistance {x + 1} (Ω): "))
            reciprocal_total += 1 / r
        total = 1 / reciprocal_total
        print(f"The total parallel resistance is {total:.2f} Ω")

    elif eqn == "power":
        known = input("Which values do you know (vi, ir, vr): ").lower()
        if known == "vi":
            v = float(input("What is the voltage (V)?: "))
            i = float(input("What is the current (A)?: "))
            p = v * i
            print(f"The power is {p:.2f} W")
        elif known == "ir":
            i = float(input("What is the current (A)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            p = i ** 2 * r
            print(f"The power is {p:.2f} W")
        elif known == "vr":
            v = float(input("What is the voltage (V)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            p = v ** 2 / r
            print(f"The power is {p:.2f} W")

    elif eqn == "emf":
        emf = float(input("What is the EMF (V)?: "))
        i = float(input("What is the current (A)?: "))
        r = float(input("What is the internal resistance (Ω)?: "))
        v = emf - i * r
        print(f"The terminal voltage is {v:.2f} V")

    elif eqn == "q":
        i = float(input("What is the current (A)?: "))
        t = float(input("What is the time (s)?: "))
        q = i * t
        print(f"The charge is {q:.2f} C")
    

def electromagnetic_induction():
    eqn = input("Are you working with EMF(emf), magnetic flux(flux), motional EMF(motional), self-inductance(self), inductor energy(energy), mutual inductance(mutual) or transformer(transformer): ").lower()
 
    if eqn == "emf":
        n = float(input("What is the number of turns (N)?: "))
        dphi = float(input("What is the change in flux (Wb)?: "))
        dt = float(input("What is the change in time (s)?: "))
        emf = -n * (dphi / dt)
        print(f"The induced EMF is {emf:.4f} V")
 
    elif eqn == "flux":
        b = float(input("What is the magnetic field strength (T)?: "))
        a = float(input("What is the area (m^2)?: "))
        theta = float(input("What is the angle between B and the normal (degrees)?: "))
        theta = math.radians(theta)
        phi = b * a * math.cos(theta)
        print(f"The magnetic flux is {phi:.4f} Wb")
 
    elif eqn == "motional":
        b = float(input("What is the magnetic field strength (T)?: "))
        l = float(input("What is the length of the conductor (m)?: "))
        v = float(input("What is the velocity (m/s)?: "))
        emf = b * l * v
        print(f"The motional EMF is {emf:.4f} V")
 
    elif eqn == "self":
        emf = float(input("What is the EMF (V)?: "))
        di = float(input("What is the change in current (A)?: "))
        dt = float(input("What is the change in time (s)?: "))
        l = -emf / (di / dt)
        print(f"The self-inductance is {l:.6f} H")
 
    elif eqn == "energy":
        l = float(input("What is the inductance (H)?: "))
        i = float(input("What is the current (A)?: "))
        e = 0.5 * l * i ** 2
        print(f"The energy stored is {e:.4f} J")
 
    elif eqn == "mutual":
        m = float(input("What is the mutual inductance (H)?: "))
        di = float(input("What is the change in primary current (A)?: "))
        dt = float(input("What is the change in time (s)?: "))
        emf2 = -m * (di / dt)
        print(f"The induced EMF in the secondary coil is {emf2:.4f} V")
 
    elif eqn == "transformer":
        find = input("Do you want to find secondary voltage(vs), primary voltage(vp), secondary turns(ns) or primary turns(np): ").lower()
        if find == "vs":
            vp = float(input("What is the primary voltage (V)?: "))
            np_ = float(input("What is the number of primary turns?: "))
            ns = float(input("What is the number of secondary turns?: "))
            vs = vp * (ns / np_)
            print(f"The secondary voltage is {vs:.4f} V")
        elif find == "vp":
            vs = float(input("What is the secondary voltage (V)?: "))
            np_ = float(input("What is the number of primary turns?: "))
            ns = float(input("What is the number of secondary turns?: "))
            vp = vs * (np_ / ns)
            print(f"The primary voltage is {vp:.4f} V")
        elif find == "ns":
            vp = float(input("What is the primary voltage (V)?: "))
            vs = float(input("What is the secondary voltage (V)?: "))
            np_ = float(input("What is the number of primary turns?: "))
            ns = np_ * (vs / vp)
            print(f"The number of secondary turns is {ns:.2f}")
        elif find == "np":
            vp = float(input("What is the primary voltage (V)?: "))
            vs = float(input("What is the secondary voltage (V)?: "))
            ns = float(input("What is the number of secondary turns?: "))
            np_ = ns * (vp / vs)
            print(f"The number of primary turns is {np_:.2f}")
 
 
def wave_motion_sound():
    eqn = input("Are you working with wave speed(speed), period(period), speed of sound in air(sound), Doppler effect(doppler), intensity(intensity), sound level(level), beats(beats), standing wave on a string(string), closed pipe(closed) or open pipe(open): ").lower()
 
    if eqn == "speed":
        f = float(input("What is the frequency (Hz)?: "))
        wavelength = float(input("What is the wavelength (m)?: "))
        v = f * wavelength
        print(f"The wave speed is {v:.4f} m/s")
 
    elif eqn == "period":
        f = float(input("What is the frequency (Hz)?: "))
        t = 1 / f
        print(f"The period is {t:.4f} s")
 
    elif eqn == "sound":
        temp = float(input("What is the air temperature (°C)?: "))
        v = 331 + 0.6 * temp
        print(f"The speed of sound in air is {v:.2f} m/s")
 
    elif eqn == "doppler":
        f = float(input("What is the source frequency (Hz)?: "))
        v_sound = float(input("What is the speed of sound (m/s)?: "))
        v0 = float(input("What is the observer's velocity (m/s, positive if moving toward source)?: "))
        vs = float(input("What is the source's velocity (m/s, positive if moving toward observer)?: "))
        f_obs = f * (v_sound + v0) / (v_sound - vs)
        print(f"The observed frequency is {f_obs:.4f} Hz")
 
    elif eqn == "intensity":
        p = float(input("What is the power (W)?: "))
        a = float(input("What is the area (m^2)?: "))
        i = p / a
        print(f"The intensity is {i:.6f} W/m^2")
 
    elif eqn == "level":
        i = float(input("What is the intensity (W/m^2)?: "))
        beta = 10 * math.log10(i / I0_sound)
        print(f"The sound intensity level is {beta:.2f} dB")
 
    elif eqn == "beats":
        f1 = float(input("What is the first frequency (Hz)?: "))
        f2 = float(input("What is the second frequency (Hz)?: "))
        f_beat = abs(f1 - f2)
        print(f"The beat frequency is {f_beat:.4f} Hz")
 
    elif eqn == "string":
        n = int(input("What harmonic number (n)?: "))
        v = float(input("What is the wave speed (m/s)?: "))
        l = float(input("What is the length of the string (m)?: "))
        f = (n * v) / (2 * l)
        print(f"The frequency of harmonic {n} is {f:.4f} Hz")
 
    elif eqn == "closed":
        n = int(input("What harmonic number (must be odd)?: "))
        v = float(input("What is the wave speed (m/s)?: "))
        l = float(input("What is the length of the pipe (m)?: "))
        f = (n * v) / (4 * l)
        print(f"The frequency of harmonic {n} is {f:.4f} Hz")
 
    elif eqn == "open":
        n = int(input("What harmonic number (n)?: "))
        v = float(input("What is the wave speed (m/s)?: "))
        l = float(input("What is the length of the pipe (m)?: "))
        f = (n * v) / (2 * l)
        print(f"The frequency of harmonic {n} is {f:.4f} Hz")
 
 
def thermal_properties():
    eqn = input("Are you working with heat energy(heat), latent heat(latent), linear expansion(linear), area expansion(area), volume expansion(volume), thermal conduction(conduction) or ideal gas law(gas): ").lower()
 
    if eqn == "heat":
        m = float(input("What is the mass (kg)?: "))
        cshc = float(input("What is the specific heat capacity (J/kg·K)?: "))
        dt = float(input("What is the change in temperature (K)?: "))
        q = m * cshc * dt
        print(f"The heat energy is {q:.4f} J")
 
    elif eqn == "latent":
        m = float(input("What is the mass (kg)?: "))
        l = float(input("What is the specific latent heat (J/kg)?: "))
        q = m * l
        print(f"The heat energy is {q:.4f} J")
 
    elif eqn == "linear":
        l0 = float(input("What is the original length (m)?: "))
        alpha = float(input("What is the linear expansion coefficient (per K)?: "))
        dt = float(input("What is the change in temperature (K)?: "))
        dl = l0 * alpha * dt
        print(f"The change in length is {dl:.6f} m")
 
    elif eqn == "area":
        a0 = float(input("What is the original area (m^2)?: "))
        beta = float(input("What is the area expansion coefficient (per K)?: "))
        dt = float(input("What is the change in temperature (K)?: "))
        da = a0 * beta * dt
        print(f"The change in area is {da:.6f} m^2")
 
    elif eqn == "volume":
        v0 = float(input("What is the original volume (m^3)?: "))
        gamma = float(input("What is the volume expansion coefficient (per K)?: "))
        dt = float(input("What is the change in temperature (K)?: "))
        dv = v0 * gamma * dt
        print(f"The change in volume is {dv:.6f} m^3")
 
    elif eqn == "conduction":
        k_therm = float(input("What is the thermal conductivity (W/m·K)?: "))
        a = float(input("What is the cross-sectional area (m^2)?: "))
        dt = float(input("What is the temperature difference (K)?: "))
        d = float(input("What is the thickness (m)?: "))
        rate = (k_therm * a * dt) / d
        print(f"The rate of heat transfer is {rate:.4f} W")
 
    elif eqn == "gas":
        find = input("Do you want to find pressure(p), volume(v), moles(n) or temperature(t): ").lower()
        if find == "p":
            n = float(input("What is the number of moles?: "))
            t = float(input("What is the temperature (K)?: "))
            v = float(input("What is the volume (m^3)?: "))
            p = (n * R_gas * t) / v
            print(f"The pressure is {p:.4f} Pa")
        elif find == "v":
            n = float(input("What is the number of moles?: "))
            t = float(input("What is the temperature (K)?: "))
            p = float(input("What is the pressure (Pa)?: "))
            v = (n * R_gas * t) / p
            print(f"The volume is {v:.6f} m^3")
        elif find == "n":
            p = float(input("What is the pressure (Pa)?: "))
            v = float(input("What is the volume (m^3)?: "))
            t = float(input("What is the temperature (K)?: "))
            n = (p * v) / (R_gas * t)
            print(f"The number of moles is {n:.4f}")
        elif find == "t":
            p = float(input("What is the pressure (Pa)?: "))
            v = float(input("What is the volume (m^3)?: "))
            n = float(input("What is the number of moles?: "))
            t = (p * v) / (n * R_gas)
            print(f"The temperature is {t:.4f} K")
 
 
def shm():
    eqn = input("Are you working with displacement(x), velocity(v), acceleration(a), period of a spring(spring), period of a pendulum(pendulum), max velocity(vmax), max acceleration(amax) or energy(energy): ").lower()
 
    if eqn == "x":
        amp = float(input("What is the amplitude (m)?: "))
        omega = float(input("What is the angular frequency (rad/s)?: "))
        t = float(input("What is the time (s)?: "))
        phi = float(input("What is the phase constant (radians, 0 if none)?: "))
        x = amp * math.cos(omega * t + phi)
        print(f"The displacement is {x:.4f} m")
 
    elif eqn == "v":
        amp = float(input("What is the amplitude (m)?: "))
        omega = float(input("What is the angular frequency (rad/s)?: "))
        t = float(input("What is the time (s)?: "))
        phi = float(input("What is the phase constant (radians, 0 if none)?: "))
        v = -amp * omega * math.sin(omega * t + phi)
        print(f"The velocity is {v:.4f} m/s")
 
    elif eqn == "a":
        omega = float(input("What is the angular frequency (rad/s)?: "))
        x = float(input("What is the displacement (m)?: "))
        acc = -omega ** 2 * x
        print(f"The acceleration is {acc:.4f} m/s^2")
 
    elif eqn == "spring":
        m = float(input("What is the mass (kg)?: "))
        k = float(input("What is the spring constant (N/m)?: "))
        t = 2 * math.pi * math.sqrt(m / k)
        print(f"The period is {t:.4f} s")
 
    elif eqn == "pendulum":
        l = float(input("What is the length (m)?: "))
        t = 2 * math.pi * math.sqrt(l / g)
        print(f"The period is {t:.4f} s")
 
    elif eqn == "vmax":
        amp = float(input("What is the amplitude (m)?: "))
        omega = float(input("What is the angular frequency (rad/s)?: "))
        vmax = amp * omega
        print(f"The maximum velocity is {vmax:.4f} m/s")
 
    elif eqn == "amax":
        amp = float(input("What is the amplitude (m)?: "))
        omega = float(input("What is the angular frequency (rad/s)?: "))
        amax = amp * omega ** 2
        print(f"The maximum acceleration is {amax:.4f} m/s^2")
 
    elif eqn == "energy":
        find = input("Do you want total energy(total), kinetic energy(ke) or potential energy(pe): ").lower()
        if find == "total":
            k = float(input("What is the spring constant (N/m)?: "))
            amp = float(input("What is the amplitude (m)?: "))
            e = 0.5 * k * amp ** 2
            print(f"The total energy is {e:.4f} J")
        elif find == "ke":
            m = float(input("What is the mass (kg)?: "))
            v = float(input("What is the velocity (m/s)?: "))
            ke = 0.5 * m * v ** 2
            print(f"The kinetic energy is {ke:.4f} J")
        elif find == "pe":
            k = float(input("What is the spring constant (N/m)?: "))
            x = float(input("What is the displacement (m)?: "))
            pe = 0.5 * k * x ** 2
            print(f"The potential energy is {pe:.4f} J")
 
 
def fluid_dynamics():
    eqn = input("Are you working with density(density), pressure from force(pressure), pressure in a fluid(depth), Pascal's principle(pascal), Archimedes' principle(archimedes), continuity equation(continuity), Bernoulli's equation(bernoulli) or Poiseuille's law(poiseuille): ").lower()
 
    if eqn == "density":
        m = float(input("What is the mass (kg)?: "))
        v = float(input("What is the volume (m^3)?: "))
        rho = m / v
        print(f"The density is {rho:.4f} kg/m^3")
 
    elif eqn == "pressure":
        f = float(input("What is the force (N)?: "))
        a = float(input("What is the area (m^2)?: "))
        p = f / a
        print(f"The pressure is {p:.4f} Pa")
 
    elif eqn == "depth":
        p0 = float(input("What is the pressure at the surface (Pa)?: "))
        rho = float(input("What is the fluid density (kg/m^3)?: "))
        depth = float(input("What is the depth (m)?: "))
        p = p0 + rho * g * depth
        print(f"The pressure at depth is {p:.4f} Pa")
 
    elif eqn == "pascal":
        f1 = float(input("What is the force on the first piston (N)?: "))
        a1 = float(input("What is the area of the first piston (m^2)?: "))
        a2 = float(input("What is the area of the second piston (m^2)?: "))
        f2 = f1 * (a2 / a1)
        print(f"The force on the second piston is {f2:.4f} N")
 
    elif eqn == "archimedes":
        rho_fluid = float(input("What is the density of the fluid (kg/m^3)?: "))
        v_disp = float(input("What is the displaced volume (m^3)?: "))
        fb = rho_fluid * v_disp * g
        print(f"The buoyant force is {fb:.4f} N")
 
    elif eqn == "continuity":
        a1 = float(input("What is the first cross-sectional area (m^2)?: "))
        v1 = float(input("What is the first velocity (m/s)?: "))
        a2 = float(input("What is the second cross-sectional area (m^2)?: "))
        v2 = (a1 * v1) / a2
        print(f"The second velocity is {v2:.4f} m/s")
 
    elif eqn == "bernoulli":
        p1 = float(input("What is the pressure at point 1 (Pa)?: "))
        rho = float(input("What is the fluid density (kg/m^3)?: "))
        v1 = float(input("What is the velocity at point 1 (m/s)?: "))
        h1 = float(input("What is the height at point 1 (m)?: "))
        v2 = float(input("What is the velocity at point 2 (m/s)?: "))
        h2 = float(input("What is the height at point 2 (m)?: "))
        p2 = p1 + 0.5 * rho * (v1 ** 2 - v2 ** 2) + rho * g * (h1 - h2)
        print(f"The pressure at point 2 is {p2:.4f} Pa")
 
    elif eqn == "poiseuille":
        r = float(input("What is the radius of the pipe (m)?: "))
        dp = float(input("What is the pressure difference (Pa)?: "))
        eta = float(input("What is the viscosity (Pa·s)?: "))
        l = float(input("What is the length of the pipe (m)?: "))
        q = (math.pi * r ** 4 * dp) / (8 * eta * l)
        print(f"The volumetric flow rate is {q:.8f} m^3/s")
 
 
def optics():
    eqn = input("Are you working with the mirror/lens equation(lens), magnification(mag), lens maker's equation(maker), Snell's law(snell), critical angle(critical) or power of a lens(power): ").lower()
 
    if eqn == "lens":
        find = input("Do you want to find focal length(f), object distance(do) or image distance(di): ").lower()
        if find == "f":
            do = float(input("What is the object distance (m)?: "))
            di = float(input("What is the image distance (m)?: "))
            f = 1 / (1 / do + 1 / di)
            print(f"The focal length is {f:.4f} m")
        elif find == "do":
            f = float(input("What is the focal length (m)?: "))
            di = float(input("What is the image distance (m)?: "))
            do = 1 / (1 / f - 1 / di)
            print(f"The object distance is {do:.4f} m")
        elif find == "di":
            f = float(input("What is the focal length (m)?: "))
            do = float(input("What is the object distance (m)?: "))
            di = 1 / (1 / f - 1 / do)
            print(f"The image distance is {di:.4f} m")
 
    elif eqn == "mag":
        do = float(input("What is the object distance (m)?: "))
        di = float(input("What is the image distance (m)?: "))
        m = -di / do
        print(f"The magnification is {m:.4f}")
 
    elif eqn == "maker":
        n = float(input("What is the refractive index of the lens material?: "))
        r1 = float(input("What is the radius of curvature of the first surface (m)?: "))
        r2 = float(input("What is the radius of curvature of the second surface (m)?: "))
        f = 1 / ((n - 1) * (1 / r1 - 1 / r2))
        print(f"The focal length is {f:.4f} m")
 
    elif eqn == "snell":
        find = input("Do you want to find n1, n2, angle1 or angle2: ").lower()
        if find == "angle2":
            n1 = float(input("What is n1?: "))
            n2 = float(input("What is n2?: "))
            theta1 = float(input("What is angle 1 (degrees)?: "))
            theta1 = math.radians(theta1)
            theta2 = math.asin((n1 * math.sin(theta1)) / n2)
            print(f"Angle 2 is {math.degrees(theta2):.2f} degrees")
        elif find == "angle1":
            n1 = float(input("What is n1?: "))
            n2 = float(input("What is n2?: "))
            theta2 = float(input("What is angle 2 (degrees)?: "))
            theta2 = math.radians(theta2)
            theta1 = math.asin((n2 * math.sin(theta2)) / n1)
            print(f"Angle 1 is {math.degrees(theta1):.2f} degrees")
        elif find == "n1":
            n2 = float(input("What is n2?: "))
            theta1 = math.radians(float(input("What is angle 1 (degrees)?: ")))
            theta2 = math.radians(float(input("What is angle 2 (degrees)?: ")))
            n1 = (n2 * math.sin(theta2)) / math.sin(theta1)
            print(f"n1 is {n1:.4f}")
        elif find == "n2":
            n1 = float(input("What is n1?: "))
            theta1 = math.radians(float(input("What is angle 1 (degrees)?: ")))
            theta2 = math.radians(float(input("What is angle 2 (degrees)?: ")))
            n2 = (n1 * math.sin(theta1)) / math.sin(theta2)
            print(f"n2 is {n2:.4f}")
 
    elif eqn == "critical":
        n1 = float(input("What is the refractive index of the denser medium (n1)?: "))
        n2 = float(input("What is the refractive index of the less dense medium (n2)?: "))
        theta_c = math.asin(n2 / n1)
        print(f"The critical angle is {math.degrees(theta_c):.2f} degrees")
 
    elif eqn == "power":
        f = float(input("What is the focal length (m)?: "))
        p = 1 / f
        print(f"The power of the lens is {p:.4f} D")
 
 
def electric_currents_magnetic_fields():
    eqn = input("Are you working with force on a moving charge(chargeforce), force on a current-carrying wire(wireforce), field of a long straight wire(wirefield), field of a solenoid(solenoid), field at the center of a loop(loop) or torque on a current loop(torque): ").lower()
 
    if eqn == "chargeforce":
        q = float(input("What is the charge (C)?: "))
        v = float(input("What is the velocity (m/s)?: "))
        b = float(input("What is the magnetic field strength (T)?: "))
        theta = float(input("What is the angle between v and B (degrees)?: "))
        theta = math.radians(theta)
        f = q * v * b * math.sin(theta)
        print(f"The force on the charge is {f:.6e} N")
 
    elif eqn == "wireforce":
        b = float(input("What is the magnetic field strength (T)?: "))
        i = float(input("What is the current (A)?: "))
        l = float(input("What is the length of the wire (m)?: "))
        theta = float(input("What is the angle between the wire and B (degrees)?: "))
        theta = math.radians(theta)
        f = b * i * l * math.sin(theta)
        print(f"The force on the wire is {f:.4f} N")
 
    elif eqn == "wirefield":
        i = float(input("What is the current (A)?: "))
        r = float(input("What is the distance from the wire (m)?: "))
        b = (mu0 * i) / (2 * math.pi * r)
        print(f"The magnetic field strength is {b:.6e} T")
 
    elif eqn == "solenoid":
        n = float(input("What is the number of turns per unit length (turns/m)?: "))
        i = float(input("What is the current (A)?: "))
        b = mu0 * n * i
        print(f"The magnetic field strength is {b:.6e} T")
 
    elif eqn == "loop":
        i = float(input("What is the current (A)?: "))
        r = float(input("What is the radius of the loop (m)?: "))
        b = (mu0 * i) / (2 * r)
        print(f"The magnetic field strength at the center is {b:.6e} T")
 
    elif eqn == "torque":
        n = float(input("What is the number of turns?: "))
        i = float(input("What is the current (A)?: "))
        a = float(input("What is the area of the loop (m^2)?: "))
        b = float(input("What is the magnetic field strength (T)?: "))
        theta = float(input("What is the angle between the loop's normal and B (degrees)?: "))
        theta = math.radians(theta)
        tau = n * i * a * b * math.sin(theta)
        print(f"The torque is {tau:.6f} N·m")
 
 
def nuclear_physics():
    eqn = input("Are you working with radioactive decay(decay), half-life(halflife), activity(activity), mass-energy equivalence(massenergy) or binding energy(binding): ").lower()
 
    if eqn == "decay":
        n0 = float(input("What is the initial number of nuclei?: "))
        lam = float(input("What is the decay constant (per s)?: "))
        t = float(input("What is the time (s)?: "))
        n = n0 * math.exp(-lam * t)
        print(f"The remaining number of nuclei is {n:.4e}")
 
    elif eqn == "halflife":
        find = input("Do you want to find half-life(t) or decay constant(lambda): ").lower()
        if find == "t":
            lam = float(input("What is the decay constant (per s)?: "))
            t_half = math.log(2) / lam
            print(f"The half-life is {t_half:.4e} s")
        elif find == "lambda":
            t_half = float(input("What is the half-life (s)?: "))
            lam = math.log(2) / t_half
            print(f"The decay constant is {lam:.4e} per s")
 
    elif eqn == "activity":
        lam = float(input("What is the decay constant (per s)?: "))
        n = float(input("What is the number of nuclei present?: "))
        a = lam * n
        print(f"The activity is {a:.4e} decays/s")
 
    elif eqn == "massenergy":
        m = float(input("What is the mass (kg)?: "))
        e = m * c_light ** 2
        print(f"The energy equivalent is {e:.4e} J")
 
    elif eqn == "binding":
        dm = float(input("What is the mass defect (kg)?: "))
        de = dm * c_light ** 2
        print(f"The binding energy is {de:.4e} J")
 
 
def quantum_mechanics():
    eqn = input("Are you working with photon energy(photon), the photoelectric effect(photoelectric) or de Broglie wavelength(debroglie): ").lower()
 
    if eqn == "photon":
        find = input("Do you want to find energy(e), frequency(f) or wavelength(w): ").lower()
        if find == "e":
            f = float(input("What is the frequency (Hz)?: "))
            e = h_planck * f
            print(f"The photon energy is {e:.4e} J")
        elif find == "f":
            e = float(input("What is the energy (J)?: "))
            f = e / h_planck
            print(f"The frequency is {f:.4e} Hz")
        elif find == "w":
            e = float(input("What is the energy (J)?: "))
            wavelength = (h_planck * c_light) / e
            print(f"The wavelength is {wavelength:.4e} m")
 
    elif eqn == "photoelectric":
        f = float(input("What is the frequency of the incident light (Hz)?: "))
        phi = float(input("What is the work function (J)?: "))
        ke_max = h_planck * f - phi
        print(f"The maximum kinetic energy of the emitted electron is {ke_max:.4e} J")
 
    elif eqn == "debroglie":
        m = float(input("What is the mass (kg)?: "))
        v = float(input("What is the velocity (m/s)?: "))
        wavelength = h_planck / (m * v)
        print(f"The de Broglie wavelength is {wavelength:.4e} m")
 
 
def thermodynamics():
    eqn = input("Are you working with the first law of thermodynamics(first), work done by a gas(work), efficiency(efficiency), Carnot efficiency(carnot) or entropy(entropy): ").lower()
 
    if eqn == "first":
        find = input("Do you want to find change in internal energy(u), heat(q) or work(w): ").lower()
        if find == "u":
            q = float(input("What is the heat added to the system (J)?: "))
            w = float(input("What is the work done by the system (J)?: "))
            du = q - w
            print(f"The change in internal energy is {du:.4f} J")
        elif find == "q":
            du = float(input("What is the change in internal energy (J)?: "))
            w = float(input("What is the work done by the system (J)?: "))
            q = du + w
            print(f"The heat added is {q:.4f} J")
        elif find == "w":
            q = float(input("What is the heat added to the system (J)?: "))
            du = float(input("What is the change in internal energy (J)?: "))
            w = q - du
            print(f"The work done by the system is {w:.4f} J")
 
    elif eqn == "work":
        p = float(input("What is the pressure (Pa)?: "))
        dv = float(input("What is the change in volume (m^3)?: "))
        w = p * dv
        print(f"The work done is {w:.4f} J")
 
    elif eqn == "efficiency":
        w_out = float(input("What is the work output (J)?: "))
        q_in = float(input("What is the heat input (J)?: "))
        eff = w_out / q_in
        print(f"The efficiency is {eff * 100:.2f}%")
 
    elif eqn == "carnot":
        t_cold = float(input("What is the cold reservoir temperature (K)?: "))
        t_hot = float(input("What is the hot reservoir temperature (K)?: "))
        eff = 1 - (t_cold / t_hot)
        print(f"The Carnot efficiency is {eff * 100:.2f}%")
 
    elif eqn == "entropy":
        q = float(input("What is the heat transferred (J)?: "))
        t = float(input("What is the temperature (K)?: "))
        ds = q / t
        print(f"The change in entropy is {ds:.6f} J/K")
 
 
def capacitors_circuits():
    eqn = input("Are you working with capacitance(cap), energy stored(energy), series capacitance(series), parallel capacitance(parallel) or RC charging/discharging(rc): ").lower()
 
    if eqn == "cap":
        find = input("Do you want to find capacitance(c), charge(q) or voltage(v): ").lower()
        if find == "c":
            q = float(input("What is the charge (C)?: "))
            v = float(input("What is the voltage (V)?: "))
            capa = q / v
            print(f"The capacitance is {capa:.6e} F")
        elif find == "q":
            capa = float(input("What is the capacitance (F)?: "))
            v = float(input("What is the voltage (V)?: "))
            q = capa * v
            print(f"The charge is {q:.6e} C")
        elif find == "v":
            q = float(input("What is the charge (C)?: "))
            capa = float(input("What is the capacitance (F)?: "))
            v = q / capa
            print(f"The voltage is {v:.4f} V")
 
    elif eqn == "energy":
        capa = float(input("What is the capacitance (F)?: "))
        v = float(input("What is the voltage (V)?: "))
        e = 0.5 * capa * v ** 2
        print(f"The energy stored is {e:.6e} J")
 
    elif eqn == "series":
        n = int(input("How many capacitors are in series?: "))
        reciprocal_total = 0
        for x in range(n):
            c = float(input(f"Enter capacitance {x + 1} (F): "))
            reciprocal_total += 1 / c
        total = 1 / reciprocal_total
        print(f"The total series capacitance is {total:.6e} F")
 
    elif eqn == "parallel":
        n = int(input("How many capacitors are in parallel?: "))
        total = 0
        for x in range(n):
            c = float(input(f"Enter capacitance {x + 1} (F): "))
            total += c
        print(f"The total parallel capacitance is {total:.6e} F")
 
    elif eqn == "rc":
        find = input("Do you want to find charging voltage(charge) or discharging voltage(discharge): ").lower()
        v0 = float(input("What is the initial/source voltage (V)?: "))
        r = float(input("What is the resistance (Ω)?: "))
        capa = float(input("What is the capacitance (F)?: "))
        t = float(input("What is the time (s)?: "))
        tau = r * capa
        if find == "charge":
            v = v0 * (1 - math.exp(-t / tau))
            print(f"The voltage across the capacitor is {v:.4f} V")
        elif find == "discharge":
            v = v0 * math.exp(-t / tau)
            print(f"The voltage across the capacitor is {v:.4f} V")
 
 
def resistors_ohms_law():
    eqn = input("Are you working with Ohm's law(ohms), series resistors(series), parallel resistors(parallel), power(power) or resistivity(resistivity): ").lower()
 
    if eqn == "ohms":
        find = input("Do you want to find voltage(v), current(i) or resistance(r): ").lower()
        if find == "v":
            i = float(input("What is the current (A)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            v = i * r
            print(f"The voltage is {v:.4f} V")
        elif find == "i":
            v = float(input("What is the voltage (V)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            i = v / r
            print(f"The current is {i:.4f} A")
        elif find == "r":
            v = float(input("What is the voltage (V)?: "))
            i = float(input("What is the current (A)?: "))
            r = v / i
            print(f"The resistance is {r:.4f} Ω")
 
    elif eqn == "series":
        n = int(input("How many resistors are in series?: "))
        total = 0
        for x in range(n):
            r = float(input(f"Enter resistance {x + 1} (Ω): "))
            total += r
        print(f"The total series resistance is {total:.4f} Ω")
 
    elif eqn == "parallel":
        n = int(input("How many resistors are in parallel?: "))
        reciprocal_total = 0
        for x in range(n):
            r = float(input(f"Enter resistance {x + 1} (Ω): "))
            reciprocal_total += 1 / r
        total = 1 / reciprocal_total
        print(f"The total parallel resistance is {total:.4f} Ω")
 
    elif eqn == "power":
        known = input("Which values do you know (vi, ir, vr): ").lower()
        if known == "vi":
            v = float(input("What is the voltage (V)?: "))
            i = float(input("What is the current (A)?: "))
            p = v * i
            print(f"The power is {p:.4f} W")
        elif known == "ir":
            i = float(input("What is the current (A)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            p = i ** 2 * r
            print(f"The power is {p:.4f} W")
        elif known == "vr":
            v = float(input("What is the voltage (V)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            p = v ** 2 / r
            print(f"The power is {p:.4f} W")
 
    elif eqn == "resistivity":
        find = input("Do you want to find resistivity(rho), resistance(r), length(l) or area(a): ").lower()
        if find == "rho":
            r = float(input("What is the resistance (Ω)?: "))
            a = float(input("What is the cross-sectional area (m^2)?: "))
            l = float(input("What is the length (m)?: "))
            rho = (r * a) / l
            print(f"The resistivity is {rho:.6e} Ω·m")
        elif find == "r":
            rho = float(input("What is the resistivity (Ω·m)?: "))
            l = float(input("What is the length (m)?: "))
            a = float(input("What is the cross-sectional area (m^2)?: "))
            r = (rho * l) / a
            print(f"The resistance is {r:.4f} Ω")
        elif find == "l":
            r = float(input("What is the resistance (Ω)?: "))
            a = float(input("What is the cross-sectional area (m^2)?: "))
            rho = float(input("What is the resistivity (Ω·m)?: "))
            l = (r * a) / rho
            print(f"The length is {l:.4f} m")
        elif find == "a":
            rho = float(input("What is the resistivity (Ω·m)?: "))
            l = float(input("What is the length (m)?: "))
            r = float(input("What is the resistance (Ω)?: "))
            a = (rho * l) / r
            print(f"The cross-sectional area is {a:.6e} m^2")
 
 
def magnetism_magnetic_forces():
    eqn = input("Are you working with force on a moving charge(chargeforce), force on a current-carrying wire(wireforce), force between two parallel wires(twowires), radius of circular motion(radius) or magnetic dipole moment(dipole): ").lower()
 
    if eqn == "chargeforce":
        q = float(input("What is the charge (C)?: "))
        v = float(input("What is the velocity (m/s)?: "))
        b = float(input("What is the magnetic field strength (T)?: "))
        theta = float(input("What is the angle between v and B (degrees)?: "))
        theta = math.radians(theta)
        f = q * v * b * math.sin(theta)
        print(f"The magnetic force is {f:.6e} N")
 
    elif eqn == "wireforce":
        b = float(input("What is the magnetic field strength (T)?: "))
        i = float(input("What is the current (A)?: "))
        l = float(input("What is the length of the wire (m)?: "))
        theta = float(input("What is the angle between the wire and B (degrees)?: "))
        theta = math.radians(theta)
        f = b * i * l * math.sin(theta)
        print(f"The force on the wire is {f:.4f} N")
 
    elif eqn == "twowires":
        i1 = float(input("What is the current in the first wire (A)?: "))
        i2 = float(input("What is the current in the second wire (A)?: "))
        l = float(input("What is the length of the wires (m)?: "))
        r = float(input("What is the distance between the wires (m)?: "))
        f = (mu0 * i1 * i2 * l) / (2 * math.pi * r)
        print(f"The force between the wires is {f:.6e} N")
 
    elif eqn == "radius":
        m = float(input("What is the mass of the particle (kg)?: "))
        v = float(input("What is the velocity (m/s)?: "))
        q = float(input("What is the charge (C)?: "))
        b = float(input("What is the magnetic field strength (T)?: "))
        r = (m * v) / (q * b)
        print(f"The radius of the circular path is {r:.6e} m")
 
    elif eqn == "dipole":
        n = float(input("What is the number of turns?: "))
        i = float(input("What is the current (A)?: "))
        a = float(input("What is the area of the loop (m^2)?: "))
        m = n * i * a
        print(f"The magnetic dipole moment is {m:.6e} A·m^2")
 
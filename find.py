import math
pi = 3.142
g = 9.81
h_planck = 6.626e-34      # J·s
c_light = 3.0e8           # m/s
e_charge = 1.6e-19        # C
epsilon0 = 8.85e-12       # F/m
mu0 = 4 * math.pi * 1e-7  # T·m/A
R_gas = 8.314             # J/(mol·K)
I0_sound = 1e-12          # W/m^2
def pendulumf():
    c = input("Are you  finding period, length or the frequency(p or l or f)?: ")
    if c == "p":
        length = float(input("What is the length of the rope?: "))
        sqrt = math.sqrt(length / 9.81)
        period = 2 * pi * sqrt
        print(f"The period of the pendulum is: {period:.2f} seconds")
    elif c == "l":
        time = float(input("How long did it take for one oscillation to occur?: "))
        n = time ** 2 * g
        d = 4 * pi ** 2
        length = n / d
        print(f"The length of the rope is {length:.2f} m")
    elif c == "f":
        length = float(input("What is the length of the rope?: "))
        sqrt = math.sqrt(length / 9.81)
        period = 2 * pi * sqrt
        frequency = 1 / period
        print(f"The frequency is {frequency:.2f}")

def projectilef():
    while True:
        eqn = input("Are you working with position equations(p), velocity equations(v), maximum height(mh), time of flight(t), range(r), maximum range(mr) or equation of tranjectory(e)").lower()
        if eqn == "q":
            quit()

        elif eqn == "p":
            p = input("Is it the horizontal(h) or vertical(v) equation you are finding?: ").lower()
            if p == "h":
                c = input("Do you want to find the initial velocity(v), the angle(a) or the time(t)?: ").lower()
                if c == "v":
                    x = float(input("What is the horizontal equation?: "))
                    θ = float(input("What is the angle?: "))
                    t = float(input("What s the time taken?: "))
                    θ = math.radians(θ)
                    d = math.cos(θ) * t
                    v = x / d
                    print(f"The initial velocity is {v:.2f}")
                elif c == "a":
                    x = float(input("What is the horizontal equation?: "))
                    t = float(input("What s the time taken?: "))
                    v = float(input("What is the initial velocity?: "))
                    d = v * t
                    f = x / d
                    θ = math.acos(f)
                    print(f"The angle is {θ:.2f}")
                elif c == "t":
                    x = float(input("What is the horizontal equation?: "))
                    v = float(input("What is the initial velocity?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    d = v * math.cos(θ)
                    t = x / d
                    print(f"The time taken is {t:.2f}")

            elif p == "v":
                c = input("Do you want to find the intial velocity(v), the angle(a) or the time(t)").lower()
                if c == "v":
                    y = float(input("What is the vertical position?: "))
                    t = float(input("What is the time taken?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    n = 2 * y + g * t ** 2
                    d = 2 * math.sin(θ) * t
                    v = n / d
                    print(f"The initial velocity is {v:.2f}")
                elif c == "a":
                    y = float(input("What is the vertical position?: "))
                    v = float(input("What is thhe initial velocity?: "))
                    t = float(input("What is the time taken?: "))
                    n = 2 * y + g * t ** 2
                    d = 2 * v * t
                    i = n / d
                    θ = math.asin(i)
                    print(f"The angle is {math.degrees(θ):.2f}")
                elif c == "t":
                    y = float(input("What is the vertical position?: "))
                    v = float(input("What is thhe initial velocity?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    n1 = v * math.sin(θ) + math.sqrt(v ** 2 * math.sin(θ) ** 2 - 2 * (g * y))
                    n2 = v * math.sin(θ) - math.sqrt(v ** 2 * math.sin(θ) ** 2 - 2 * (g * y))
                    t1 = n1 / g
                    t2 = n2 / g
                    print(f"The two possible times for t are {t1:.2f}s or {t2:.2f}s")

        elif eqn == "v":
            c = input("Do you want to find the Horizontal velocity(h) or the Vertical velocity(v)?: ").lower()
            if c == "h":
                p = input("Do you want to find the initial velocity(v) or the angle(a)?: ").lower()
                if p == "v":
                    vx = float(input("What is the Horizontal velocity?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    vo = vx / math.cos(θ)
                    print(f"The initial velocity is {vo:.2f}")
                elif p == "a":
                    vx = float(input("What is the Horizontal velocity?: "))
                    vo = float(input("What is the initial velocity?: "))
                    a = vx / vo
                    θ = math.acos(a)
                    print(f"The angle is {math.degrees(θ):.2f}")
            elif c == "v":
                p = input("Do you want to find the initial velocity(v), the angle(a) or the time(t)").lower()
                if p == "v":
                    vy = float(input("What is the vertical velocity?: "))
                    t = float(input("What is the time take?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    n = vy + g * t
                    d = math.sin(θ)
                    vo = n / d
                    print(f"The initial velocity is {vo:.2f}")
                elif p == "t":
                    vy = float(input("What is the vertical velocity?: "))
                    vo = float(input("What is the initial velocity?: "))
                    θ = float(input("What is the angle?: "))
                    θ = math.radians(θ)
                    n = vo * math.sin(θ) - vy
                    t = n / g
                    print(f"The time taken is {t:.2f}")
                elif p == "a":
                    vy = float(input("What is the vertical velocity?: "))
                    vo = float(input("What is the initial velocity?: "))
                    t = float(input("What is the time take?: "))
                    n = vy + g * t
                    θ = math.asin(n / vo)
                    print(f"The angle is {math.degrees(θ):.2f}")

        elif eqn == "mh":
            p = input("Do you want to find the initial velocity(v) or the angle(a)?: ").lower()
            if p == "v":
                h = float(input("What is the maximum height?: "))
                θ = float(input("What is the angle?: "))
                θ = math.radians(θ)
                n = 2 * g * h
                d = math.sin(θ) ** 2
                v = math.sqrt(n / d)
                print(f"The initial velocity is {v:.2f}")
            elif p == "a":
                h = float(input("What is the maximum height?: "))
                v = float(input("What is the initial velocity?: "))
                n = 2 * g * h
                d = v ** 2
                f = math.sqrt(n / d)
                θ = math.asin(f)
                print(f"The angle is {math.degrees(θ):.2f}")

        elif eqn == "t":
            p = input("Do you want to find the initial velocity(v) or the angle(a)?: ").lower()
            if p == "v":
                t = float(input("What is the time of flight?: "))
                θ = float(input("What is the angle?: "))
                θ = math.radians(θ)
                v = (g * t) / (2 * math.sin(θ))
                print(f"The initial velocity is {v:.2f}")
            elif p == "a":
                t = float(input("What is the time of flight?: "))
                v = float(input("What is the initial velocity?: "))
                f = (g * t) / (2 * v)
                θ = math.asin(f)
                print(f"The angle is {math.degrees(θ):.2f}")

        elif eqn == "r":
            p = input("Do you want to find the initial velocity(v) or the angle(a)?: ").lower()
            if p == "v":
                r = float(input("What is the range?: "))
                θ = float(input("What is the angle?: "))
                θ = math.radians(θ)
                v = math.sqrt((r * g) / math.sin(2 * θ))
                print(f"The initial velocity is {v:.2f}")
            elif p == "a":
                r = float(input("What is the range?: "))
                v = float(input("What is the initial velocity?: "))
                f = (r * g) / v ** 2
                θ = math.asin(f) / 2
                print(f"The angle is {math.degrees(θ):.2f}")

        elif eqn == "mr":
            mr = float(input("What is the maximum range?: "))
            v = math.sqrt(mr * g)
            print(f"The initial velocity is {v:.2f}")

        elif eqn == "e":
            x = float(input("What is the horizontal position?: "))
            θ = float(input("What is the angle?: "))
            t = float(input("What is the time taken?: "))
            θ = math.radians(θ)
            y = math.tan(θ) * x - (g * x ** 2) / (2 * v ** 2 * math.cos(θ) ** 2)
            print(f"The vertical position is {y:.2f}")
                
def circuitf():
    while True:
        eqn = input("Are you working with Ohm's law(o), power(p), series resistance(s), parallel resistance(pa), EMF/internal resistance(e) or charge(q): ").lower()
        if eqn == "quit":
            quit()

        elif eqn == "o":
            find = input("Do you want to find voltage(v), current(i) or resistance(r)?: ").lower()
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

        elif eqn == "p":
            known = input("Do you know voltage and current(vi), current and resistance(ir) or voltage and resistance(vr)?: ").lower()
            find = input("Do you want to find voltage(v), current(i), resistance(r) or power(p)?: ").lower()
            if known == "vi":
                if find == "p":
                    v = float(input("What is the voltage (V)?: "))
                    i = float(input("What is the current (A)?: "))
                    p = v * i
                    print(f"The power is {p:.2f} W")
                elif find == "v":
                    p = float(input("What is the power (W)?: "))
                    i = float(input("What is the current (A)?: "))
                    v = p / i
                    print(f"The voltage is {v:.2f} V")
                elif find == "i":
                    p = float(input("What is the power (W)?: "))
                    v = float(input("What is the voltage (V)?: "))
                    i = p / v
                    print(f"The current is {i:.2f} A")
            elif known == "ir":
                if find == "p":
                    i = float(input("What is the current (A)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    p = i ** 2 * r
                    print(f"The power is {p:.2f} W")
                elif find == "i":
                    p = float(input("What is the power (W)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    i = math.sqrt(p / r)
                    print(f"The current is {i:.2f} A")
                elif find == "r":
                    p = float(input("What is the power (W)?: "))
                    i = float(input("What is the current (A)?: "))
                    r = p / i ** 2
                    print(f"The resistance is {r:.2f} Ω")
            elif known == "vr":
                if find == "p":
                    v = float(input("What is the voltage (V)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    p = v ** 2 / r
                    print(f"The power is {p:.2f} W")
                elif find == "v":
                    p = float(input("What is the power (W)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    v = math.sqrt(p * r)
                    print(f"The voltage is {v:.2f} V")
                elif find == "r":
                    p = float(input("What is the power (W)?: "))
                    v = float(input("What is the voltage (V)?: "))
                    r = v ** 2 / p
                    print(f"The resistance is {r:.2f} Ω")

        elif eqn == "s":
            n = int(input("How many resistors in total, including the unknown one?: "))
            total = float(input("What is the total series resistance (Ω)?: "))
            known_sum = 0
            for x in range(n - 1):
                r = float(input(f"Enter known resistance {x + 1} (Ω): "))
                known_sum += r
            unknown = total - known_sum
            print(f"The unknown resistance is {unknown:.2f} Ω")

        elif eqn == "pa":
            n = int(input("How many resistors in total, including the unknown one?: "))
            total = float(input("What is the total parallel resistance (Ω)?: "))
            known_reciprocal_sum = 0
            for x in range(n - 1):
                r = float(input(f"Enter known resistance {x + 1} (Ω): "))
                known_reciprocal_sum += 1 / r
            reciprocal_unknown = (1 / total) - known_reciprocal_sum
            unknown = 1 / reciprocal_unknown
            print(f"The unknown resistance is {unknown:.2f} Ω")

        elif eqn == "e":
            find = input("Do you want to find EMF(e), current(i) or internal resistance(r)?: ").lower()
            if find == "e":
                v = float(input("What is the terminal voltage (V)?: "))
                i = float(input("What is the current (A)?: "))
                r = float(input("What is the internal resistance (Ω)?: "))
                emf = v + i * r
                print(f"The EMF is {emf:.2f} V")
            elif find == "i":
                emf = float(input("What is the EMF (V)?: "))
                v = float(input("What is the terminal voltage (V)?: "))
                r = float(input("What is the internal resistance (Ω)?: "))
                i = (emf - v) / r
                print(f"The current is {i:.2f} A")
            elif find == "r":
                emf = float(input("What is the EMF (V)?: "))
                v = float(input("What is the terminal voltage (V)?: "))
                i = float(input("What is the current (A)?: "))
                r = (emf - v) / i
                print(f"The internal resistance is {r:.2f} Ω")

        elif eqn == "q":
            find = input("Do you want to find current(i) or time(t)?: ").lower()
            if find == "i":
                q = float(input("What is the charge (C)?: "))
                t = float(input("What is the time (s)?: "))
                i = q / t
                print(f"The current is {i:.2f} A")
            elif find == "t":
                q = float(input("What is the charge (C)?: "))
                i = float(input("What is the current (A)?: "))
                t = q / i
                print(f"The time is {t:.2f} s")
def electromagnetic_inductionf():
    while True:
        eqn = input("Are you working with Faraday's law(emf), magnetic flux(flux), motional EMF(motional), self-inductance(self), inductor energy(energy), mutual inductance(mutual) or transformer(transformer) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "emf":
            find = input("Do you want to find the EMF(e), number of turns(n), change in flux(f) or change in time(t)?: ").lower()
            if find != "e":
                emf = float(input("What is the EMF (V)?: "))
            if find != "n":
                n = float(input("What is the number of turns?: "))
            if find != "f":
                dphi = float(input("What is the change in flux (Wb)?: "))
            if find != "t":
                dt = float(input("What is the change in time (s)?: "))
            if find == "e":
                emf = -n * dphi / dt
                print(f"The EMF is {emf:.4f} V")
            elif find == "n":
                n = -emf * dt / dphi
                print(f"The number of turns is {n:.2f}")
            elif find == "f":
                dphi = -emf * dt / n
                print(f"The change in flux is {dphi:.4f} Wb")
            elif find == "t":
                dt = -n * dphi / emf
                print(f"The change in time is {dt:.4f} s")
 
        elif eqn == "flux":
            find = input("Do you want to find the flux(p), magnetic field(b), area(a) or angle(t)?: ").lower()
            if find != "p":
                phi = float(input("What is the magnetic flux (Wb)?: "))
            if find != "b":
                b = float(input("What is the magnetic field strength (T)?: "))
            if find != "a":
                a = float(input("What is the area (m^2)?: "))
            if find != "t":
                θ = math.radians(float(input("What is the angle between B and the normal (degrees)?: ")))
            if find == "p":
                phi = b * a * math.cos(θ)
                print(f"The magnetic flux is {phi:.4f} Wb")
            elif find == "b":
                b = phi / (a * math.cos(θ))
                print(f"The magnetic field strength is {b:.4f} T")
            elif find == "a":
                a = phi / (b * math.cos(θ))
                print(f"The area is {a:.4f} m^2")
            elif find == "t":
                θ = math.acos(phi / (b * a))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
        elif eqn == "motional":
            find = input("Do you want to find the EMF(e), magnetic field(b), length(l) or velocity(v)?: ").lower()
            if find != "e":
                emf = float(input("What is the EMF (V)?: "))
            if find != "b":
                b = float(input("What is the magnetic field strength (T)?: "))
            if find != "l":
                l = float(input("What is the length of the conductor (m)?: "))
            if find != "v":
                v = float(input("What is the velocity (m/s)?: "))
            if find == "e":
                emf = b * l * v
                print(f"The EMF is {emf:.4f} V")
            elif find == "b":
                b = emf / (l * v)
                print(f"The magnetic field strength is {b:.4f} T")
            elif find == "l":
                l = emf / (b * v)
                print(f"The length is {l:.4f} m")
            elif find == "v":
                v = emf / (b * l)
                print(f"The velocity is {v:.4f} m/s")
 
        elif eqn in ["self", "mutual"]:
            name = "self-inductance" if eqn == "self" else "mutual inductance"
            find = input(f"Do you want to find the EMF(e), {name}(l), change in current(i) or change in time(t)?: ").lower()
            if find != "e":
                emf = float(input("What is the induced EMF (V)?: "))
            if find != "l":
                l = float(input(f"What is the {name} (H)?: "))
            if find != "i":
                di = float(input("What is the change in current (A)?: "))
            if find != "t":
                dt = float(input("What is the change in time (s)?: "))
            if find == "e":
                emf = -l * di / dt
                print(f"The EMF is {emf:.4f} V")
            elif find == "l":
                l = -emf * dt / di
                print(f"The {name} is {l:.6f} H")
            elif find == "i":
                di = -emf * dt / l
                print(f"The change in current is {di:.4f} A")
            elif find == "t":
                dt = -l * di / emf
                print(f"The change in time is {dt:.4f} s")
 
        elif eqn == "energy":
            find = input("Do you want to find the energy(e), inductance(l) or current(i)?: ").lower()
            if find == "e":
                l = float(input("What is the inductance (H)?: "))
                i = float(input("What is the current (A)?: "))
                e = 0.5 * l * i ** 2
                print(f"The energy stored is {e:.4f} J")
            elif find == "l":
                e = float(input("What is the energy stored (J)?: "))
                i = float(input("What is the current (A)?: "))
                l = 2 * e / i ** 2
                print(f"The inductance is {l:.6f} H")
            elif find == "i":
                e = float(input("What is the energy stored (J)?: "))
                l = float(input("What is the inductance (H)?: "))
                i = math.sqrt(2 * e / l)
                print(f"The current is {i:.4f} A")
 
        elif eqn == "transformer":
            find = input("Do you want to find secondary voltage(vs), primary voltage(vp), secondary turns(ns) or primary turns(np)?: ").lower()
            if find != "vs":
                vs = float(input("What is the secondary voltage (V)?: "))
            if find != "vp":
                vp = float(input("What is the primary voltage (V)?: "))
            if find != "ns":
                ns = float(input("What is the number of secondary turns?: "))
            if find != "np":
                np_ = float(input("What is the number of primary turns?: "))
            if find == "vs":
                vs = vp * ns / np_
                print(f"The secondary voltage is {vs:.4f} V")
            elif find == "vp":
                vp = vs * np_ / ns
                print(f"The primary voltage is {vp:.4f} V")
            elif find == "ns":
                ns = np_ * vs / vp
                print(f"The number of secondary turns is {ns:.2f}")
            elif find == "np":
                np_ = ns * vp / vs
                print(f"The number of primary turns is {np_:.2f}")
 
 
def wave_motion_soundf():
    while True:
        eqn = input("Are you working with wave speed(speed), period(period), speed of sound in air(sound), Doppler effect(doppler), intensity(intensity), sound level(level), beats(beats), string or open pipe(string) or closed pipe(closed) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "speed":
            find = input("Do you want to find the speed(v), frequency(f) or wavelength(w)?: ").lower()
            if find == "v":
                f = float(input("What is the frequency (Hz)?: "))
                w = float(input("What is the wavelength (m)?: "))
                v = f * w
                print(f"The wave speed is {v:.4f} m/s")
            elif find == "f":
                v = float(input("What is the wave speed (m/s)?: "))
                w = float(input("What is the wavelength (m)?: "))
                f = v / w
                print(f"The frequency is {f:.4f} Hz")
            elif find == "w":
                v = float(input("What is the wave speed (m/s)?: "))
                f = float(input("What is the frequency (Hz)?: "))
                w = v / f
                print(f"The wavelength is {w:.4f} m")
 
        elif eqn == "period":
            find = input("Do you want to find the period(t) or frequency(f)?: ").lower()
            if find == "t":
                f = float(input("What is the frequency (Hz)?: "))
                print(f"The period is {1 / f:.4f} s")
            elif find == "f":
                t = float(input("What is the period (s)?: "))
                print(f"The frequency is {1 / t:.4f} Hz")
 
        elif eqn == "sound":
            find = input("Do you want to find the speed of sound(v) or the air temperature(t)?: ").lower()
            if find == "v":
                temp = float(input("What is the air temperature (°C)?: "))
                v = 331 + 0.6 * temp
                print(f"The speed of sound is {v:.2f} m/s")
            elif find == "t":
                v = float(input("What is the speed of sound (m/s)?: "))
                temp = (v - 331) / 0.6
                print(f"The air temperature is {temp:.2f} °C")
 
        elif eqn == "doppler":
            find = input("Do you want to find the observed frequency(fo), source frequency(fs), observer velocity(vo) or source velocity(vs)?: ").lower()
            v = float(input("What is the speed of sound (m/s)?: "))
            if find != "fo":
                fo = float(input("What is the observed frequency (Hz)?: "))
            if find != "fs":
                fs = float(input("What is the source frequency (Hz)?: "))
            if find != "vo":
                vo = float(input("What is the observer velocity (m/s, + toward source)?: "))
            if find != "vs":
                vs = float(input("What is the source velocity (m/s, + toward observer)?: "))
            if find == "fo":
                fo = fs * (v + vo) / (v - vs)
                print(f"The observed frequency is {fo:.4f} Hz")
            elif find == "fs":
                fs = fo * (v - vs) / (v + vo)
                print(f"The source frequency is {fs:.4f} Hz")
            elif find == "vo":
                vo = fo * (v - vs) / fs - v
                print(f"The observer velocity is {vo:.4f} m/s")
            elif find == "vs":
                vs = v - fs * (v + vo) / fo
                print(f"The source velocity is {vs:.4f} m/s")
 
        elif eqn == "intensity":
            find = input("Do you want to find the intensity(i), power(p) or area(a)?: ").lower()
            if find == "i":
                p = float(input("What is the power (W)?: "))
                a = float(input("What is the area (m^2)?: "))
                print(f"The intensity is {p / a:.6f} W/m^2")
            elif find == "p":
                i = float(input("What is the intensity (W/m^2)?: "))
                a = float(input("What is the area (m^2)?: "))
                print(f"The power is {i * a:.6f} W")
            elif find == "a":
                i = float(input("What is the intensity (W/m^2)?: "))
                p = float(input("What is the power (W)?: "))
                print(f"The area is {p / i:.6f} m^2")
 
        elif eqn == "level":
            find = input("Do you want to find the sound level(b) or the intensity(i)?: ").lower()
            if find == "b":
                i = float(input("What is the intensity (W/m^2)?: "))
                beta = 10 * math.log10(i / I0_sound)
                print(f"The sound level is {beta:.2f} dB")
            elif find == "i":
                beta = float(input("What is the sound level (dB)?: "))
                i = I0_sound * 10 ** (beta / 10)
                print(f"The intensity is {i:.4e} W/m^2")
 
        elif eqn == "beats":
            find = input("Do you want to find the beat frequency(b) or one of the frequencies(f)?: ").lower()
            if find == "b":
                f1 = float(input("What is the first frequency (Hz)?: "))
                f2 = float(input("What is the second frequency (Hz)?: "))
                print(f"The beat frequency is {abs(f1 - f2):.4f} Hz")
            elif find == "f":
                fb = float(input("What is the beat frequency (Hz)?: "))
                f2 = float(input("What is the known frequency (Hz)?: "))
                print(f"The other frequency is {f2 + fb:.4f} Hz or {f2 - fb:.4f} Hz")
 
        elif eqn in ["string", "closed"]:
            k = 2 if eqn == "string" else 4
            find = input("Do you want to find the frequency(f), harmonic number(n), wave speed(v) or length(l)?: ").lower()
            if find != "f":
                f = float(input("What is the frequency (Hz)?: "))
            if find != "n":
                n = float(input("What is the harmonic number?: "))
            if find != "v":
                v = float(input("What is the wave speed (m/s)?: "))
            if find != "l":
                l = float(input("What is the length (m)?: "))
            if find == "f":
                f = n * v / (k * l)
                print(f"The frequency is {f:.4f} Hz")
            elif find == "n":
                n = k * l * f / v
                print(f"The harmonic number is {n:.2f}")
            elif find == "v":
                v = k * l * f / n
                print(f"The wave speed is {v:.4f} m/s")
            elif find == "l":
                l = n * v / (k * f)
                print(f"The length is {l:.4f} m")
 
 
def thermal_propertiesf():
    while True:
        eqn = input("Are you working with heat energy(heat), latent heat(latent), thermal expansion(expansion), thermal conduction(conduction) or ideal gas law(gas) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "heat":
            find = input("Do you want to find the heat(q), mass(m), specific heat capacity(c) or temperature change(t)?: ").lower()
            if find != "q":
                q = float(input("What is the heat energy (J)?: "))
            if find != "m":
                m = float(input("What is the mass (kg)?: "))
            if find != "c":
                c = float(input("What is the specific heat capacity (J/kg·K)?: "))
            if find != "t":
                dt = float(input("What is the temperature change (K)?: "))
            if find == "q":
                q = m * c * dt
                print(f"The heat energy is {q:.4f} J")
            elif find == "m":
                m = q / (c * dt)
                print(f"The mass is {m:.4f} kg")
            elif find == "c":
                c = q / (m * dt)
                print(f"The specific heat capacity is {c:.4f} J/kg·K")
            elif find == "t":
                dt = q / (m * c)
                print(f"The temperature change is {dt:.4f} K")
 
        elif eqn == "latent":
            find = input("Do you want to find the heat(q), mass(m) or specific latent heat(l)?: ").lower()
            if find == "q":
                m = float(input("What is the mass (kg)?: "))
                l = float(input("What is the specific latent heat (J/kg)?: "))
                print(f"The heat energy is {m * l:.4f} J")
            elif find == "m":
                q = float(input("What is the heat energy (J)?: "))
                l = float(input("What is the specific latent heat (J/kg)?: "))
                print(f"The mass is {q / l:.4f} kg")
            elif find == "l":
                q = float(input("What is the heat energy (J)?: "))
                m = float(input("What is the mass (kg)?: "))
                print(f"The specific latent heat is {q / m:.4f} J/kg")
 
        elif eqn == "expansion":
            kind = input("Is it linear(l), area(a) or volume(v) expansion?: ").lower()
            names = {"l": "length", "a": "area", "v": "volume"}
            name = names[kind]
            find = input(f"Do you want to find the change in {name}(d), original {name}(o), expansion coefficient(c) or temperature change(t)?: ").lower()
            if find != "d":
                d = float(input(f"What is the change in {name}?: "))
            if find != "o":
                o = float(input(f"What is the original {name}?: "))
            if find != "c":
                c = float(input("What is the expansion coefficient (per K)?: "))
            if find != "t":
                dt = float(input("What is the temperature change (K)?: "))
            if find == "d":
                d = o * c * dt
                print(f"The change in {name} is {d:.6f}")
            elif find == "o":
                o = d / (c * dt)
                print(f"The original {name} is {o:.6f}")
            elif find == "c":
                c = d / (o * dt)
                print(f"The expansion coefficient is {c:.4e} per K")
            elif find == "t":
                dt = d / (o * c)
                print(f"The temperature change is {dt:.4f} K")
 
        elif eqn == "conduction":
            find = input("Do you want to find the heat flow rate(r), conductivity(k), area(a), temperature difference(t) or thickness(d)?: ").lower()
            if find != "r":
                rate = float(input("What is the rate of heat flow (W)?: "))
            if find != "k":
                k = float(input("What is the thermal conductivity (W/m·K)?: "))
            if find != "a":
                a = float(input("What is the cross-sectional area (m^2)?: "))
            if find != "t":
                dt = float(input("What is the temperature difference (K)?: "))
            if find != "d":
                d = float(input("What is the thickness (m)?: "))
            if find == "r":
                rate = k * a * dt / d
                print(f"The rate of heat flow is {rate:.4f} W")
            elif find == "k":
                k = rate * d / (a * dt)
                print(f"The thermal conductivity is {k:.4f} W/m·K")
            elif find == "a":
                a = rate * d / (k * dt)
                print(f"The area is {a:.6f} m^2")
            elif find == "t":
                dt = rate * d / (k * a)
                print(f"The temperature difference is {dt:.4f} K")
            elif find == "d":
                d = k * a * dt / rate
                print(f"The thickness is {d:.6f} m")
 
        elif eqn == "gas":
            find = input("Do you want to find pressure(p), volume(v), moles(n) or temperature(t)?: ").lower()
            if find != "p":
                p = float(input("What is the pressure (Pa)?: "))
            if find != "v":
                v = float(input("What is the volume (m^3)?: "))
            if find != "n":
                n = float(input("What is the number of moles?: "))
            if find != "t":
                t = float(input("What is the temperature (K)?: "))
            if find == "p":
                p = n * R_gas * t / v
                print(f"The pressure is {p:.4f} Pa")
            elif find == "v":
                v = n * R_gas * t / p
                print(f"The volume is {v:.6f} m^3")
            elif find == "n":
                n = p * v / (R_gas * t)
                print(f"The number of moles is {n:.4f}")
            elif find == "t":
                t = p * v / (n * R_gas)
                print(f"The temperature is {t:.4f} K")
 
 
def shmf():
    while True:
        eqn = input("Are you working with displacement(x), velocity(v), velocity from displacement(vx), acceleration(a), angular frequency(omega), spring period(spring), pendulum period(pendulum), max velocity(vmax), max acceleration(amax) or energy(energy) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "x":
            find = input("Do you want to find the displacement(x), amplitude(a), angular frequency(w), time(t) or phase constant(p)?: ").lower()
            if find != "x":
                x = float(input("What is the displacement (m)?: "))
            if find != "a":
                A = float(input("What is the amplitude (m)?: "))
            if find != "w":
                w = float(input("What is the angular frequency (rad/s)?: "))
            if find != "t":
                t = float(input("What is the time (s)?: "))
            if find != "p":
                phi = float(input("What is the phase constant (rad, 0 if none)?: "))
            if find == "x":
                x = A * math.cos(w * t + phi)
                print(f"The displacement is {x:.4f} m")
            elif find == "a":
                A = x / math.cos(w * t + phi)
                print(f"The amplitude is {A:.4f} m")
            elif find == "w":
                w = (math.acos(x / A) - phi) / t
                print(f"The angular frequency is {w:.4f} rad/s (principal solution)")
            elif find == "t":
                t = (math.acos(x / A) - phi) / w
                print(f"The time is {t:.4f} s (first time it happens)")
            elif find == "p":
                phi = math.acos(x / A) - w * t
                print(f"The phase constant is {phi:.4f} rad (principal solution)")
 
        elif eqn == "v":
            find = input("Do you want to find the velocity(v), amplitude(a) or the phase angle wt+phi(p)?: ").lower()
            if find == "v":
                A = float(input("What is the amplitude (m)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                ph = float(input("What is the phase angle wt+phi (rad)?: "))
                v = -A * w * math.sin(ph)
                print(f"The velocity is {v:.4f} m/s")
            elif find == "a":
                v = float(input("What is the velocity (m/s)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                ph = float(input("What is the phase angle wt+phi (rad)?: "))
                A = -v / (w * math.sin(ph))
                print(f"The amplitude is {A:.4f} m")
            elif find == "p":
                v = float(input("What is the velocity (m/s)?: "))
                A = float(input("What is the amplitude (m)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                ph = math.asin(-v / (A * w))
                print(f"The phase angle is {ph:.4f} rad (principal solution)")
 
        elif eqn == "vx":
            find = input("Do you want to find the speed(v), angular frequency(w), amplitude(a) or displacement(x)?: ").lower()
            if find != "v":
                v = float(input("What is the speed (m/s)?: "))
            if find != "w":
                w = float(input("What is the angular frequency (rad/s)?: "))
            if find != "a":
                A = float(input("What is the amplitude (m)?: "))
            if find != "x":
                x = float(input("What is the displacement (m)?: "))
            if find == "v":
                v = w * math.sqrt(A ** 2 - x ** 2)
                print(f"The speed is {v:.4f} m/s")
            elif find == "w":
                w = v / math.sqrt(A ** 2 - x ** 2)
                print(f"The angular frequency is {w:.4f} rad/s")
            elif find == "a":
                A = math.sqrt(x ** 2 + (v / w) ** 2)
                print(f"The amplitude is {A:.4f} m")
            elif find == "x":
                x = math.sqrt(A ** 2 - (v / w) ** 2)
                print(f"The displacement is {x:.4f} m")
 
        elif eqn == "a":
            find = input("Do you want to find the acceleration(a), angular frequency(w) or displacement(x)?: ").lower()
            if find == "a":
                w = float(input("What is the angular frequency (rad/s)?: "))
                x = float(input("What is the displacement (m)?: "))
                print(f"The acceleration is {-w ** 2 * x:.4f} m/s^2")
            elif find == "w":
                a = float(input("What is the acceleration (m/s^2)?: "))
                x = float(input("What is the displacement (m)?: "))
                print(f"The angular frequency is {math.sqrt(-a / x):.4f} rad/s")
            elif find == "x":
                a = float(input("What is the acceleration (m/s^2)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The displacement is {-a / w ** 2:.4f} m")
 
        elif eqn == "omega":
            find = input("Do you want to find w from frequency(wf), w from period(wt), frequency from w(f) or period from w(t)?: ").lower()
            if find == "wf":
                f = float(input("What is the frequency (Hz)?: "))
                print(f"The angular frequency is {2 * math.pi * f:.4f} rad/s")
            elif find == "wt":
                t = float(input("What is the period (s)?: "))
                print(f"The angular frequency is {2 * math.pi / t:.4f} rad/s")
            elif find == "f":
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The frequency is {w / (2 * math.pi):.4f} Hz")
            elif find == "t":
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The period is {2 * math.pi / w:.4f} s")
 
        elif eqn == "spring":
            find = input("Do you want to find the period(t), mass(m) or spring constant(k)?: ").lower()
            if find == "t":
                m = float(input("What is the mass (kg)?: "))
                k = float(input("What is the spring constant (N/m)?: "))
                print(f"The period is {2 * math.pi * math.sqrt(m / k):.4f} s")
            elif find == "m":
                t = float(input("What is the period (s)?: "))
                k = float(input("What is the spring constant (N/m)?: "))
                print(f"The mass is {k * (t / (2 * math.pi)) ** 2:.4f} kg")
            elif find == "k":
                t = float(input("What is the period (s)?: "))
                m = float(input("What is the mass (kg)?: "))
                print(f"The spring constant is {m * (2 * math.pi / t) ** 2:.4f} N/m")
 
        elif eqn == "pendulum":
            find = input("Do you want to find the period(t), length(l) or gravitational acceleration(g)?: ").lower()
            if find == "t":
                l = float(input("What is the length (m)?: "))
                print(f"The period is {2 * math.pi * math.sqrt(l / g):.4f} s")
            elif find == "l":
                t = float(input("What is the period (s)?: "))
                print(f"The length is {g * (t / (2 * math.pi)) ** 2:.4f} m")
            elif find == "g":
                t = float(input("What is the period (s)?: "))
                l = float(input("What is the length (m)?: "))
                print(f"The gravitational acceleration is {l * (2 * math.pi / t) ** 2:.4f} m/s^2")
 
        elif eqn == "vmax":
            find = input("Do you want to find the max velocity(v), amplitude(a) or angular frequency(w)?: ").lower()
            if find == "v":
                A = float(input("What is the amplitude (m)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The maximum velocity is {A * w:.4f} m/s")
            elif find == "a":
                v = float(input("What is the maximum velocity (m/s)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The amplitude is {v / w:.4f} m")
            elif find == "w":
                v = float(input("What is the maximum velocity (m/s)?: "))
                A = float(input("What is the amplitude (m)?: "))
                print(f"The angular frequency is {v / A:.4f} rad/s")
 
        elif eqn == "amax":
            find = input("Do you want to find the max acceleration(a), amplitude(amp) or angular frequency(w)?: ").lower()
            if find == "a":
                A = float(input("What is the amplitude (m)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The maximum acceleration is {A * w ** 2:.4f} m/s^2")
            elif find == "amp":
                a = float(input("What is the maximum acceleration (m/s^2)?: "))
                w = float(input("What is the angular frequency (rad/s)?: "))
                print(f"The amplitude is {a / w ** 2:.4f} m")
            elif find == "w":
                a = float(input("What is the maximum acceleration (m/s^2)?: "))
                A = float(input("What is the amplitude (m)?: "))
                print(f"The angular frequency is {math.sqrt(a / A):.4f} rad/s")
 
        elif eqn == "energy":
            kind = input("Is it total energy(total), kinetic energy(ke) or potential energy(pe)?: ").lower()
            if kind == "total":
                find = input("Do you want to find the total energy(e), spring constant(k) or amplitude(a)?: ").lower()
                if find == "e":
                    k = float(input("What is the spring constant (N/m)?: "))
                    A = float(input("What is the amplitude (m)?: "))
                    print(f"The total energy is {0.5 * k * A ** 2:.4f} J")
                elif find == "k":
                    e = float(input("What is the total energy (J)?: "))
                    A = float(input("What is the amplitude (m)?: "))
                    print(f"The spring constant is {2 * e / A ** 2:.4f} N/m")
                elif find == "a":
                    e = float(input("What is the total energy (J)?: "))
                    k = float(input("What is the spring constant (N/m)?: "))
                    print(f"The amplitude is {math.sqrt(2 * e / k):.4f} m")
            elif kind == "ke":
                find = input("Do you want to find the kinetic energy(e), mass(m) or velocity(v)?: ").lower()
                if find == "e":
                    m = float(input("What is the mass (kg)?: "))
                    v = float(input("What is the velocity (m/s)?: "))
                    print(f"The kinetic energy is {0.5 * m * v ** 2:.4f} J")
                elif find == "m":
                    e = float(input("What is the kinetic energy (J)?: "))
                    v = float(input("What is the velocity (m/s)?: "))
                    print(f"The mass is {2 * e / v ** 2:.4f} kg")
                elif find == "v":
                    e = float(input("What is the kinetic energy (J)?: "))
                    m = float(input("What is the mass (kg)?: "))
                    print(f"The velocity is {math.sqrt(2 * e / m):.4f} m/s")
            elif kind == "pe":
                find = input("Do you want to find the potential energy(e), spring constant(k) or displacement(x)?: ").lower()
                if find == "e":
                    k = float(input("What is the spring constant (N/m)?: "))
                    x = float(input("What is the displacement (m)?: "))
                    print(f"The potential energy is {0.5 * k * x ** 2:.4f} J")
                elif find == "k":
                    e = float(input("What is the potential energy (J)?: "))
                    x = float(input("What is the displacement (m)?: "))
                    print(f"The spring constant is {2 * e / x ** 2:.4f} N/m")
                elif find == "x":
                    e = float(input("What is the potential energy (J)?: "))
                    k = float(input("What is the spring constant (N/m)?: "))
                    print(f"The displacement is {math.sqrt(2 * e / k):.4f} m")
 
 
def fluid_dynamicsf():
    while True:
        eqn = input("Are you working with density(density), pressure(pressure), pressure at depth(depth), Pascal's principle(pascal), Archimedes' principle(archimedes), continuity(continuity), Bernoulli(bernoulli), Poiseuille's law(poiseuille) or Reynolds number(reynolds) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "density":
            find = input("Do you want to find the density(d), mass(m) or volume(v)?: ").lower()
            if find == "d":
                m = float(input("What is the mass (kg)?: "))
                v = float(input("What is the volume (m^3)?: "))
                print(f"The density is {m / v:.4f} kg/m^3")
            elif find == "m":
                rho = float(input("What is the density (kg/m^3)?: "))
                v = float(input("What is the volume (m^3)?: "))
                print(f"The mass is {rho * v:.4f} kg")
            elif find == "v":
                m = float(input("What is the mass (kg)?: "))
                rho = float(input("What is the density (kg/m^3)?: "))
                print(f"The volume is {m / rho:.6f} m^3")
 
        elif eqn == "pressure":
            find = input("Do you want to find the pressure(p), force(f) or area(a)?: ").lower()
            if find == "p":
                f = float(input("What is the force (N)?: "))
                a = float(input("What is the area (m^2)?: "))
                print(f"The pressure is {f / a:.4f} Pa")
            elif find == "f":
                p = float(input("What is the pressure (Pa)?: "))
                a = float(input("What is the area (m^2)?: "))
                print(f"The force is {p * a:.4f} N")
            elif find == "a":
                f = float(input("What is the force (N)?: "))
                p = float(input("What is the pressure (Pa)?: "))
                print(f"The area is {f / p:.6f} m^2")
 
        elif eqn == "depth":
            find = input("Do you want to find the pressure at depth(p), surface pressure(p0), density(r) or depth(d)?: ").lower()
            if find != "p":
                p = float(input("What is the pressure at depth (Pa)?: "))
            if find != "p0":
                p0 = float(input("What is the surface pressure (Pa)?: "))
            if find != "r":
                rho = float(input("What is the fluid density (kg/m^3)?: "))
            if find != "d":
                d = float(input("What is the depth (m)?: "))
            if find == "p":
                p = p0 + rho * g * d
                print(f"The pressure at depth is {p:.4f} Pa")
            elif find == "p0":
                p0 = p - rho * g * d
                print(f"The surface pressure is {p0:.4f} Pa")
            elif find == "r":
                rho = (p - p0) / (g * d)
                print(f"The density is {rho:.4f} kg/m^3")
            elif find == "d":
                d = (p - p0) / (rho * g)
                print(f"The depth is {d:.4f} m")
 
        elif eqn == "pascal":
            find = input("Do you want to find force 1(f1), area 1(a1), force 2(f2) or area 2(a2)?: ").lower()
            if find != "f1":
                f1 = float(input("What is force 1 (N)?: "))
            if find != "a1":
                a1 = float(input("What is area 1 (m^2)?: "))
            if find != "f2":
                f2 = float(input("What is force 2 (N)?: "))
            if find != "a2":
                a2 = float(input("What is area 2 (m^2)?: "))
            if find == "f1":
                f1 = f2 * a1 / a2
                print(f"Force 1 is {f1:.4f} N")
            elif find == "a1":
                a1 = f1 * a2 / f2
                print(f"Area 1 is {a1:.6f} m^2")
            elif find == "f2":
                f2 = f1 * a2 / a1
                print(f"Force 2 is {f2:.4f} N")
            elif find == "a2":
                a2 = f2 * a1 / f1
                print(f"Area 2 is {a2:.6f} m^2")
 
        elif eqn == "archimedes":
            find = input("Do you want to find the buoyant force(f), fluid density(r) or displaced volume(v)?: ").lower()
            if find == "f":
                rho = float(input("What is the fluid density (kg/m^3)?: "))
                v = float(input("What is the displaced volume (m^3)?: "))
                print(f"The buoyant force is {rho * v * g:.4f} N")
            elif find == "r":
                fb = float(input("What is the buoyant force (N)?: "))
                v = float(input("What is the displaced volume (m^3)?: "))
                print(f"The fluid density is {fb / (v * g):.4f} kg/m^3")
            elif find == "v":
                fb = float(input("What is the buoyant force (N)?: "))
                rho = float(input("What is the fluid density (kg/m^3)?: "))
                print(f"The displaced volume is {fb / (rho * g):.6f} m^3")
 
        elif eqn == "continuity":
            find = input("Do you want to find area 1(a1), velocity 1(v1), area 2(a2) or velocity 2(v2)?: ").lower()
            if find != "a1":
                a1 = float(input("What is area 1 (m^2)?: "))
            if find != "v1":
                v1 = float(input("What is velocity 1 (m/s)?: "))
            if find != "a2":
                a2 = float(input("What is area 2 (m^2)?: "))
            if find != "v2":
                v2 = float(input("What is velocity 2 (m/s)?: "))
            if find == "a1":
                a1 = a2 * v2 / v1
                print(f"Area 1 is {a1:.6f} m^2")
            elif find == "v1":
                v1 = a2 * v2 / a1
                print(f"Velocity 1 is {v1:.4f} m/s")
            elif find == "a2":
                a2 = a1 * v1 / v2
                print(f"Area 2 is {a2:.6f} m^2")
            elif find == "v2":
                v2 = a1 * v1 / a2
                print(f"Velocity 2 is {v2:.4f} m/s")
 
        elif eqn == "bernoulli":
            find = input("Do you want to find pressure 1(p1), pressure 2(p2), velocity 1(v1), velocity 2(v2), height 1(h1) or height 2(h2)?: ").lower()
            rho = float(input("What is the fluid density (kg/m^3)?: "))
            if find != "p1":
                p1 = float(input("What is pressure 1 (Pa)?: "))
            if find != "p2":
                p2 = float(input("What is pressure 2 (Pa)?: "))
            if find != "v1":
                v1 = float(input("What is velocity 1 (m/s)?: "))
            if find != "v2":
                v2 = float(input("What is velocity 2 (m/s)?: "))
            if find != "h1":
                h1 = float(input("What is height 1 (m)?: "))
            if find != "h2":
                h2 = float(input("What is height 2 (m)?: "))
            if find == "p1":
                p1 = p2 + 0.5 * rho * (v2 ** 2 - v1 ** 2) + rho * g * (h2 - h1)
                print(f"Pressure 1 is {p1:.4f} Pa")
            elif find == "p2":
                p2 = p1 + 0.5 * rho * (v1 ** 2 - v2 ** 2) + rho * g * (h1 - h2)
                print(f"Pressure 2 is {p2:.4f} Pa")
            elif find == "v1":
                v1 = math.sqrt(v2 ** 2 + 2 * (p2 - p1) / rho + 2 * g * (h2 - h1))
                print(f"Velocity 1 is {v1:.4f} m/s")
            elif find == "v2":
                v2 = math.sqrt(v1 ** 2 + 2 * (p1 - p2) / rho + 2 * g * (h1 - h2))
                print(f"Velocity 2 is {v2:.4f} m/s")
            elif find == "h1":
                h1 = h2 + (p2 - p1) / (rho * g) + (v2 ** 2 - v1 ** 2) / (2 * g)
                print(f"Height 1 is {h1:.4f} m")
            elif find == "h2":
                h2 = h1 + (p1 - p2) / (rho * g) + (v1 ** 2 - v2 ** 2) / (2 * g)
                print(f"Height 2 is {h2:.4f} m")
 
        elif eqn == "poiseuille":
            find = input("Do you want to find the flow rate(q), radius(r), pressure difference(p), viscosity(n) or length(l)?: ").lower()
            if find != "q":
                q = float(input("What is the volumetric flow rate (m^3/s)?: "))
            if find != "r":
                r = float(input("What is the pipe radius (m)?: "))
            if find != "p":
                dp = float(input("What is the pressure difference (Pa)?: "))
            if find != "n":
                eta = float(input("What is the viscosity (Pa·s)?: "))
            if find != "l":
                l = float(input("What is the pipe length (m)?: "))
            if find == "q":
                q = math.pi * r ** 4 * dp / (8 * eta * l)
                print(f"The flow rate is {q:.6e} m^3/s")
            elif find == "r":
                r = (8 * eta * l * q / (math.pi * dp)) ** 0.25
                print(f"The radius is {r:.6f} m")
            elif find == "p":
                dp = 8 * eta * l * q / (math.pi * r ** 4)
                print(f"The pressure difference is {dp:.4f} Pa")
            elif find == "n":
                eta = math.pi * r ** 4 * dp / (8 * l * q)
                print(f"The viscosity is {eta:.6f} Pa·s")
            elif find == "l":
                l = math.pi * r ** 4 * dp / (8 * eta * q)
                print(f"The length is {l:.4f} m")
 
        elif eqn == "reynolds":
            find = input("Do you want to find the Reynolds number(re), density(r), velocity(v), length(l) or viscosity(n)?: ").lower()
            if find != "re":
                re = float(input("What is the Reynolds number?: "))
            if find != "r":
                rho = float(input("What is the density (kg/m^3)?: "))
            if find != "v":
                v = float(input("What is the velocity (m/s)?: "))
            if find != "l":
                l = float(input("What is the characteristic length (m)?: "))
            if find != "n":
                eta = float(input("What is the viscosity (Pa·s)?: "))
            if find == "re":
                re = rho * v * l / eta
                print(f"The Reynolds number is {re:.4f}")
            elif find == "r":
                rho = re * eta / (v * l)
                print(f"The density is {rho:.4f} kg/m^3")
            elif find == "v":
                v = re * eta / (rho * l)
                print(f"The velocity is {v:.4f} m/s")
            elif find == "l":
                l = re * eta / (rho * v)
                print(f"The length is {l:.4f} m")
            elif find == "n":
                eta = rho * v * l / re
                print(f"The viscosity is {eta:.6f} Pa·s")
 
 
def opticsf():
    while True:
        eqn = input("Are you working with the lens/mirror equation(lens), magnification(mag), lens maker's equation(maker), Snell's law(snell), critical angle(critical), lens power(power) or combined lenses(combined) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "lens":
            find = input("Do you want to find focal length(f), object distance(do) or image distance(di)?: ").lower()
            if find == "f":
                do = float(input("What is the object distance (m)?: "))
                di = float(input("What is the image distance (m)?: "))
                print(f"The focal length is {1 / (1 / do + 1 / di):.4f} m")
            elif find == "do":
                f = float(input("What is the focal length (m)?: "))
                di = float(input("What is the image distance (m)?: "))
                print(f"The object distance is {1 / (1 / f - 1 / di):.4f} m")
            elif find == "di":
                f = float(input("What is the focal length (m)?: "))
                do = float(input("What is the object distance (m)?: "))
                print(f"The image distance is {1 / (1 / f - 1 / do):.4f} m")
 
        elif eqn == "mag":
            find = input("Do you want to find magnification from distances(m), magnification from heights(mh), image distance(di), object distance(do), image height(hi) or object height(ho)?: ").lower()
            if find == "m":
                di = float(input("What is the image distance (m)?: "))
                do = float(input("What is the object distance (m)?: "))
                print(f"The magnification is {-di / do:.4f}")
            elif find == "mh":
                hi = float(input("What is the image height (m)?: "))
                ho = float(input("What is the object height (m)?: "))
                print(f"The magnification is {hi / ho:.4f}")
            elif find == "di":
                m = float(input("What is the magnification?: "))
                do = float(input("What is the object distance (m)?: "))
                print(f"The image distance is {-m * do:.4f} m")
            elif find == "do":
                m = float(input("What is the magnification?: "))
                di = float(input("What is the image distance (m)?: "))
                print(f"The object distance is {-di / m:.4f} m")
            elif find == "hi":
                m = float(input("What is the magnification?: "))
                ho = float(input("What is the object height (m)?: "))
                print(f"The image height is {m * ho:.4f} m")
            elif find == "ho":
                m = float(input("What is the magnification?: "))
                hi = float(input("What is the image height (m)?: "))
                print(f"The object height is {hi / m:.4f} m")
 
        elif eqn == "maker":
            find = input("Do you want to find focal length(f), refractive index(n), radius 1(r1) or radius 2(r2)?: ").lower()
            if find != "f":
                f = float(input("What is the focal length (m)?: "))
            if find != "n":
                n = float(input("What is the refractive index of the lens?: "))
            if find != "r1":
                r1 = float(input("What is radius of curvature 1 (m)?: "))
            if find != "r2":
                r2 = float(input("What is radius of curvature 2 (m)?: "))
            if find == "f":
                f = 1 / ((n - 1) * (1 / r1 - 1 / r2))
                print(f"The focal length is {f:.4f} m")
            elif find == "n":
                n = 1 / (f * (1 / r1 - 1 / r2)) + 1
                print(f"The refractive index is {n:.4f}")
            elif find == "r1":
                r1 = 1 / (1 / (f * (n - 1)) + 1 / r2)
                print(f"Radius 1 is {r1:.4f} m")
            elif find == "r2":
                r2 = 1 / (1 / r1 - 1 / (f * (n - 1)))
                print(f"Radius 2 is {r2:.4f} m")
 
        elif eqn == "snell":
            find = input("Do you want to find n1(n1), n2(n2), angle 1(a1) or angle 2(a2)?: ").lower()
            if find != "n1":
                n1 = float(input("What is n1?: "))
            if find != "n2":
                n2 = float(input("What is n2?: "))
            if find != "a1":
                θ1 = math.radians(float(input("What is angle 1 (degrees)?: ")))
            if find != "a2":
                θ2 = math.radians(float(input("What is angle 2 (degrees)?: ")))
            if find == "n1":
                n1 = n2 * math.sin(θ2) / math.sin(θ1)
                print(f"n1 is {n1:.4f}")
            elif find == "n2":
                n2 = n1 * math.sin(θ1) / math.sin(θ2)
                print(f"n2 is {n2:.4f}")
            elif find == "a1":
                θ1 = math.asin(n2 * math.sin(θ2) / n1)
                print(f"Angle 1 is {math.degrees(θ1):.2f} degrees")
            elif find == "a2":
                θ2 = math.asin(n1 * math.sin(θ1) / n2)
                print(f"Angle 2 is {math.degrees(θ2):.2f} degrees")
 
        elif eqn == "critical":
            find = input("Do you want to find the critical angle(c), n1(n1) or n2(n2)?: ").lower()
            if find == "c":
                n1 = float(input("What is n1 (denser medium)?: "))
                n2 = float(input("What is n2 (less dense medium)?: "))
                print(f"The critical angle is {math.degrees(math.asin(n2 / n1)):.2f} degrees")
            elif find == "n1":
                n2 = float(input("What is n2 (less dense medium)?: "))
                θc = math.radians(float(input("What is the critical angle (degrees)?: ")))
                print(f"n1 is {n2 / math.sin(θc):.4f}")
            elif find == "n2":
                n1 = float(input("What is n1 (denser medium)?: "))
                θc = math.radians(float(input("What is the critical angle (degrees)?: ")))
                print(f"n2 is {n1 * math.sin(θc):.4f}")
 
        elif eqn == "power":
            find = input("Do you want to find the power(p) or focal length(f)?: ").lower()
            if find == "p":
                f = float(input("What is the focal length (m)?: "))
                print(f"The lens power is {1 / f:.4f} D")
            elif find == "f":
                p = float(input("What is the lens power (D)?: "))
                print(f"The focal length is {1 / p:.4f} m")
 
        elif eqn == "combined":
            find = input("Do you want to find the total power(t) or an unknown lens power(u)?: ").lower()
            n = int(input("How many lenses in total (including the unknown one if any)?: "))
            known = 0
            count = n if find == "t" else n - 1
            for x in range(count):
                known += float(input(f"Enter power of lens {x + 1} (D): "))
            if find == "t":
                print(f"The total power is {known:.4f} D")
            elif find == "u":
                total = float(input("What is the total power (D)?: "))
                print(f"The unknown lens power is {total - known:.4f} D")
 
 
def electric_currents_magnetic_fieldsf():
    while True:
        eqn = input("Are you working with force on a moving charge(chargeforce), force on a wire(wireforce), field of a straight wire(wirefield), field of a solenoid(solenoid), field at a loop's center(loop) or torque on a loop(torque) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "chargeforce":
            find = input("Do you want to find the force(f), charge(q), velocity(v), field(b) or angle(a)?: ").lower()
            if find != "f":
                f = float(input("What is the force (N)?: "))
            if find != "q":
                q = float(input("What is the charge (C)?: "))
            if find != "v":
                v = float(input("What is the velocity (m/s)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find != "a":
                θ = math.radians(float(input("What is the angle between v and B (degrees)?: ")))
            if find == "f":
                f = q * v * b * math.sin(θ)
                print(f"The force is {f:.6e} N")
            elif find == "q":
                q = f / (v * b * math.sin(θ))
                print(f"The charge is {q:.6e} C")
            elif find == "v":
                v = f / (q * b * math.sin(θ))
                print(f"The velocity is {v:.4f} m/s")
            elif find == "b":
                b = f / (q * v * math.sin(θ))
                print(f"The magnetic field is {b:.6e} T")
            elif find == "a":
                θ = math.asin(f / (q * v * b))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
        elif eqn == "wireforce":
            find = input("Do you want to find the force(f), field(b), current(i), length(l) or angle(a)?: ").lower()
            if find != "f":
                f = float(input("What is the force (N)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find != "i":
                i = float(input("What is the current (A)?: "))
            if find != "l":
                l = float(input("What is the length of the wire (m)?: "))
            if find != "a":
                θ = math.radians(float(input("What is the angle between wire and B (degrees)?: ")))
            if find == "f":
                f = b * i * l * math.sin(θ)
                print(f"The force is {f:.6f} N")
            elif find == "b":
                b = f / (i * l * math.sin(θ))
                print(f"The magnetic field is {b:.6f} T")
            elif find == "i":
                i = f / (b * l * math.sin(θ))
                print(f"The current is {i:.4f} A")
            elif find == "l":
                l = f / (b * i * math.sin(θ))
                print(f"The length is {l:.4f} m")
            elif find == "a":
                θ = math.asin(f / (b * i * l))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
        elif eqn == "wirefield":
            find = input("Do you want to find the field(b), current(i) or distance(r)?: ").lower()
            if find == "b":
                i = float(input("What is the current (A)?: "))
                r = float(input("What is the distance from the wire (m)?: "))
                print(f"The magnetic field is {mu0 * i / (2 * math.pi * r):.6e} T")
            elif find == "i":
                b = float(input("What is the magnetic field (T)?: "))
                r = float(input("What is the distance from the wire (m)?: "))
                print(f"The current is {b * 2 * math.pi * r / mu0:.4f} A")
            elif find == "r":
                b = float(input("What is the magnetic field (T)?: "))
                i = float(input("What is the current (A)?: "))
                print(f"The distance is {mu0 * i / (2 * math.pi * b):.6f} m")
 
        elif eqn == "solenoid":
            find = input("Do you want to find the field(b), turns per metre(n) or current(i)?: ").lower()
            if find == "b":
                n = float(input("What is the number of turns per metre?: "))
                i = float(input("What is the current (A)?: "))
                print(f"The magnetic field is {mu0 * n * i:.6e} T")
            elif find == "n":
                b = float(input("What is the magnetic field (T)?: "))
                i = float(input("What is the current (A)?: "))
                print(f"The turns per metre is {b / (mu0 * i):.4f}")
            elif find == "i":
                b = float(input("What is the magnetic field (T)?: "))
                n = float(input("What is the number of turns per metre?: "))
                print(f"The current is {b / (mu0 * n):.4f} A")
 
        elif eqn == "loop":
            find = input("Do you want to find the field(b), current(i) or radius(r)?: ").lower()
            if find == "b":
                i = float(input("What is the current (A)?: "))
                r = float(input("What is the loop radius (m)?: "))
                print(f"The magnetic field is {mu0 * i / (2 * r):.6e} T")
            elif find == "i":
                b = float(input("What is the magnetic field (T)?: "))
                r = float(input("What is the loop radius (m)?: "))
                print(f"The current is {2 * r * b / mu0:.4f} A")
            elif find == "r":
                b = float(input("What is the magnetic field (T)?: "))
                i = float(input("What is the current (A)?: "))
                print(f"The radius is {mu0 * i / (2 * b):.6f} m")
 
        elif eqn == "torque":
            find = input("Do you want to find the torque(t), turns(n), current(i), area(a), field(b) or angle(th)?: ").lower()
            if find != "t":
                tau = float(input("What is the torque (N·m)?: "))
            if find != "n":
                n = float(input("What is the number of turns?: "))
            if find != "i":
                i = float(input("What is the current (A)?: "))
            if find != "a":
                a = float(input("What is the area of the loop (m^2)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find != "th":
                θ = math.radians(float(input("What is the angle between the normal and B (degrees)?: ")))
            if find == "t":
                tau = n * i * a * b * math.sin(θ)
                print(f"The torque is {tau:.6f} N·m")
            elif find == "n":
                n = tau / (i * a * b * math.sin(θ))
                print(f"The number of turns is {n:.2f}")
            elif find == "i":
                i = tau / (n * a * b * math.sin(θ))
                print(f"The current is {i:.4f} A")
            elif find == "a":
                a = tau / (n * i * b * math.sin(θ))
                print(f"The area is {a:.6f} m^2")
            elif find == "b":
                b = tau / (n * i * a * math.sin(θ))
                print(f"The magnetic field is {b:.6f} T")
            elif find == "th":
                θ = math.asin(tau / (n * i * a * b))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
 
def nuclear_physicsf():
    while True:
        eqn = input("Are you working with radioactive decay(decay), decay using half-life(halfdecay), half-life(halflife), activity(activity), mass-energy(massenergy) or binding energy(binding) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "decay":
            find = input("Do you want to find remaining nuclei(n), initial nuclei(n0), decay constant(l) or time(t)?: ").lower()
            if find != "n":
                n = float(input("What is the number of nuclei remaining?: "))
            if find != "n0":
                n0 = float(input("What is the initial number of nuclei?: "))
            if find != "l":
                lam = float(input("What is the decay constant (per s)?: "))
            if find != "t":
                t = float(input("What is the time (s)?: "))
            if find == "n":
                n = n0 * math.exp(-lam * t)
                print(f"The remaining nuclei is {n:.4e}")
            elif find == "n0":
                n0 = n / math.exp(-lam * t)
                print(f"The initial number of nuclei is {n0:.4e}")
            elif find == "l":
                lam = math.log(n0 / n) / t
                print(f"The decay constant is {lam:.4e} per s")
            elif find == "t":
                t = math.log(n0 / n) / lam
                print(f"The time is {t:.4e} s")
 
        elif eqn == "halfdecay":
            find = input("Do you want to find remaining nuclei(n), initial nuclei(n0), time(t) or half-life(h)?: ").lower()
            if find != "n":
                n = float(input("What is the number of nuclei remaining?: "))
            if find != "n0":
                n0 = float(input("What is the initial number of nuclei?: "))
            if find != "t":
                t = float(input("What is the time elapsed?: "))
            if find != "h":
                th = float(input("What is the half-life (same time unit as above)?: "))
            if find == "n":
                n = n0 * 0.5 ** (t / th)
                print(f"The remaining nuclei is {n:.4e}")
            elif find == "n0":
                n0 = n / 0.5 ** (t / th)
                print(f"The initial number of nuclei is {n0:.4e}")
            elif find == "t":
                t = th * math.log(n / n0) / math.log(0.5)
                print(f"The time elapsed is {t:.4f}")
            elif find == "h":
                th = t * math.log(0.5) / math.log(n / n0)
                print(f"The half-life is {th:.4f}")
 
        elif eqn == "halflife":
            find = input("Do you want to find the half-life(t) or decay constant(l)?: ").lower()
            if find == "t":
                lam = float(input("What is the decay constant (per s)?: "))
                print(f"The half-life is {math.log(2) / lam:.4e} s")
            elif find == "l":
                th = float(input("What is the half-life (s)?: "))
                print(f"The decay constant is {math.log(2) / th:.4e} per s")
 
        elif eqn == "activity":
            find = input("Do you want to find the activity(a), decay constant(l) or number of nuclei(n)?: ").lower()
            if find == "a":
                lam = float(input("What is the decay constant (per s)?: "))
                n = float(input("What is the number of nuclei?: "))
                print(f"The activity is {lam * n:.4e} Bq")
            elif find == "l":
                a = float(input("What is the activity (Bq)?: "))
                n = float(input("What is the number of nuclei?: "))
                print(f"The decay constant is {a / n:.4e} per s")
            elif find == "n":
                a = float(input("What is the activity (Bq)?: "))
                lam = float(input("What is the decay constant (per s)?: "))
                print(f"The number of nuclei is {a / lam:.4e}")
 
        elif eqn in ["massenergy", "binding"]:
            find = input("Do you want to find the energy(e) or the mass (defect)(m)?: ").lower()
            if find == "e":
                m = float(input("What is the mass (defect) (kg)?: "))
                print(f"The energy is {m * c_light ** 2:.4e} J")
            elif find == "m":
                e = float(input("What is the energy (J)?: "))
                print(f"The mass (defect) is {e / c_light ** 2:.4e} kg")
 
 
def quantum_mechanicsf():
    while True:
        eqn = input("Are you working with photon energy(photon), the photoelectric effect(photoelectric), threshold frequency(threshold), stopping potential(stopping) or de Broglie wavelength(debroglie) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "photon":
            find = input("Do you want to find energy from frequency(ef), frequency from energy(fe), energy from wavelength(ew), wavelength from energy(we), frequency from wavelength(fw) or wavelength from frequency(wf)?: ").lower()
            if find == "ef":
                f = float(input("What is the frequency (Hz)?: "))
                print(f"The photon energy is {h_planck * f:.4e} J")
            elif find == "fe":
                e = float(input("What is the energy (J)?: "))
                print(f"The frequency is {e / h_planck:.4e} Hz")
            elif find == "ew":
                w = float(input("What is the wavelength (m)?: "))
                print(f"The photon energy is {h_planck * c_light / w:.4e} J")
            elif find == "we":
                e = float(input("What is the energy (J)?: "))
                print(f"The wavelength is {h_planck * c_light / e:.4e} m")
            elif find == "fw":
                w = float(input("What is the wavelength (m)?: "))
                print(f"The frequency is {c_light / w:.4e} Hz")
            elif find == "wf":
                f = float(input("What is the frequency (Hz)?: "))
                print(f"The wavelength is {c_light / f:.4e} m")
 
        elif eqn == "photoelectric":
            find = input("Do you want to find the max kinetic energy(k), frequency(f) or work function(p)?: ").lower()
            if find == "k":
                f = float(input("What is the frequency (Hz)?: "))
                phi = float(input("What is the work function (J)?: "))
                print(f"The maximum kinetic energy is {h_planck * f - phi:.4e} J")
            elif find == "f":
                ke = float(input("What is the maximum kinetic energy (J)?: "))
                phi = float(input("What is the work function (J)?: "))
                print(f"The frequency is {(ke + phi) / h_planck:.4e} Hz")
            elif find == "p":
                ke = float(input("What is the maximum kinetic energy (J)?: "))
                f = float(input("What is the frequency (Hz)?: "))
                print(f"The work function is {h_planck * f - ke:.4e} J")
 
        elif eqn == "threshold":
            find = input("Do you want to find the threshold frequency(f) or work function(p)?: ").lower()
            if find == "f":
                phi = float(input("What is the work function (J)?: "))
                print(f"The threshold frequency is {phi / h_planck:.4e} Hz")
            elif find == "p":
                f0 = float(input("What is the threshold frequency (Hz)?: "))
                print(f"The work function is {h_planck * f0:.4e} J")
 
        elif eqn == "stopping":
            find = input("Do you want to find the stopping potential(v) or max kinetic energy(k)?: ").lower()
            if find == "v":
                ke = float(input("What is the maximum kinetic energy (J)?: "))
                print(f"The stopping potential is {ke / e_charge:.4f} V")
            elif find == "k":
                vs = float(input("What is the stopping potential (V)?: "))
                print(f"The maximum kinetic energy is {e_charge * vs:.4e} J")
 
        elif eqn == "debroglie":
            find = input("Do you want to find the wavelength(w), mass(m) or velocity(v)?: ").lower()
            if find == "w":
                m = float(input("What is the mass (kg)?: "))
                v = float(input("What is the velocity (m/s)?: "))
                print(f"The wavelength is {h_planck / (m * v):.4e} m")
            elif find == "m":
                w = float(input("What is the wavelength (m)?: "))
                v = float(input("What is the velocity (m/s)?: "))
                print(f"The mass is {h_planck / (w * v):.4e} kg")
            elif find == "v":
                w = float(input("What is the wavelength (m)?: "))
                m = float(input("What is the mass (kg)?: "))
                print(f"The velocity is {h_planck / (w * m):.4e} m/s")
 
 
def thermodynamicsf():
    while True:
        eqn = input("Are you working with the first law(first), work by a gas(work), efficiency(efficiency), Carnot efficiency(carnot), entropy(entropy) or internal energy of an ideal gas(internal) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "first":
            find = input("Do you want to find change in internal energy(u), heat added(q) or work done by the system(w)?: ").lower()
            if find == "u":
                q = float(input("What is the heat added (J)?: "))
                w = float(input("What is the work done by the system (J)?: "))
                print(f"The change in internal energy is {q - w:.4f} J")
            elif find == "q":
                du = float(input("What is the change in internal energy (J)?: "))
                w = float(input("What is the work done by the system (J)?: "))
                print(f"The heat added is {du + w:.4f} J")
            elif find == "w":
                q = float(input("What is the heat added (J)?: "))
                du = float(input("What is the change in internal energy (J)?: "))
                print(f"The work done by the system is {q - du:.4f} J")
 
        elif eqn == "work":
            find = input("Do you want to find the work(w), pressure(p) or change in volume(v)?: ").lower()
            if find == "w":
                p = float(input("What is the pressure (Pa)?: "))
                dv = float(input("What is the change in volume (m^3)?: "))
                print(f"The work done is {p * dv:.4f} J")
            elif find == "p":
                w = float(input("What is the work done (J)?: "))
                dv = float(input("What is the change in volume (m^3)?: "))
                print(f"The pressure is {w / dv:.4f} Pa")
            elif find == "v":
                w = float(input("What is the work done (J)?: "))
                p = float(input("What is the pressure (Pa)?: "))
                print(f"The change in volume is {w / p:.6f} m^3")
 
        elif eqn == "efficiency":
            find = input("Do you want to find the efficiency(e), work output(w) or heat input(q)?: ").lower()
            if find == "e":
                w = float(input("What is the work output (J)?: "))
                q = float(input("What is the heat input (J)?: "))
                print(f"The efficiency is {w / q * 100:.2f}%")
            elif find == "w":
                eff = float(input("What is the efficiency (%)?: ")) / 100
                q = float(input("What is the heat input (J)?: "))
                print(f"The work output is {eff * q:.4f} J")
            elif find == "q":
                eff = float(input("What is the efficiency (%)?: ")) / 100
                w = float(input("What is the work output (J)?: "))
                print(f"The heat input is {w / eff:.4f} J")
 
        elif eqn == "carnot":
            find = input("Do you want to find the efficiency(e), cold temperature(c) or hot temperature(h)?: ").lower()
            if find == "e":
                tc = float(input("What is the cold reservoir temperature (K)?: "))
                th = float(input("What is the hot reservoir temperature (K)?: "))
                print(f"The Carnot efficiency is {(1 - tc / th) * 100:.2f}%")
            elif find == "c":
                eff = float(input("What is the efficiency (%)?: ")) / 100
                th = float(input("What is the hot reservoir temperature (K)?: "))
                print(f"The cold reservoir temperature is {th * (1 - eff):.4f} K")
            elif find == "h":
                eff = float(input("What is the efficiency (%)?: ")) / 100
                tc = float(input("What is the cold reservoir temperature (K)?: "))
                print(f"The hot reservoir temperature is {tc / (1 - eff):.4f} K")
 
        elif eqn == "entropy":
            find = input("Do you want to find the entropy change(s), heat(q) or temperature(t)?: ").lower()
            if find == "s":
                q = float(input("What is the heat transferred (J)?: "))
                t = float(input("What is the temperature (K)?: "))
                print(f"The entropy change is {q / t:.6f} J/K")
            elif find == "q":
                ds = float(input("What is the entropy change (J/K)?: "))
                t = float(input("What is the temperature (K)?: "))
                print(f"The heat transferred is {ds * t:.4f} J")
            elif find == "t":
                q = float(input("What is the heat transferred (J)?: "))
                ds = float(input("What is the entropy change (J/K)?: "))
                print(f"The temperature is {q / ds:.4f} K")
 
        elif eqn == "internal":
            find = input("Do you want to find the internal energy(u), moles(n) or temperature(t)?: ").lower()
            if find == "u":
                n = float(input("What is the number of moles?: "))
                t = float(input("What is the temperature (K)?: "))
                print(f"The internal energy is {1.5 * n * R_gas * t:.4f} J")
            elif find == "n":
                u = float(input("What is the internal energy (J)?: "))
                t = float(input("What is the temperature (K)?: "))
                print(f"The number of moles is {u / (1.5 * R_gas * t):.4f}")
            elif find == "t":
                u = float(input("What is the internal energy (J)?: "))
                n = float(input("What is the number of moles?: "))
                print(f"The temperature is {u / (1.5 * n * R_gas):.4f} K")
 
 
def capacitors_circuitsf():
    while True:
        eqn = input("Are you working with capacitance(cap), energy stored(energy), series capacitors(series), parallel capacitors(parallel), parallel plate capacitor(plate), time constant(tau) or RC charging/discharging(rc) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "cap":
            find = input("Do you want to find capacitance(c), charge(q) or voltage(v)?: ").lower()
            if find == "c":
                q = float(input("What is the charge (C)?: "))
                v = float(input("What is the voltage (V)?: "))
                print(f"The capacitance is {q / v:.6e} F")
            elif find == "q":
                cap = float(input("What is the capacitance (F)?: "))
                v = float(input("What is the voltage (V)?: "))
                print(f"The charge is {cap * v:.6e} C")
            elif find == "v":
                q = float(input("What is the charge (C)?: "))
                cap = float(input("What is the capacitance (F)?: "))
                print(f"The voltage is {q / cap:.4f} V")
 
        elif eqn == "energy":
            find = input("Do you want to find the energy(e), capacitance(c) or voltage(v)?: ").lower()
            if find == "e":
                cap = float(input("What is the capacitance (F)?: "))
                v = float(input("What is the voltage (V)?: "))
                print(f"The energy stored is {0.5 * cap * v ** 2:.6e} J")
            elif find == "c":
                e = float(input("What is the energy stored (J)?: "))
                v = float(input("What is the voltage (V)?: "))
                print(f"The capacitance is {2 * e / v ** 2:.6e} F")
            elif find == "v":
                e = float(input("What is the energy stored (J)?: "))
                cap = float(input("What is the capacitance (F)?: "))
                print(f"The voltage is {math.sqrt(2 * e / cap):.4f} V")
 
        elif eqn == "series":
            find = input("Do you want to find the total capacitance(t) or an unknown capacitor(u)?: ").lower()
            n = int(input("How many capacitors in total (including the unknown one if any)?: "))
            known = 0
            count = n if find == "t" else n - 1
            for x in range(count):
                known += 1 / float(input(f"Enter capacitance {x + 1} (F): "))
            if find == "t":
                print(f"The total series capacitance is {1 / known:.6e} F")
            elif find == "u":
                total = float(input("What is the total series capacitance (F)?: "))
                print(f"The unknown capacitance is {1 / (1 / total - known):.6e} F")
 
        elif eqn == "parallel":
            find = input("Do you want to find the total capacitance(t) or an unknown capacitor(u)?: ").lower()
            n = int(input("How many capacitors in total (including the unknown one if any)?: "))
            known = 0
            count = n if find == "t" else n - 1
            for x in range(count):
                known += float(input(f"Enter capacitance {x + 1} (F): "))
            if find == "t":
                print(f"The total parallel capacitance is {known:.6e} F")
            elif find == "u":
                total = float(input("What is the total parallel capacitance (F)?: "))
                print(f"The unknown capacitance is {total - known:.6e} F")
 
        elif eqn == "plate":
            find = input("Do you want to find capacitance(c), area(a) or separation(d)?: ").lower()
            if find == "c":
                a = float(input("What is the plate area (m^2)?: "))
                d = float(input("What is the plate separation (m)?: "))
                print(f"The capacitance is {epsilon0 * a / d:.6e} F")
            elif find == "a":
                cap = float(input("What is the capacitance (F)?: "))
                d = float(input("What is the plate separation (m)?: "))
                print(f"The area is {cap * d / epsilon0:.6e} m^2")
            elif find == "d":
                cap = float(input("What is the capacitance (F)?: "))
                a = float(input("What is the plate area (m^2)?: "))
                print(f"The separation is {epsilon0 * a / cap:.6e} m")
 
        elif eqn == "tau":
            find = input("Do you want to find the time constant(t), resistance(r) or capacitance(c)?: ").lower()
            if find == "t":
                r = float(input("What is the resistance (Ω)?: "))
                cap = float(input("What is the capacitance (F)?: "))
                print(f"The time constant is {r * cap:.6e} s")
            elif find == "r":
                tau = float(input("What is the time constant (s)?: "))
                cap = float(input("What is the capacitance (F)?: "))
                print(f"The resistance is {tau / cap:.4f} Ω")
            elif find == "c":
                tau = float(input("What is the time constant (s)?: "))
                r = float(input("What is the resistance (Ω)?: "))
                print(f"The capacitance is {tau / r:.6e} F")
 
        elif eqn == "rc":
            kind = input("Is the capacitor charging(c) or discharging(d)?: ").lower()
            find = input("Do you want to find the voltage(v), initial/source voltage(v0) or time(t)?: ").lower()
            r = float(input("What is the resistance (Ω)?: "))
            cap = float(input("What is the capacitance (F)?: "))
            tau = r * cap
            if find != "v":
                v = float(input("What is the capacitor voltage (V)?: "))
            if find != "v0":
                v0 = float(input("What is the initial/source voltage (V)?: "))
            if find != "t":
                t = float(input("What is the time (s)?: "))
            if kind == "c":
                if find == "v":
                    v = v0 * (1 - math.exp(-t / tau))
                    print(f"The capacitor voltage is {v:.4f} V")
                elif find == "v0":
                    v0 = v / (1 - math.exp(-t / tau))
                    print(f"The source voltage is {v0:.4f} V")
                elif find == "t":
                    t = -tau * math.log(1 - v / v0)
                    print(f"The time is {t:.4f} s")
            elif kind == "d":
                if find == "v":
                    v = v0 * math.exp(-t / tau)
                    print(f"The capacitor voltage is {v:.4f} V")
                elif find == "v0":
                    v0 = v / math.exp(-t / tau)
                    print(f"The initial voltage is {v0:.4f} V")
                elif find == "t":
                    t = -tau * math.log(v / v0)
                    print(f"The time is {t:.4f} s")
 
 
def resistors_ohms_lawf():
    while True:
        eqn = input("Are you working with Ohm's law(ohms), series resistors(series), parallel resistors(parallel), power(power) or resistivity(resistivity) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "ohms":
            find = input("Do you want to find voltage(v), current(i) or resistance(r)?: ").lower()
            if find == "v":
                i = float(input("What is the current (A)?: "))
                r = float(input("What is the resistance (Ω)?: "))
                print(f"The voltage is {i * r:.4f} V")
            elif find == "i":
                v = float(input("What is the voltage (V)?: "))
                r = float(input("What is the resistance (Ω)?: "))
                print(f"The current is {v / r:.4f} A")
            elif find == "r":
                v = float(input("What is the voltage (V)?: "))
                i = float(input("What is the current (A)?: "))
                print(f"The resistance is {v / i:.4f} Ω")
 
        elif eqn == "series":
            find = input("Do you want to find the total resistance(t) or an unknown resistor(u)?: ").lower()
            n = int(input("How many resistors in total (including the unknown one if any)?: "))
            known = 0
            count = n if find == "t" else n - 1
            for x in range(count):
                known += float(input(f"Enter resistance {x + 1} (Ω): "))
            if find == "t":
                print(f"The total series resistance is {known:.4f} Ω")
            elif find == "u":
                total = float(input("What is the total series resistance (Ω)?: "))
                print(f"The unknown resistance is {total - known:.4f} Ω")
 
        elif eqn == "parallel":
            find = input("Do you want to find the total resistance(t) or an unknown resistor(u)?: ").lower()
            n = int(input("How many resistors in total (including the unknown one if any)?: "))
            known = 0
            count = n if find == "t" else n - 1
            for x in range(count):
                known += 1 / float(input(f"Enter resistance {x + 1} (Ω): "))
            if find == "t":
                print(f"The total parallel resistance is {1 / known:.4f} Ω")
            elif find == "u":
                total = float(input("What is the total parallel resistance (Ω)?: "))
                print(f"The unknown resistance is {1 / (1 / total - known):.4f} Ω")
 
        elif eqn == "power":
            known = input("Which two values do you know (vi, ir, vr)?: ").lower()
            find = input("Do you want to find power(p) or one of the other values?: ").lower()
            if known == "vi":
                if find == "p":
                    v = float(input("What is the voltage (V)?: "))
                    i = float(input("What is the current (A)?: "))
                    print(f"The power is {v * i:.4f} W")
                elif find == "v":
                    p = float(input("What is the power (W)?: "))
                    i = float(input("What is the current (A)?: "))
                    print(f"The voltage is {p / i:.4f} V")
                elif find == "i":
                    p = float(input("What is the power (W)?: "))
                    v = float(input("What is the voltage (V)?: "))
                    print(f"The current is {p / v:.4f} A")
            elif known == "ir":
                if find == "p":
                    i = float(input("What is the current (A)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    print(f"The power is {i ** 2 * r:.4f} W")
                elif find == "i":
                    p = float(input("What is the power (W)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    print(f"The current is {math.sqrt(p / r):.4f} A")
                elif find == "r":
                    p = float(input("What is the power (W)?: "))
                    i = float(input("What is the current (A)?: "))
                    print(f"The resistance is {p / i ** 2:.4f} Ω")
            elif known == "vr":
                if find == "p":
                    v = float(input("What is the voltage (V)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    print(f"The power is {v ** 2 / r:.4f} W")
                elif find == "v":
                    p = float(input("What is the power (W)?: "))
                    r = float(input("What is the resistance (Ω)?: "))
                    print(f"The voltage is {math.sqrt(p * r):.4f} V")
                elif find == "r":
                    p = float(input("What is the power (W)?: "))
                    v = float(input("What is the voltage (V)?: "))
                    print(f"The resistance is {v ** 2 / p:.4f} Ω")
 
        elif eqn == "resistivity":
            find = input("Do you want to find resistance(r), resistivity(p), length(l) or area(a)?: ").lower()
            if find != "r":
                r = float(input("What is the resistance (Ω)?: "))
            if find != "p":
                rho = float(input("What is the resistivity (Ω·m)?: "))
            if find != "l":
                l = float(input("What is the length (m)?: "))
            if find != "a":
                a = float(input("What is the cross-sectional area (m^2)?: "))
            if find == "r":
                r = rho * l / a
                print(f"The resistance is {r:.4f} Ω")
            elif find == "p":
                rho = r * a / l
                print(f"The resistivity is {rho:.6e} Ω·m")
            elif find == "l":
                l = r * a / rho
                print(f"The length is {l:.4f} m")
            elif find == "a":
                a = rho * l / r
                print(f"The area is {a:.6e} m^2")
 
 
def magnetism_magnetic_forcesf():
    while True:
        eqn = input("Are you working with force on a moving charge(chargeforce), force on a wire(wireforce), force between two wires(twowires), circular motion radius(radius), magnetic dipole moment(dipole) or velocity selector(selector) (q to quit): ").lower()
        if eqn == "q":
            quit()
 
        elif eqn == "chargeforce":
            find = input("Do you want to find the force(f), charge(q), velocity(v), field(b) or angle(a)?: ").lower()
            if find != "f":
                f = float(input("What is the force (N)?: "))
            if find != "q":
                q = float(input("What is the charge (C)?: "))
            if find != "v":
                v = float(input("What is the velocity (m/s)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find != "a":
                θ = math.radians(float(input("What is the angle between v and B (degrees)?: ")))
            if find == "f":
                f = q * v * b * math.sin(θ)
                print(f"The force is {f:.6e} N")
            elif find == "q":
                q = f / (v * b * math.sin(θ))
                print(f"The charge is {q:.6e} C")
            elif find == "v":
                v = f / (q * b * math.sin(θ))
                print(f"The velocity is {v:.4f} m/s")
            elif find == "b":
                b = f / (q * v * math.sin(θ))
                print(f"The magnetic field is {b:.6e} T")
            elif find == "a":
                θ = math.asin(f / (q * v * b))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
        elif eqn == "wireforce":
            find = input("Do you want to find the force(f), field(b), current(i), length(l) or angle(a)?: ").lower()
            if find != "f":
                f = float(input("What is the force (N)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find != "i":
                i = float(input("What is the current (A)?: "))
            if find != "l":
                l = float(input("What is the length of the wire (m)?: "))
            if find != "a":
                θ = math.radians(float(input("What is the angle between wire and B (degrees)?: ")))
            if find == "f":
                f = b * i * l * math.sin(θ)
                print(f"The force is {f:.6f} N")
            elif find == "b":
                b = f / (i * l * math.sin(θ))
                print(f"The magnetic field is {b:.6f} T")
            elif find == "i":
                i = f / (b * l * math.sin(θ))
                print(f"The current is {i:.4f} A")
            elif find == "l":
                l = f / (b * i * math.sin(θ))
                print(f"The length is {l:.4f} m")
            elif find == "a":
                θ = math.asin(f / (b * i * l))
                print(f"The angle is {math.degrees(θ):.2f} degrees")
 
        elif eqn == "twowires":
            find = input("Do you want to find the force(f), current 1(i1), current 2(i2), length(l) or separation(r)?: ").lower()
            if find != "f":
                f = float(input("What is the force (N)?: "))
            if find != "i1":
                i1 = float(input("What is current 1 (A)?: "))
            if find != "i2":
                i2 = float(input("What is current 2 (A)?: "))
            if find != "l":
                l = float(input("What is the length of the wires (m)?: "))
            if find != "r":
                r = float(input("What is the separation (m)?: "))
            if find == "f":
                f = mu0 * i1 * i2 * l / (2 * math.pi * r)
                print(f"The force is {f:.6e} N")
            elif find == "i1":
                i1 = f * 2 * math.pi * r / (mu0 * i2 * l)
                print(f"Current 1 is {i1:.4f} A")
            elif find == "i2":
                i2 = f * 2 * math.pi * r / (mu0 * i1 * l)
                print(f"Current 2 is {i2:.4f} A")
            elif find == "l":
                l = f * 2 * math.pi * r / (mu0 * i1 * i2)
                print(f"The length is {l:.4f} m")
            elif find == "r":
                r = mu0 * i1 * i2 * l / (2 * math.pi * f)
                print(f"The separation is {r:.6f} m")
 
        elif eqn == "radius":
            find = input("Do you want to find the radius(r), mass(m), velocity(v), charge(q) or field(b)?: ").lower()
            if find != "r":
                r = float(input("What is the radius of the path (m)?: "))
            if find != "m":
                m = float(input("What is the mass (kg)?: "))
            if find != "v":
                v = float(input("What is the velocity (m/s)?: "))
            if find != "q":
                q = float(input("What is the charge (C)?: "))
            if find != "b":
                b = float(input("What is the magnetic field (T)?: "))
            if find == "r":
                r = m * v / (q * b)
                print(f"The radius is {r:.6e} m")
            elif find == "m":
                m = r * q * b / v
                print(f"The mass is {m:.6e} kg")
            elif find == "v":
                v = r * q * b / m
                print(f"The velocity is {v:.4e} m/s")
            elif find == "q":
                q = m * v / (r * b)
                print(f"The charge is {q:.6e} C")
            elif find == "b":
                b = m * v / (r * q)
                print(f"The magnetic field is {b:.6e} T")
 
        elif eqn == "dipole":
            find = input("Do you want to find the dipole moment(d), turns(n), current(i) or area(a)?: ").lower()
            if find != "d":
                dip = float(input("What is the magnetic dipole moment (A·m^2)?: "))
            if find != "n":
                n = float(input("What is the number of turns?: "))
            if find != "i":
                i = float(input("What is the current (A)?: "))
            if find != "a":
                a = float(input("What is the area (m^2)?: "))
            if find == "d":
                dip = n * i * a
                print(f"The dipole moment is {dip:.6e} A·m^2")
            elif find == "n":
                n = dip / (i * a)
                print(f"The number of turns is {n:.2f}")
            elif find == "i":
                i = dip / (n * a)
                print(f"The current is {i:.4f} A")
            elif find == "a":
                a = dip / (n * i)
                print(f"The area is {a:.6e} m^2")
 
        elif eqn == "selector":
            find = input("Do you want to find the selected velocity(v), electric field(e) or magnetic field(b)?: ").lower()
            if find == "v":
                e = float(input("What is the electric field (V/m)?: "))
                b = float(input("What is the magnetic field (T)?: "))
                print(f"The selected velocity is {e / b:.4e} m/s")
            elif find == "e":
                v = float(input("What is the velocity (m/s)?: "))
                b = float(input("What is the magnetic field (T)?: "))
                print(f"The electric field is {v * b:.4e} V/m")
            elif find == "b":
                e = float(input("What is the electric field (V/m)?: "))
                v = float(input("What is the velocity (m/s)?: "))
                print(f"The magnetic field is {e / v:.6e} T")
 
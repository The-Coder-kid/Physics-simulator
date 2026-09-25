import math
pi = 3.142
g = 9.81

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
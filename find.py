import math
pi = 3.142
g = 9.81
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
        
                elif p == "v" :
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
                        i = math.radians(i)
                        θ = math.asin(i)
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
            C = input("Do you want to find the Horizontal velocity(h) or the Vertical velocity(v)?: ").lower()            
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
                    a = math.radians(a)
                    θ = math.acos(a)
            elif c == "v":
                p = input("Do you want to find the initial velocity(v), the angle(a) or the time(t)").lower()
                if p == "v":
                    vy = float(input("What is the vertical velocity?: "))
                    t = float("What is the time take?: ")
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
                    θ = math.sin(θ)
                    n = vo * θ - vy
                    t = n / g
                elif p == "a":
                    vy = float(input("What is the vertical velocity?: "))
                    vo = float(input("What is the initial velocity?: "))
                    t = float("What is the time take?: ")
                    n = vy * g * t
                    th = math.radians(n / vo)
                    θ = math.sin(th)
        elif eqn == "mh":
            p = input("Do you want to find the initial velocity(v) or the angle(a)").lower()
            if p == "v":
                h = float(input("What is the maximum height?: "))
                vo = float(input("What is the initial velocity?: "))
                θ = float(input("What is the angle?: "))
                θ = math.radians(θ)
                n = 2 * g * h
                θ = math.sin(θ) ** 2
                v = math.sqrt(n / θ)
            elif p == "a":
                n = 2 * g * h
                v = v ** 2
                f = math.sqrt(n / v)
                f = math.radians(f)
                θ = math.asin(f)
                
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
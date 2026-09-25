import math
from find import pendulumf, projectilef
escape = ["quit", "q"]
Practicals = ["pendulum", "projectile", "m", "find"]
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
    

while True:
    Choice = input("What practical do you want to do?: ").lower()

    if Choice in escape:
        quit()

    if Choice in Practicals:
        if Choice == "pendulum":            
            length = float(input("What is the length of the rope?: "))  # Use float for length
            unit_l = input("What unit is being used to measure the length?: ")
            
            if unit_l == "cm":
                length = length / 100  # Convert cm to meters
                unit_l = "m"
                pendulum(length, unit_l)
            elif unit_l == "m": 
                pendulum(length, unit_l)

        elif Choice == "projectile":
            while True:
                try:
                    v = float(input("What is the initial velocity of the projectile in meters per second (m/s)? "))
                    break
                except:
                    ValueError
                    print("Value must be a number")
                    continue
            while True:
                try:
                    θ = float(input("What is the angle of projection with respect to the horizontal in degrees? "))
                    break
                except:
                    ValueError
                    print("Value must be a number")
                    continue
            while True:
                try:
                    t = float(input("How many seconds did the projectile take to complete its flight? "))
                    break
                except:
                    ValueError
                    print("Value must be a number")
                    continue
            projectile(v, θ, t)
        elif Choice == "find":
            aspect = input("Under what aspect are you trying to solve on?: ")
            if aspect not in ["pendulum", "projectile"]:
                print("Pick an aspect in the current list of practicals")
                continue
            elif aspect in ["pendulum", "projectile"]:
                if aspect == "pendulum":
                    pendulumf()
                elif aspect == "projectile":
                    projectilef()
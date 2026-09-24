import math

# Constants
pi = 3.142
g = 9.81

# Function to calculate the period of a pendulum
def pendulum_period(length):
    sqrt = math.sqrt(length / g)
    period = 2 * pi * sqrt
    return period

# Function to calculate the frequency of a pendulum
def pendulum_frequency(period):
    frequency = 1 / period
    return frequency

# Function to calculate the maximum height of a projectile
def projectile_max_height(v, θ):
    θ = math.radians(θ)
    h = (v ** 2 * math.sin(θ) ** 2) / (2 * g)
    return h

# Function to calculate the time of flight of a projectile
def projectile_time_of_flight(v, θ):
    θ = math.radians(θ)
    t = (2 * v * math.sin(θ)) / g
    return t

# Function to calculate the range of a projectile
def projectile_range(v, θ):
    θ = math.radians(θ)
    r = (v ** 2 * math.sin(2 * θ)) / g
    return r

# Function to calculate the equation of the trajectory of a projectile
def projectile_trajectory(x, v, θ):
    θ = math.radians(θ)
    y = (math.tan(θ) * x) - ((g * x ** 2) / (2 * v ** 2 * math.cos(θ) ** 2))
    return y

# Function to handle pendulum calculations
def pendulumf():
    length = float(input("What is the length of the rope?: "))  # Use float for length
    unit_l = input("What unit is being used to measure the length?: ")
    
    if unit_l == "cm":
        length = length / 100  # Convert cm to meters
        unit_l = "m"
    period = pendulum_period(length)
    frequency = pendulum_frequency(period)
    print(f"The period of the pendulum is: {period:.2f} seconds")
    print(f"The frequency of the pendulum is: {frequency:.2f} Hz")

# Function to handle projectile calculations
def projectilef():
    while True:
        try:
            v = float(input("What is the initial velocity of the projectile in meters per second (m/s)? "))
            break
        except ValueError:
            print("Value must be a number")
            continue
    while True:
        try:
            θ = float(input("What is the angle of projection with respect to the horizontal in degrees? "))
            break
        except ValueError:
            print("Value must be a number")
            continue
    while True:
        try:
            t = float(input("How many seconds did the projectile take to complete its flight? "))
            break
        except ValueError:
            print("Value must be a number")
            continue
    
    mh = projectile_max_height(v, θ)
    t = projectile_time_of_flight(v, θ)
    r = projectile_range(v, θ)
    print(f"The maximum height of the projectile is: {mh:.2f} meters")
    print(f"The time of flight of the projectile is: {t:.2f} seconds")
    print(f"The range of the projectile is: {r:.2f} meters")

# Main loop
escape = ["quit", "q"]
Practicals = ["pendulum", "projectile", "m", "find"]

while True:
    Choice = input("What practical do you want to do?: ").lower()

    if Choice in escape:
        quit()

    if Choice in Practicals:
        if Choice == "pendulum":
            pendulumf()
        elif Choice == "projectile":
            projectilef()
        elif Choice == "m":
            pass  # Placeholder for additional calculations
        elif Choice == "find":
            aspect = input("Under what aspect are you trying to solve on?: ")
            if aspect not in ["pendulum", "projectile"]:
                print("Pick an aspect in the current list of practicals")
                continue
            elif aspect == "pendulum":
                pendulumf()
            elif aspect == "projectile":
                projectilef()

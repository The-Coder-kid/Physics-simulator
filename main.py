import math
from find import pendulumf, projectilef
from functions import *
escape = ["quit", "q"]
Practicals = ["pendulum", "projectile", "circuit", "m", "find"]
Total_practicals = len(Practicals)
pi = 3.142
g = 9.81    

while True:
    print("Welcome to the Physics practicals simulator")
    print("The following are the practicals available in this program:", end=" ")

    for index, practical in enumerate(Practicals):
        if index == Total_practicals - 1:
            print(practical, end=".")
        else:
            print(practical, end=", ")

    print("\nType 'quit' or 'q' to exit the program")

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
        elif Choice == "circuit":
            circuit()
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
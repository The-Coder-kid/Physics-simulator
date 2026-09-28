import math
from find import (pendulumf, projectilef, circuitf, electromagnetic_inductionf, wave_motion_soundf,
                  thermal_propertiesf, shmf, fluid_dynamicsf, opticsf, electric_currents_magnetic_fieldsf,
                  nuclear_physicsf, quantum_mechanicsf, thermodynamicsf, capacitors_circuitsf,
                  resistors_ohms_lawf, magnetism_magnetic_forcesf)
from functions import *
escape = ["quit", "q"]
Practicals = ["pendulum", "projectile", "circuit", "electromagnetic induction", "wave motion", "thermal properties of matter", 
              "simple harmonic motion", "fluid dynamics", "optics", "electric currents and magnetic fields", "nuclear physics", 
              "quantum mechanics", "thermodynamics", "capacitors and electric circuits", "resistors and ohm's law", "magnetism and magnetic forces", "m", "find"]
Total_practicals = len(Practicals)
pi = 3.142
g = 9.81    

while True:
    print("Welcome to the Physics practicals simulator")
    print("The following are the practicals available in this program: ")
    for item in Practicals:
        print(f" - {item}")
    print("Type 'quit' or 'q' to exit the program")
    Choice = input("What practical do you want to do?: ").lower()
    if Choice in escape:
        quit()


    for index, practical in enumerate(Practicals):
        if index == Total_practicals - 1:
            print(practical, end=".")
        else:
            print(practical, end=", ")

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
        elif Choice == "electromagnetic induction":
            electromagnetic_induction()
        elif Choice == "wave motion":
            wave_motion_sound()
        elif Choice == "thermal properties of matter":
            thermal_properties()
        elif Choice == "simple harmonic motion":
            shm()
        elif Choice == "fluid dynamics":
            fluid_dynamics()
        elif Choice == "optics":
            optics()
        elif Choice == "electric currents and magnetic fields":
            electric_currents_magnetic_fields()
        elif Choice == "nuclear physics":
            nuclear_physics()
        elif Choice == "quantum mechanics":
            quantum_mechanics()
        elif Choice == "thermodynamics":
            thermodynamics()
        elif Choice == "capacitors and electric circuits":
            capacitors_circuits()
        elif Choice == "resistors and ohm's law":
            resistors_ohms_law()
        elif Choice == "magnetism and magnetic forces":
            magnetism_magnetic_forces()
        elif Choice == "find":
            aspect = input("Under what aspect are you trying to solve on?: ").lower()
            if aspect not in Practicals or aspect in ["m", "find"]:
                print("Pick an aspect in the current list of practicals")
                continue
            elif aspect == "pendulum":
                pendulumf()
            elif aspect == "projectile":
                projectilef()
            elif aspect == "circuit":
                circuitf()
            elif aspect == "electromagnetic induction":
                electromagnetic_inductionf()
            elif aspect == "wave motion":
                wave_motion_soundf()
            elif aspect == "thermal properties of matter":
                thermal_propertiesf()
            elif aspect == "simple harmonic motion":
                shmf()
            elif aspect == "fluid dynamics":
                fluid_dynamicsf()
            elif aspect == "optics":
                opticsf()
            elif aspect == "electric currents and magnetic fields":
                electric_currents_magnetic_fieldsf()
            elif aspect == "nuclear physics":
                nuclear_physicsf()
            elif aspect == "quantum mechanics":
                quantum_mechanicsf()
            elif aspect == "thermodynamics":
                thermodynamicsf()
            elif aspect == "capacitors and electric circuits":
                capacitors_circuitsf()
            elif aspect == "resistors and ohm's law":
                resistors_ohms_lawf()
            elif aspect == "magnetism and magnetic forces":
                magnetism_magnetic_forcesf()
#Question 5

def main():
    mass = float(input("Enter the mass of the object: "))
    velocity = float(input("Enter the velocity of the object: "))

    KE = kinetic_energy(mass,velocity)
    print("\nThe Kinetic Energy of the object is:", KE, "Joules.")

def kinetic_energy(mass, velocity):
    KE = (1/2) * mass * (velocity**2)
    return KE


main()

#input from user
m = float(input("Enter mass in kilograms: "))

#constant value for the speed of light in m/s
C = 299792458

#Calculating energy using Einstein's equation
energy = m * C ** 2

#Displaying the result
print(f"The energy equivalent to {m} kg of mass is {energy} joules.")
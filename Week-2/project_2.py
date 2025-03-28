import numpy as np

print("Choose the type of equation to solve:")
print("1. Quadratic (ax^2 + bx + c = 0)")
print("2. Cubic (ax^3 + bx^2 + cx + d = 0)")
print("3. Quartic (ax^4 + bx^3 + cx^2 + dx + e = 0)")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    # Quadratic Equation Solver
    a = float(input("Enter coefficient a for quadratic equation: "))
    b = float(input("Enter coefficient b for quadratic equation: "))
    c = float(input("Enter coefficient c for quadratic equation: "))

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        print("Two real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("One real root:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = np.sqrt(-discriminant) / (2*a)
        print(f"Complex roots: {real_part} ± {imaginary_part}i")

elif choice == "2":
    # Cubic Equation Solver
    a = float(input("Enter coefficient a for cubic equation: "))
    b = float(input("Enter coefficient b for cubic equation: "))
    c = float(input("Enter coefficient c for cubic equation: "))
    d = float(input("Enter coefficient d for cubic equation: "))

    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)  

    print("Roots of the cubic equation:")
    for root in roots:
        print(root)

elif choice == "3":
    # Quartic Equation Solver
    a = float(input("Enter coefficient a for quartic equation: "))
    b = float(input("Enter coefficient b for quartic equation: "))
    c = float(input("Enter coefficient c for quartic equation: "))
    d = float(input("Enter coefficient d for quartic equation: "))
    e = float(input("Enter coefficient e for quartic equation: "))

    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)  

    print("Roots of the quartic equation:")
    for root in roots:
        print(root)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
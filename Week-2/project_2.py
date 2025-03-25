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
        root1 = (-b + (discriminant) ** 0.5) / (2*a)
        root2 = (-b - (discriminant) ** 0.5) / (2*a)
        print("Two real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("One real root:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = ((-discriminant) ** 0.5) / (2*a)
        print("Complex roots:", real_part, "+/-", imaginary_part, "i")

elif choice == "2":
    # Cubic Equation Solver
    a = float(input("Enter coefficient a for cubic equation: "))
    b = float(input("Enter coefficient b for cubic equation: "))
    c = float(input("Enter coefficient c for cubic equation: "))
    d = float(input("Enter coefficient d for cubic equation: "))
    
    def cubic_solver(a, b, c, d):
        for x in range(-100, 101):  # Checking integer roots
            if a*x**3 + b*x**2 + c*x + d == 0:
                print("One real root of the cubic equation:", x)
                return
        print("No simple integer root found.")
    
    cubic_solver(a, b, c, d)

elif choice == "3":
    # Quartic Equation Solver
    a = float(input("Enter coefficient a for quartic equation: "))
    b = float(input("Enter coefficient b for quartic equation: "))
    c = float(input("Enter coefficient c for quartic equation: "))
    d = float(input("Enter coefficient d for quartic equation: "))
    e = float(input("Enter coefficient e for quartic equation: "))
    
    def quartic_solver(a, b, c, d, e):
        for x in range(-100, 101):  # Checking integer roots
            if a*x**4 + b*x**3 + c*x**2 + d*x + e == 0:
                print("One real root of the quartic equation:", x)
                return
        print("No simple integer root found.")
    
    quartic_solver(a, b, c, d, e)

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
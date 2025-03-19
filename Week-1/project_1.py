def simple_interest(P, R, T):
    return (P * R * T) / 100

def compound_interest(P, R, T):
    return P * (1 + R / 100) ** T - P

def annuity_plan(P, R, T, N):
    r = (R / 100) / N  
    n = T * N  
    return P * ((1 + r) ** n - 1) / r

print("\nChoose a calculation:")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. Annuity Plan")
choice = input("Enter your choice (1/2/3): ")

if choice in ["1", "2", "3"]:
    P = float(input("Enter Principal/Payment amount: "))
    R = float(input("Enter Rate of Interest (% per year): "))
    T = float(input("Enter Time (in years): "))

    if choice == "1":
        SI = simple_interest(P, R, T)
        print(f"Simple Interest: {SI:.2f}")
        print(f"Total Amount: {P + SI:.2f}")

    elif choice == "2":
        CI = compound_interest(P, R, T)
        print(f"Compound Interest: {CI:.2f}")
        print(f"Total Amount: {P + CI:.2f}")

    elif choice == "3":
        N = int(input("Enter number of payments per year (e.g., 12 for monthly): "))
        FV = annuity_plan(P, R, T, N)
        print(f"Future Value of the Annuity: {FV:.2f}")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
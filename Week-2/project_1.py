def swap_ages(name1, age1, name2, age2):
    print(f"Before Swap: {name1} - {age1} years, {name2} - {age2} years")
    
    # Swapping ages
    age1, age2 = age2, age1  
    
    print(f"After Swap: {name1} - {age1} years, {name2} - {age2} years")


swap_ages("chinemerem", 22, "jason", 18)
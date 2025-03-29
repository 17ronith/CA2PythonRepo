def find_cube_pairs(target):
    solutions = []  # Removed semicolon after list initialization
    max_num = round(target ** (1/3))  # Fixed incorrect exponentiation syntax

    for a in range(1, max_num + 1):  # Fixed 'ranges' to 'range'
        for b in range(a, max_num + 1):  # Ensured b ≥ a to avoid duplicates
            if a**3 + b**3 == target:  # Fixed '***' to '**' for correct exponentiation
                solutions.append((a, b))  # Fixed incorrect list name 'sol' to 'solutions'

    return solutions  # Ensured function correctly returns results

pairs = find_cube_pairs(1729)  # Removed trailing comma to prevent tuple assignment

print("Valid cube pairs for 1729:")  # Fixed 'printf' to 'print'

for a, b in pairs:  # Fixed incorrect loop variable 'pair' to 'pairs'
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Fixed exponentiation in output

#all errors have been fixed

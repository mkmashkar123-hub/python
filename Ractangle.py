# Pyramid Triangle
rows = 5
for i in range(1, rows + 1):
    # Print spaces first, then stars
    print(" " * (rows - i) + "*" * (2 * i - 1))
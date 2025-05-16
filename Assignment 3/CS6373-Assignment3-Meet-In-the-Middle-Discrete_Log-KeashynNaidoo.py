import gmpy2

def read_multiline_input(prompt):
    """Read multi-line input until an empty line is entered."""
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        try:
            # Attempt to convert the input line to an integer
            lines.append(int(line.strip()))
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return int("".join(map(str, lines))) if lines else None  # Join all lines and convert to integer

def save_results(p, g, h, x, filename):
    """Save the results to a text file."""
    try:
        with open(filename, 'w') as f:
            f.write("Results:\n")
            f.write(f"Given values:\n")
            f.write(f"p = {p}\n")
            f.write(f"g = {g}\n")
            f.write(f"h = {h}\n")
            f.write(f"Computed value of x: {x}\n")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def is_prime(n):
    """Check if a number is prime using gmpy2 for efficiency."""
    return gmpy2.is_prime(n)

def main():
    # Step 1: Input values from the user
    p = read_multiline_input("Enter the prime number (p) (press Enter on a new line to finish):")
    if p is None or not is_prime(p):
        print(f"The number {p} is not a prime number.")
        return

    print("Proceeding to input base/generator (g)...")
    g = read_multiline_input("Enter the base / generator (g) (press Enter on a new line to finish): ")
    if g is None or g <= 1 or g >= p:
        print(f"The base g must be greater than 1 and less than p ({p}).")
        return

    print("Proceeding to input target value (h)...")
    h = read_multiline_input("Enter the target value (h) (press Enter on a new line to finish): ")
    if h is None or h < 0 or h >= p:
        print(f"The target value must be a non-negative integer less than p ({p}).")
        return

    B = 2 ** 20  # 1048576

    # Step 2: Precompute g^B mod p
    gB = gmpy2.powmod(g, B, p)

    # Step 3: Build the hash table for h / g^x1
    hash_table = {}
    for x1 in range(B):
        g_x1 = gmpy2.powmod(g, x1, p)
        try:
            h_div_gx1 = gmpy2.f_mod(h * gmpy2.invert(g_x1, p), p)
            hash_table[h_div_gx1] = x1
        except ZeroDivisionError:
            print(f"Division by zero encountered on x1 = {x1}. Skipping this value.")
            continue
        except ValueError:
            print(f"Invalid operation for x1 = {x1}. Skipping this value.")
            continue

    # Step 4: Check for each x0 if (g^B)^x0 is in the hash table
    for x0 in range(B):
        gB_x0 = gmpy2.powmod(gB, x0, p)
        if gB_x0 in hash_table:
            x1 = hash_table[gB_x0]
            x = x0 * B + x1

            # Step 5: Save the results to a file
            save_results(p, g, h, x, 'MiTM_discretelog.txt')
            print(f"Prime number p: {p}")
            print(f"Base g: {g}")
            print(f"Target h: {h}")
            print(f"Computed value of x: {x}")
            break
    else:
        print("No solution found.")
        # Save the no solution message to the results file
        save_results(p, g, h, "No solution found", 'MiTM_discretelog .txt')

if __name__ == "__main__":
    main()
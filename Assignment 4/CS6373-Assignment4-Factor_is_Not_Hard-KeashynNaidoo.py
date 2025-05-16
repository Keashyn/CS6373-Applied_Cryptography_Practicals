import gmpy2

def factor_rsa(N):
    # Calculate the integer square root of N (floor)
    sqrt_N = gmpy2.isqrt(N)

    # Compute A as ceiling of the sqrt of N
    if sqrt_N * sqrt_N == N:
        A = sqrt_N
    else:
        A = sqrt_N + 1

    # Calculate x = sqrt(A^2 - N)
    x = gmpy2.isqrt(A * A - N)

    # Calculate factors p and q
    p = A - x
    q = A + x

    return p, q

def main():
    try:
        # Prompt the user to enter the modulus N on separate lines
        print("Enter the RSA modulus N (press Enter on a new line when done):")
        input_lines = []

        while True:
            line = input()
            if line.strip() == "":  # Break on empty line
                break
            input_lines.append(line.strip())

        # Join the input lines to form the complete number
        input_str = ''.join(input_lines)

        # Convert input to multi-precision integer
        N = gmpy2.mpz(input_str)

        # Factor N
        p, q = factor_rsa(N)

        # Output the results
        print("N:", N)
        print("p:", p)
        print("q:", q)
        verification = p * q == N
        print("Verification: p * q == N ->", verification)

        # Save results to a text file
        with open("factorization_results.txt", "w") as f:
            f.write(f" Given N: {N}\n")
            f.write(f"p: {p}\n")
            f.write(f"q: {q}\n")
            f.write(f"Verification: p * q == N -> {verification}\n")

        print("Results saved to factorization_results.txt")

    except Exception as e:
        print("Error:", e)
        print("Please enter a valid integer modulus.")

if __name__ == "__main__":
    main()

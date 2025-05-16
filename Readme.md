# Cryptography Analysis Assignments – Python Implementations

This repository contains Python-based solutions for four cryptographic analysis assignments developed as part of the **CS6373 - Applied Cryptography** course at the **University of Texas at San Antonio (UTSA)**.

---

## 📁 Assignments Overview

---

### 1. XOR-Based Vigenère Cipher

#### 🔍 Objective:
Crack a ciphertext encrypted using a Vigenère-like cipher where **XOR** is used instead of modular addition. The key length is between 1 and 13, and the same key bytes repeat cyclically.

#### 🛠️ Task:
- Analyze the ciphertext.
- Determine the probable key length.
- Recover the key using statistical methods (e.g., frequency analysis).
- Decrypt the ciphertext to retrieve the original message.

#### 🔓 Deliverables:
- Recovered key.
- Decrypted plaintext.
- Python code for analysis and decryption.

---

### 2. One-Time Pad with Reused Key

#### 🔍 Objective:
Decrypt 7 ciphertexts of equal length (31 bytes), all encrypted with the **same one-time pad key**—a critical cryptographic flaw.

#### 🛠️ Task:
- Exploit the OTP key reuse using techniques such as crib-dragging and XORing ciphertexts.
- Recover the 7 plaintext messages.
- Provide insights into the decryption methodology and heuristics used.

#### 🔓 Deliverables:
- All 7 decrypted plaintexts.
- Description of the attack methodology.
- Python code implementing the attack.

---

### 3. Discrete Log via Meet-in-the-Middle

#### 🔍 Objective:
Efficiently compute _x_ in the equation:  
\[
h = g^x \mod p
\]  
where \(1 < x < 2^{40}\), using a **meet-in-the-middle** strategy to reduce the brute-force complexity.

#### 🛠️ Task:
- Implement the meet-in-the-middle attack to split the search space and reduce operations.
- Efficiently compute the discrete logarithm without testing all possible 2⁴⁰ values.

#### 🔓 Deliverables:
- Python implementation file.
- Algorithm description explaining the approach.
- Results file showing values of \( p \), \( g \), \( h \), and computed \( x \).

---

### 4. Factor is Not Hard

#### 🔍 Objective:
Demonstrate a vulnerability in RSA when the prime factors \( p \) and \( q \) are close. Use **Fermat’s factorization** to recover the original primes from a given RSA modulus \( N \).

#### 🛠️ Task:
- Implement Fermat’s factorization using Python and the `gmpy2` library.
- Read \( N \) as multi-line input.
- Use the identity:
  \[
  N = A^2 - x^2 \Rightarrow p = A - x, \quad q = A + x
  \]  
  where \( A = \lceil \sqrt{N} \rceil \), and \( x = \sqrt{A^2 - N} \).
- Verify correctness by ensuring \( p \times q = N \).
- Output results to the console and save them in `factorization_results.txt`.

#### 🔓 Deliverables:
- Python implementation script.
- Recovered prime factors \( p \) and \( q \).
- A brief explanation document on the method, its effectiveness, and real-world implications for RSA key generation.

---

## 🧰 Technologies Used
- Python 3.7.7
- Standard libraries only (except `gmpy2` for Assignment 3 and 4)

---

## 📂 Folder Structure (Recommended)
- Assignment 1 - XOR-Based Vigenère Cipher 
- Assignment 2 - One-Time Pad 
- Assignment 3 - Meet-in-the-Middle Discrete Log 
- Assignment 4 - Factor is Not Hard

---

## 📌 Notes
- All ciphertexts are hex-encoded.
- Plaintexts contain standard English characters (letters, punctuation, and spaces), but no digits.
- Newline characters were excluded during encryption for simplicity.

---

## ⚠️ Important Notice

This repository is intended for **educational purposes only**. The Python code provided should not be reused for future assignments or copied by other students. Unauthorized use may violate academic integrity policies. Always ensure your work is original and refer to course materials for guidance.

---

## 👤 Author

**Keashyn Naidoo**  
CS6373 - Applied Cryptography  
University of Texas at San Antonio (UTSA)

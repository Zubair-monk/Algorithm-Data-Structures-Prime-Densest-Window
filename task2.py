def prime_finding(n):
    """Checking if the number is prime or not"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def densest_prime_window(s, w, n):
    #check if it is numeric or not
    if not s.isdigit():
        return "0, 0: Invalid input"

    best_index = 0
    max_count = -1
    best_primes = []

    # 2. Sliding Window Loop [cite: 35]
    for start in range(len(s) - w + 1):
        window = s[start: start + w]
        unique_primes = []  # creating empty list for storing prime numbers


        # 3. Substring Extraction [cite: 36]
        for i in range(len(window)):
            for j in range(i + 1, len(window) + 1):
                value = int(window[i:j])

                # Check limit and primality
                if value < n and prime_finding(value):
                    if value not in unique_primes:
                        unique_primes.append(value) #insert the prime number in the list


        current_count = len(unique_primes)
        if current_count > max_count:
            max_count = current_count
            best_index = start
            best_primes = sorted(unique_primes)
        elif current_count == max_count and max_count > 0:

            pass

    if max_count <= 0:
        return "0, 0: No primes found"


    if len(best_primes) >= 6:
        primes_str = f"{best_primes[0]}, {best_primes[1]}, {best_primes[2]}, ..., " \
                     f"{best_primes[-3]}, {best_primes[-2]}, {best_primes[-1]}"
    else:
        primes_str = ", ".join(map(str, best_primes))

    return f"{best_index}, {max_count}: {primes_str}"

# --- Execution for Test Cases ---
# Case 1: 3141592653, 2, 50 [cite: 49]
print(densest_prime_window("3141592653", 2, 50))
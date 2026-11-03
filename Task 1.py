import math


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    limit = int(math.isqrt(x))
    for d in range(2, limit + 1):
        if x % d == 0:
            return False
    return True


def find_prime_densest_window(s: str, w: int, n: int) -> None:
    # Input validation
    if not s.isdigit() or w <= 0 or w > len(s) or n <= 0:
        print("0, 0: Invalid input")
        return

    best_index = 0
    best_primes = set()
    best_count = 0

    # Slide window
    for start in range(0, len(s) - w + 1):
        window = s[start:start + w]
        window_primes = set()

        # All substrings in this window
        for i in range(len(window)):
            for j in range(i + 1, len(window) + 1):
                sub = window[i:j]
                num = int(sub)  # leading zeros are fine, int("013") -> 13
                if num < n and is_prime(num):
                    window_primes.add(num)

        count = len(window_primes)

        # Update best window
        if count > best_count:
            best_count = count
            best_index = start
            best_primes = window_primes.copy()
        elif count == best_count and count > 0:
            if start < best_index:
                best_index = start
                best_primes = window_primes.copy()

    # No primes at all
    if best_count == 0:
        print("0, 0: No primes found")
        return

    # Prepare output
    primes_sorted = sorted(best_primes)
    if len(primes_sorted) >= 6:
        display = primes_sorted[:3] + primes_sorted[-3:]
    else:
        display = primes_sorted

    # Format: index, count: primes
    primes_str = ", ".join(str(p) for p in display)
    print(f"{best_index}, {best_count}: {primes_str}")


# --- Example runs (you can change these) ---

# Sample from spec:
find_prime_densest_window("12319", 3, 50)      # expected: 1, 4: 2, 3, 23, 31

# No primes example:
find_prime_densest_window("44488", 3, 500)     # expected: 0, 0: No primes found

# Invalid input example:
find_prime_densest_window("COMP", 4, 100)      # expected: 0, 0: Invalid input

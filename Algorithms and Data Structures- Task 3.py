def is_prime(num):
    """Return
    True if num is prime, otherwise False."""

    if num < 2:
    return False


if num == 2:
  return True

if num % 2 == 0:
  return False

Limit = int(num ** 0.5) + 1

For i in range(3, limit, 2):

if num % i == 0:
   return False

Return
True

Def
prime_dense_window_set(s, w, n):

“ “ “Find
the
prime - densest
window
using
sets.” ” ”



# Input validation

If
not s.isdigit() or w <= 0 or w > len(s) or n <= 0:

Return “0, 0: Invalid
input”





best_index = 0

best_count = 0

Best_prime = set()

# Slide window across string

For
start in range(len(s) - w + 1):

window = s[start:start + w]
window_primes = set()

# Generate all substrings inside current window

For
i in range(len(window)):

For
j in range(i + 1, len(window) + 1):

Value = int(window[i:j])

If
value < n and is_prime(value):

Window_primes.add(value)

current_count = len(window_primes)

# Updates best window

If
current_count > best_count:
best_count = current_count

Best_index = start
best_primes = window_primes.copy()

If
best_count == 0:
return “0, 0: No
primes
found”



Sorted_primes = sorted(best_primes)

If
lens(sorted_primes) >= 6:

primes_str = (

    F"{sorted_primes[0]}, {sorted_primes[1]}, {sorted_primes[2]},” 

    F"...,” 

    F"{sorted_primes[-3]}, {sorted_primes[-2]}, {sorted_primes[-1]},”

)

Else:

primes_str = “, ”.join(map(str, sorted_primes))

Return
f” {best_index}, {best_count}: {primes_str}”



# --- Execution for Test Cases ---

print(densest_prime_window("3141592653", 2, 50))
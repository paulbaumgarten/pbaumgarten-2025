# Lesson 09 Challenge Solutions
# For Loops

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Multiplication table
n = 7
print(f"{n}× multiplication table:")
for i in range(1, 13):
    product = n * i
    print(f"  {n} × {i:2d} = {product:3d}")
    # LED gets greener the higher the product
    brightness = min(product, 80)
    np[0] = (0, brightness // 2, brightness // 4)
    np.write()
    time.sleep(0.2)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: FizzBuzz with LED
print("\nFizzBuzz 1–30:")
for i in range(1, 31):
    if i % 15 == 0:
        word = "FizzBuzz"
        np[0] = (80, 0, 80)   # Purple
    elif i % 3 == 0:
        word = "Fizz"
        np[0] = (80, 0, 0)    # Red
    elif i % 5 == 0:
        word = "Buzz"
        np[0] = (0, 0, 80)    # Blue
    else:
        word = str(i)
        np[0] = (0, 40, 0)    # Dim green
    np.write()
    print(f"  {i:2d}: {word}")
    time.sleep(0.15)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Prime sieve (Sieve of Eratosthenes)
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [n for n in range(2, limit + 1) if is_prime[n]]

primes = sieve_of_eratosthenes(100)
print(f"\nPrimes up to 100 ({len(primes)} found):")
for i, p in enumerate(primes):
    print(f"{p:4d}", end="")
    if (i + 1) % 10 == 0:
        print()
print()

# Sum and average
print(f"Sum of primes up to 100: {sum(primes)}")
print(f"Largest prime ≤ 100: {primes[-1]}")

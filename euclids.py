def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a % b)

# returns (x, y, d) such that ax + by = gcd(a, b)
# if d = 1, then x is the modular inverse of a mod b
def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_euclid(b, a % b)
    print(f"return of child {b, a%b} of parent {a, b} is {x, y, d}")
    print(f"returning {y, x - (a // b) * y, d} to callee")
    return (y, x - (a // b) * y, d)

print(euclid(132, 5*76))
result = extended_euclid(5, 132)
print(f"extended euclid of 5, 132 is {result}")
print(f"inverse of 5 mod 132 is {result[0]}") if result[2] == 1 else print("no inverse")

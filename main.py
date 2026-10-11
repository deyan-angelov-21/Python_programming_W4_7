print("Program starting.")
print()
print("Check multiplicative persistence.")
n = int(input("Insert an integer: "))
n = abs(n)
steps = 0
while len(str(n)) > 1:
    digits = list(str(n))
    product = 1
    for d in digits:
        product *= int(d)
    expression = ".*.".join(digits)
    print(f"{expression}={product}")
    n = product
    steps += 1
print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")

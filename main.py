import sys

print("Program starting.")
print()
print("Check multiplicative persistence.")

if sys.stdin.isatty():
    number = int(input("Insert an integer: "))
else:
    print("Insert an integer: ", end="")
    raw = input()
    print(raw)
    number = int(raw)

steps = 0
while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    print("*".join(str(number)), "=", product)
    number = product
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")

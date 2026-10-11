print("Program starting.")
print()
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))

steps = 0
while number > 9:
    digits = [int(d) for d in str(number)]
    product = 1
    for digit in digits:
        product *= digit

    print("*".join(str(d) for d in digits), "=", product)

    number = product
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")

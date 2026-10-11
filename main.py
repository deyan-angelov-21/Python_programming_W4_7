def main():
    print("Program starting.")
    print("Check multiplicative persistence.")
    
    try:
        user_input = input("Insert an integer: ")
        n = int(user_input)
    except ValueError:
        return

    steps = 0
    current_str = user_input.strip()

    while len(current_str) > 1:
        digits = [int(ch) for ch in current_str]
        
        product = 1
        for d in digits:
            product *= d
            
        expression = " * ".join(str(d) for d in digits)
        print(f"{expression} = {product}")
        
        current_str = str(product)
        steps += 1

    print("No more steps.")
    print(f"This program took {steps} step(s)")
    print("Program ending.")

if __name__ == "__main__":
    main()

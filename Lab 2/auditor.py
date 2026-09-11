def calculate(first_number, operator, second_number):
    """Perform a basic arithmetic calculation."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("Simple Calculator")
    print("Enter 'q' to quit.")

    while True:
        expression = input("Enter a calculation (for example, 5 + 3): ").strip()
        if expression.lower() == "q":
            break

        try:
            first, operator, second = expression.split()
            result = calculate(float(first), operator, float(second))
            print(f"Result: {result:g}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
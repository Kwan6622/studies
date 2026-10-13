#15/07/2026
#A program that acts like a calculator, expression format x y z = ?
#1. Prompts user for an expression
#2. If y is / then z can't be 0 
#3. Output the result as float

def expression(a, b, c):
    a = float(a)
    c = float(c)

    match b:
        case "+":
            return a + c
        case "-":
            return a - c
        case "*":
            return a * c
        case "/":
            if c != 0:
                return a / c
            return "Invalid Expression!"
        case _:
            return "Invalid Expression!"

def main():
    x, y, z = input("Expression: ").split(" ")
    print(expression(x, y, z))

if __name__ == "__main__":
    main()
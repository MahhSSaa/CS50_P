first, operator, second = input("Expression: ").strip().split(" ")
first = float(first)
second = float(second)

match operator:
    case "+":
        print(f"{first + second:.1f}")
    case "-":
        print(f"{first - second:.1f}")
    case "*":
        print(f"{first * second:.1f}")
    case "/":
        print(f"{first / second:.1f}")

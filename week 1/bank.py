answer = input("Greeting: ").lower().strip()

if answer.startswith("hello"):
    print("$0")
elif answer[0] == "h":
    print("$20")
else:
    print("$100")

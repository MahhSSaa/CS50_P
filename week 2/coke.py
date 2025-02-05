price = 50
input_coin = 0

while input_coin < price:
    print(f"Amount Due: {price - input_coin}")
    next_coin = int(input("Next Coin: ").strip())
    coins = [25, 10, 5]
    if next_coin in coins:
        input_coin += next_coin
    else:
        continue

print(f"Change Owed: {input_coin - price}")

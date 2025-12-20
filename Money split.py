n = int(input("Enter the amount of money: "))
coin_types = [500, 100, 10, 5, 1]
def possiblecombinations(amount, coins, index, current_combination):
    if amount == 0:
        print(current_combination)
        return
    if index >= len(coins):
        return
    current_coin = coins[index]
    max_count = amount // current_coin
    for count in range(max_count, -1, -1):
        new_combination = current_combination + [current_coin] * count
        possiblecombinations(amount - (count * current_coin), coins, index + 1, new_combination)
print(f"All possible ways to split {n}:")
possiblecombinations(n, coin_types, 0, [])
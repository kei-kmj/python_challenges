cards = [100, 200, 150, 80, 250, 300]
budget = 500

# 購入可能な最大枚数を求める

def max_cards_purchasable(cards):
    sorted_cards = sorted(cards)
    total_cost = 0
    count = 0

    for price in sorted_cards:
        if total_cost + price > budget:
            break
        total_cost += price
        count += 1

    return count

print(max_cards_purchasable(cards))

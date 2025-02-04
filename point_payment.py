balance, payment_count = (int(x) for x in input().split())
payments = [int(input()) for _ in range(payment_count)]

point = 0

for pay in payments:
    # 料金よりもポイントが多い場合、ポイントを減らす
    # ポイント使用時にはポイントはつかない
    if point >= pay:
        point -= pay
    else:
        # ポイントが足りない場合、残高から支払う
        balance -= pay
        point += pay * 0.1

    print(balance, int(point))

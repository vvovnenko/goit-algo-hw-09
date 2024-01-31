import timeit
from typing import Callable


def benchmark(func: Callable, sum_: int):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(sum_)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'sum_': sum_}, number=10)


coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    return count_coins


def find_min_coins(sum_):
    min_coins_required = [0] + [float("inf")] * sum_
    last_coin_used = [0] * (sum_ + 1)

    for s in range(1, sum_ + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin

    return count_coins


if __name__ == '__main__':
    results = []

    for n in [10, 50, 100, 1000, 1000, 10000, 100000]:
        greedy_time = benchmark(find_coins_greedy, n)
        min_time = benchmark(find_min_coins, n)
        results.append((n, greedy_time, min_time, min_time / greedy_time))

    print('Час виконання алгоритмів в секундах для різних сум:')
    print(f"| {'Сума':<10} | {'Жадібний, сек':<30} | {'Динамічний, сек':<30} |")
    print(f"| :{'-'*9} | :{'-'*29} | :{'-'*29} |")

    for result in results:
        print(f"| {result[0]:<10} | {result[1]:<30} | {result[2]:<30} |")


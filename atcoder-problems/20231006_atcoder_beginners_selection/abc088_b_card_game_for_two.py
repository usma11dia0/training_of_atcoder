def solve(n: int, a_list: list) -> int:
    target_list = [*a_list]
    target_list.sort(reverse=True)
    alice_cards = [target_list[i] for i in range(0, n, 2)]
    bob_cards = [target_list[i] for i in range(1, n, 2)]

    alice_score = sum(alice_cards)
    bob_score = sum(bob_cards)

    return alice_score - bob_score

if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split()))
    print(solve(n, a_list))
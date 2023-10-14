def solve(n: int, d_list: list) -> int:
    target_list = [*d_list]
    target_list.sort(reverse=True)

    kagami_mochi = [10**9]
    while len(target_list):
        max_value = target_list.pop(0)
        diameter_kagami_mochi = kagami_mochi[-1]
        if max_value < diameter_kagami_mochi:
            kagami_mochi.append(max_value)

    return len(kagami_mochi) - 1

if __name__ == '__main__':
    n = int(input())
    d_list = [int(input()) for _ in range(0, n)]
    print(solve(n, d_list))
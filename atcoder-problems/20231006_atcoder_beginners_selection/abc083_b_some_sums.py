def solve(n: int, a: int, b:int) -> int:
    target_list = []
    for t in range(1, n + 1):
        t_str = str(t)
        total_digit = sum_digit(t_str)
        if a <= total_digit and total_digit <= b:
            target_list.append(t_str)
    result = sum(map(int, target_list))    
    
    return result


def sum_digit(target: str):
    total = sum(map(int, target))
    
    return total


if __name__ == '__main__':
    n, a, b = map(int, input().split())
    print(solve(n, a, b))
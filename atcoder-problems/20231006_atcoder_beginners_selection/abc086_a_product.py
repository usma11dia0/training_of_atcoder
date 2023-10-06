def solve(a: int, b: int) -> str:
    product = a * b
    if product % 2:
        return "Odd"
    else:
        return "Even"

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))
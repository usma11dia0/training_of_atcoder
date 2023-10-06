def solve(s: str) -> int:
    cnt = 0
    for s in s_str:
        if s == "1":
            cnt += 1
    return cnt


if __name__ == "__main__":
    s_str = str(input())
    print(solve(s_str))
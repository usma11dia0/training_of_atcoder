def solve(a_list: list) -> int:
    cnt = 0
    while True: 
        if any(x % 2 == 1 or x == 0 for x in a_list):
            return cnt
        a_list = [x / 2 for x in a_list]
        cnt += 1

if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    print(solve(a_list))
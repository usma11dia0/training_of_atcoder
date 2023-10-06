def solve(a: int, b: int, c: int, s: str) -> None:
    print(a + b + c, s)



if __name__ == "__main__":
    a = int(input())
    b, c = map(int, input().split())
    s = str(input())
    
    solve(a, b, c, s)
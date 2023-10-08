def solve(a: int, b: int, c:int, x: int) -> int:
    list_500 = [ 500 * i  for i in range(a + 1)]
    list_100 = [ 100 * i  for i in range(b + 1)]
    list_50 = [ 50 * i  for i in range(c + 1)]
 
    cnt  = 0
    for s in list_500:
        if x < s: continue
        for t in list_100:
            if x < s + t: continue
            for u in list_50:
                if s + t + u == x:
                    cnt += 1
    return cnt

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    
    print(solve(a, b, c, x))
def solve(a_list: list) -> int:
    cnt = 0
    tmp_list = a_list
    while True: 
        for tmp in tmp_list:
            if tmp % 2 == 1 or tmp == 0:
                return cnt
        tmp_list = devide_all_by_2(tmp_list)
        cnt += 1

def devide_all_by_2(target_list: list) -> list:
    result_list = []    
    for target in target_list:
        result_list.append(target / 2)
    return result_list



if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    print(solve(a_list))
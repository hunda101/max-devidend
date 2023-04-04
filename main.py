def main():
    N = int(input ("positive integer: "))
    A = []
    while True:
        a = input("input list: ").split()
        if not a:
            break
        num_list = list(map(int, a))
        A.append(num_list)

    func(A, N)

def func(A, N):
    B = []
    list_num = [sorted(set(lst), reverse=True) for lst in A]
    print(list_num)
    select_index = 1
    for skip_index in range(len(list_num)):
        tmp_dict = {}
        max_index_value = list_num[select_index][0]
        tmp_dict[select_index] = max_index_value
        while True:
            for i, val in enumerate(list_num):
                if i != skip_index and i != select_index:
                    tmp_dict[i] = val[0]
            if sum(tmp_dict.values()) % N == 0:
                dict_sum_list = {}
                for k, v in tmp_dict.items():
                    if len(list_num[k]) > 1:
                        delta = list_num[k][0] - list_num[k][1]
                        if delta == 0:
                            continue
                        dict_sum_list[k] = delta
                print(dict_sum_list)
                min_delta_key = min(dict_sum_list, key=dict_sum_list.get)
                del tmp_dict[min_delta_key]
                list_num[min_delta_key].pop(0)
            else:
                break
        B.append(list(tmp_dict.values()))
        select_index += 1
        if select_index == len(list_num):
            select_index = 0
    sum_B = [sum(x) for x in B]
    print(B)
    print(max(sum_B))
main()
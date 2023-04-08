def main():
    print("The author of this program is Mark Khomenko")
    print("Program calculates maximum sum of elements entered by user, which is not dividable by N,. Variant 18.")
    try:
        N = int(input("positive integer: "))
        if N <= 0:
            raise ValueError("incorrect value: must be positive integer")
        data = []
        while True:
            a = input("input list: ").split()
            if not a:
                break
            num_list = list(map(int, a))
            data.append(num_list)
            max_divisor(data, N)
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except (EOFError, ValueError) as e:
        print("***** error")
        print(repr(e))


def _numbers_combinations(skip_index, select_index, list_num, possible_combinations, N):
    tmp_dict = {}
    max_index_value = list_num[select_index][0]
    tmp_dict[select_index] = max_index_value
    for i, val in enumerate(list_num):
        if i != skip_index and i != select_index:
            tmp_dict[i] = val[0]
    while sum(tmp_dict.values()) % N == 0:
        if _search_min_delta(tmp_dict, list_num) == 0:
            tmp_dict = {}
            break
    possible_combinations.append(tuple((tmp_dict, skip_index, sum(tmp_dict.values()))))


def _search_min_delta(tmp_dict, list_num):
    dict_sum_list = {}
    for k, v in tmp_dict.items():
        if len(list_num[k]) > 1:
            delta = list_num[k][0] - list_num[k][1]
            if delta == 0:
                continue
            dict_sum_list[k] = delta
    if not dict_sum_list:
        return 0
    min_delta_key = min(dict_sum_list, key=dict_sum_list.get)
    tmp_dict[min_delta_key] = list_num[min_delta_key][1]
    list_num[min_delta_key].pop(0)


def max_divisor(data, N):
    possible_combinations = []
    list_num = [sorted(set(lst), reverse=True) for lst in data]
    try:
        select_index = 1
        for skip_index in range(len(list_num)):
            _numbers_combinations(skip_index, select_index, list_num, possible_combinations, N)
            select_index += 1
            if select_index == len(list_num):
                select_index = 0
        max_dict = max(possible_combinations, key=lambda d: sum(d[0].values()))
    except (IndexError, ValueError):
        max_dict = ({None: None}, None, None)
    return_result(max_dict, N, len(list_num))


def return_result(ps, N, length):
    print("THE WORK IS DONE,")
    print(f"For N = {N}")
    print(f"Number of lists: {length}")
    print(f"List from which a number was not selected: {ps[1]}")
    print(f"Max sum that not divisible by {N} is {ps[2]}")
    print("These numbers were selected: ", end="")
    for k, v in ps[0].items():
        print(f"from {k} list number: {v}", end=", ")


main()

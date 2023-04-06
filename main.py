def main():
    N = int(input("positive integer: "))
    data = []
    while True:
        a = input("input list: ").split()
        if not a:
            break
        num_list = list(map(int, a))
        data.append(num_list)

    func(data, N)
def numbers_combinations(skip_index, select_index, list_num, possible_combinations, N):
    tmp_dict = {}
    max_index_value = list_num[select_index][0]
    tmp_dict[select_index] = max_index_value
    for i, val in enumerate(list_num):
        if i != skip_index and i != select_index:
            tmp_dict[i] = val[0]
    while True:
        if sum(tmp_dict.values()) % N == 0:
            if search_min_delta(tmp_dict, list_num) == 0:
                tmp_dict = {}
                break
        else:
            break
    possible_combinations.append(tmp_dict)

def search_min_delta(tmp_dict, list_num):
    dict_sum_list = {}
    for k, v in tmp_dict.items():
        if len(list_num[k]) > 1:
            delta = list_num[k][0] - list_num[k][1]
            if delta == 0:
                continue
            dict_sum_list[k] = delta
    print(dict_sum_list)
    if not dict_sum_list:
        return 0
    min_delta_key = min(dict_sum_list, key=dict_sum_list.get)
    tmp_dict[min_delta_key] = list_num [min_delta_key] [1]
    list_num[min_delta_key].pop(0)


def func(data, N):
    possible_combinations = []
    list_num = [sorted(set(lst), reverse=True) for lst in data]
    if len(list_num) < 2:
         return next(0)
    select_index = 1
    for skip_index in range(len(list_num)):
        numbers_combinations(skip_index, select_index, list_num, possible_combinations, N)
        select_index += 1
        if select_index == len(list_num):
            select_index = 0
    next(possible_combinations)

def next(ps):
    print(ps)
main()

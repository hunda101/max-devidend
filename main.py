def main():
    """
    tells about the program, asks user to input N and lists of numbers
    """
    print("The author of this program is Mark Khomenko")
    print("Program calculates maximum sum of elements entered by user, which is not dividable by N,. Variant 18.")
    try:
        N = int(input("Input positive integer N: "))
        if N <= 0:
            raise ValueError("incorrect value: must be positive integer")
        data = []
        while True:
            a = input("Input numbers of list(input white line to stop): ").split()
            if not a:
                break
            num_list = list(map(int, a))
            data.append(num_list)

    except KeyboardInterrupt:
        print("\nprogram aborted")
    except (EOFError, ValueError) as e:
        print("***** error")
        print(repr(e))
    else:
        max_divisor(data, N)


def _numbers_combinations(skip_index, select_index, list_num, possible_combinations, N):
    """
    find one max combination of numbers from lists except of one
    """
    tmp_dict = {idx: val[0] for idx, val in enumerate(list_num) if idx not in (skip_index, select_index)}
    max_index_value = list_num[select_index][0]
    tmp_dict[select_index] = max_index_value
    is_dividable = False
    delta_index = 0
    print(tmp_dict)
    while sum(tmp_dict.values()) % N == 0:
        if _find_min_delta(tmp_dict, list_num, delta_index) == 0:
            is_dividable = True
            break
        delta_index += 1
    possible_combinations.append(
        ({}, None, None) if is_dividable else (dict(sorted(tmp_dict.items())), skip_index, sum(tmp_dict.values()))
    )


def _find_min_delta(tmp_dict, list_num_copy, index):
    """
    finds the best solution to choose number to get maximum sum that is not divided by N
    """
    dict_sum_list = {}
    for k, v in tmp_dict.items():
        if len(list_num_copy[k]) > index + 1:
            delta = list_num_copy[k][index] - list_num_copy[k][index + 1]
            dict_sum_list[k] = delta
    if not dict_sum_list:
        return 0
    min_delta_key = min(dict_sum_list, key=dict_sum_list.get)
    tmp_dict[min_delta_key] = list_num_copy[min_delta_key][index+1]


def max_divisor(data, N):
    """
    finds all max combinations from lists except of one list and passes combination with maximum sum
    """
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
    except ValueError:
        max_dict = ({}, None, None)
    except IndexError:
        max_dict = ({}, 0, None)
    return_result(max_dict, N, len(list_num))


def _print_numbers(pc):
    for k, v in pc.items():
        print(f"list: {k}, number: {v}", end="; ")


def return_result(ps, N, amount):
    print("THE WORK IS DONE, ")
    print(f"For N = {N}, ")
    print(f"Amount of lists: {amount}, ")
    print(f"List from which a number was not selected: {ps[1]},")
    print(f"Max sum that is not divisible by {N} is {ps[2]}")
    print("These numbers were selected: ", end="")
    _print_numbers(ps[0])


main()

def main():
    """
    tells about the program, asks user to input N and lists of numbers
    """
    print("The author of this program is Mark Khomenko")
    print("Program calculates maximum sum of elements entered by user, which is not divisible by N. Variant 18.")
    try:
        N = int(input("Input positive integer N: "))
        if N <= 0:
            raise ValueError("incorrect value: must be positive integer")
        data = []
        while lst := input("Input list of numbers(input white line to stop): ").split():
            num_list = list(map(int, lst))
            data.append(num_list)
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except (EOFError, ValueError) as e:
        print("***** error")
        print(repr(e))
    else:
        max_divisor(data, N)


def max_divisor(data, N):
    """
    finds all max combinations from lists except of one list and passes combination with maximum sum of numbers
    """
    possible_combinations = []
    for lst in data:
        lst.sort(reverse=True)
    try:
        if len(data) == 1:
            raise IndexError
        for skip_idx in range(len(data)):
            _numbers_combinations(skip_idx, data, possible_combinations, N)
        max_combination = max(possible_combinations, key=lambda mx: sum(mx[0].values()))
    except ValueError:
        max_combination = ({}, None, None)
    except IndexError:
        max_combination = ({}, 0, None)
    print_result(max_combination, N, len(data))


def _numbers_combinations(skip_idx, sorted_data, possible_combinations, N):
    """
    find one max combination of numbers from lists except of one
    """
    selected_numbers = {idx: val[0] for idx, val in enumerate(sorted_data) if idx != skip_idx}
    is_divisible = False
    if sum(selected_numbers.values()) % N == 0:
        stack = [0 if idx != skip_idx else -1 for idx in range(len(sorted_data))]
        len_stack = [len(v) for k, v in enumerate(sorted_data)]
        max_stack = [v - 1 if idx != skip_idx else -1 for idx, v in enumerate(len_stack)]
        if non_divisible_sum(stack, len_stack, max_stack, skip_idx, sorted_data, selected_numbers, N) == 0:
            is_divisible = True
    possible_combinations.append(
        ({}, None, None) if is_divisible
        else (selected_numbers, skip_idx, sum(selected_numbers.values()))
    )


def non_divisible_sum(stack, len_stack, max_stack, skip_idx, sorted_data, selected_numbers, N):
    """
    finds non-divisible combination by given stack

    if there are no non-divisible combination, it returns 0
    """
    max_sum = (-float('inf'), [])
    while index_list := _generate_index_combinations(stack, len_stack, max_stack, skip_idx):
        curr_sum = 0
        for i, val in enumerate(index_list):
            if i == skip_idx:
                continue
            curr_sum += sorted_data[i][val]
        if curr_sum % N != 0 and curr_sum > max_sum[0]:
            index_list_copy = _deep_copy(index_list)
            max_sum = (curr_sum, index_list_copy)
    if not max_sum[1]:
        return 0
    for idx, val in enumerate(max_sum[1]):
        if idx == skip_idx:
            continue
        selected_numbers[idx] = sorted_data[idx][val]


def _generate_index_combinations(stack, len_stack, max_stack, skip_idx):
    """
    generates all combination
    """
    n = len(stack)
    for i in range(n - 1, -1, -1):
        if i == skip_idx:
            continue
        stack[i] += 1
        if stack[i] > len_stack[i] - 1:
            stack[i] = 0
        else:
            break
    if stack == max_stack:
        return None
    return stack


def _deep_copy(lst):
    """
    makes deep copy of list
    """
    if isinstance(lst, list):
        copy_lst = []
        for val in lst:
            copy_val = _deep_copy(val)
            copy_lst.append(copy_val)
        return copy_lst
    else:
        return lst


def _print_numbers(combination):
    """
    prints from which list number was selected and the number itself
    """
    for k, v in combination.items():
        print(k, v)


def print_result(max_combination, N, amount):
    """
    prints the result of program
    """
    print("THE WORK IS DONE")
    print(N)
    print(amount)
    print(max_combination[1])
    print(max_combination[2])
    _print_numbers(max_combination[0])

main()

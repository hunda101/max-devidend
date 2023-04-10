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
            lst = input("Input numbers of list(input white line to stop): ").split()
            if not lst:
                break
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
    finds all max combinations from lists except of one list and passes combination with maximum sum
    """
    possible_combinations = []
    sorted_data = [sorted(set(lst), reverse=True) for lst in data]
    try:
        for skip_idx in range(len(sorted_data)):
            _numbers_combinations(skip_idx, sorted_data, possible_combinations, N)
        max_combination = max(possible_combinations, key=lambda mx: sum(mx[0].values()))
    except ValueError:
        max_combination = ({}, None, None)
    except IndexError:
        max_combination = ({}, 0, None)
    print_result(max_combination, N, len(sorted_data))


def _numbers_combinations(skip_idx, sorted_data, possible_combinations, N):
    """
    find one max combination of numbers from lists except of one
    """
    sorted_data_copy = _deep_copy(sorted_data)
    selected_numbers = {idx: val[0] for idx, val in enumerate(sorted_data_copy) if idx != skip_idx}
    is_dividable = False
    delta_index = 0
    while sum(selected_numbers.values()) % N == 0:
        if _find_min_delta(selected_numbers, sorted_data_copy) == 0:
            is_dividable = True
            break
        delta_index += 1
    possible_combinations.append(
        ({}, None, None) if is_dividable
        else (selected_numbers, skip_idx, sum(selected_numbers.values()))
    )


def _find_min_delta(selected_numbers, sorted_data_copy):
    """
    finds the best solution to choose number to get maximum sum that is not divided by N
    """
    selected_numbers_delta = {}
    for k, v in selected_numbers.items():
        if len(sorted_data_copy[k]) > 1:
            delta = sorted_data_copy[k][0] - sorted_data_copy[k][1]
            selected_numbers_delta[k] = delta
    if not selected_numbers_delta:
        return 0
    min_delta_key = min(selected_numbers_delta, key=selected_numbers_delta.get)
    selected_numbers[min_delta_key] = sorted_data_copy[min_delta_key][1]
    sorted_data_copy[min_delta_key].pop(0)


def _deep_copy(lst):
    """
    makes deep copy of list
    """
    if isinstance(lst, list):
        return [_deep_copy(val) for val in lst]
    else:
        return lst


def _print_numbers(combination):
    """
    prints from which list number was selected and the number itself
    """
    for k, v in combination.items():
        print(f"list: {k}, number: {v}", end="; ")


def print_result(max_combination, N, amount):
    """
    prints the result of program
    """
    print("THE WORK IS DONE, ")
    print(f"For N = {N}, ")
    print(f"Amount of lists: {amount}, ")
    print(f"List from which a number was not selected: {max_combination[1]},")
    print(f"Max sum that is not divisible by {N} is {max_combination[2]}")
    print("These numbers were selected: ", end="")
    _print_numbers(max_combination[0])


main()

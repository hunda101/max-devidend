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


def _numbers_combinations(skip_idx, select_idx, sorted_data, possible_combinations, N):
    """
    find one max combination of numbers from lists except of one
    """
    selected_numbers = {idx: val[0] for idx, val in enumerate(sorted_data) if idx not in (skip_idx, select_idx)}
    max_index_value = sorted_data[select_idx][0]
    selected_numbers[select_idx] = max_index_value
    is_dividable = False
    delta_index = 0
    while sum(selected_numbers.values()) % N == 0:
        if _find_min_delta(selected_numbers, sorted_data, delta_index) == 0:
            is_dividable = True
            break
        delta_index += 1
    possible_combinations.append(
        ({}, None, None) if is_dividable
        else (dict(sorted(selected_numbers.items())), skip_idx, sum(selected_numbers.values()))
    )


def _find_min_delta(selected_numbers, sorted_data, idx):
    """
    finds the best solution to choose number to get maximum sum that is not divided by N
    """
    selected_numbers_delta = {}
    for k, v in selected_numbers.items():
        if len(sorted_data[k]) > idx + 1:
            delta = sorted_data[k][idx] - sorted_data[k][idx + 1]
            selected_numbers_delta[k] = delta
    if not selected_numbers_delta:
        return 0
    min_delta_key = min(selected_numbers_delta, key=selected_numbers_delta.get)
    selected_numbers[min_delta_key] = sorted_data[min_delta_key][idx + 1]


def max_divisor(data, N):
    """
    finds all max combinations from lists except of one list and passes combination with maximum sum
    """
    possible_combinations = []
    sorted_data = [sorted(set(lst), reverse=True) for lst in data]
    try:
        select_idx = 1
        for skip_idx in range(len(sorted_data)):
            _numbers_combinations(skip_idx, select_idx, sorted_data, possible_combinations, N)
            select_idx += 1
            if select_idx == len(sorted_data):
                select_idx = 0
        max_combination = max(possible_combinations, key=lambda mx: sum(mx[0].values()))
    except ValueError:
        max_combination = ({}, None, None)
    except IndexError:
        max_combination = ({}, 0, None)
    print_result(max_combination, N, len(sorted_data))


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

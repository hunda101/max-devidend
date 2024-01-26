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
        max_divisor(data, N)
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except (EOFError, ValueError) as e:
        print("***** error")
        print(repr(e))


def max_divisor(data, N):
    """
    finds all max combinations from lists except of one list and passes combination with maximum sum of numbers
    """
    possible_combinations = []
    sorted_data = [sorted(set(lst), reverse=True) for lst in data]
    len_stack = [len(v) for k, v in enumerate(sorted_data)]
    max_stack = [v - 1 for idx, v in enumerate(len_stack)]
    try:
        if len(sorted_data) == 1:
            raise IndexError
        for skip_idx in range(len(sorted_data)):
            numbers_combinations(skip_idx, sorted_data, possible_combinations, N, max_stack)
        max_combination = max(possible_combinations, key=lambda mx: sum(mx[0].values()))
    except ValueError:
        max_combination = ({}, None, None)
    except IndexError:
        max_combination = ({}, 0, None)
    print_result(max_combination, N, len(sorted_data))


def numbers_combinations(skip_idx, sorted_data, possible_combinations, N, max_stack):
    """
    find one max combination of numbers from lists except of one
    """
    selected_numbers = {idx: val[0] for idx, val in enumerate(sorted_data) if idx != skip_idx}
    is_divisible = False
    stack = [0 if idx != skip_idx else -1 for idx in range(len(sorted_data))]
    is_divisible, stack, selected_numbers = find_non_divisible_sum(stack,max_stack, skip_idx, sorted_data,
                                                                   selected_numbers, N, is_divisible)
    possible_combinations.append(
        ({}, None, None) if is_divisible
        else (selected_numbers, skip_idx, sum(selected_numbers.values()))
    )


def find_non_divisible_sum(stack, max_stack, skip_idx, sorted_data, selected_numbers, N, is_divisible):
    """
    finds non-divisible combination by given stack
    if there are no non-divisible combination, it stops searching
    """
    if sum(selected_numbers.values()) % N == 0:
        delta = {}
        for i, val in enumerate(stack):
            if i != skip_idx:
                while val < max_stack[i] and (sorted_data[i][val] - sorted_data[i][val + 1]) % N == 0:
                    sorted_data[i].pop(val + 1)
                    max_stack[i] -= 1
                if val < max_stack[i]:
                    delta[i] = sorted_data[i][val] - sorted_data[i][val+1]
        if not delta:
            is_divisible = True
            return is_divisible, stack, selected_numbers
        min_key = min(delta, key=delta.get)
        stack[min_key] = +1
        selected_numbers[min_key] = sorted_data[min_key][stack[min_key]]

    return is_divisible, stack, selected_numbers


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

def func(A, N):
    B = set()
    row_sums = [sum(row) for row in A]
    max_values = {}
    for i, row in enumerate(A):
        sorted_row = sorted(set(row), reverse=True)
        max_values[i] = (sorted_row[0], sorted_row[1] if len(sorted_row) > 1 else None)
    for skip_index in range(len(A)):
        for select_index in range(len(A)):
            if select_index == skip_index:
                continue
            max_index_value, second_max_index_value = max_values[select_index]
            tmp_dict = {select_index: max_index_value}
            for i, row in enumerate(A):
                if i != skip_index and i != select_index:
                    tmp_dict[i] = max_values[i][0]
            if sum(tmp_dict.values()) % N == 0:
                delta_dict = {}
                for k, v in tmp_dict.items():
                    if max_values[k][1] is not None:
                        delta = max_values[k][0] - max_values[k][1]
                        if delta == 0:
                            continue
                        delta_dict[k] = delta
                if delta_dict:
                    min_delta_key = min(delta_dict, key=delta_dict.get)
                    del tmp_dict[min_delta_key]
                    max_values[min_delta_key] = (max_values[min_delta_key][1], None) if len(A[min_delta_key]) == 1 else (A[min_delta_key][1], None)
            B.add(tuple(sorted(tmp_dict.values())))
    max_B_sum = max([sum(b) for b in B])
    return max_B_sum

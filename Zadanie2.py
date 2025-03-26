def max_dict(*dicts):
    result = {}
    all_keys = set()
    for d in dicts:
        all_keys.update(d.keys())
    for key in all_keys:
        max_value = None
        for d in dicts:
            if key in d:
                if max_value is None or d[key] > max_value:
                    max_value = d[key]
        if max_value is not None:
            result[key] = max_value
    return result
def sum_dict(*dicts):
    result = {}
    all_keys = set()
    for d in dicts:
        all_keys.update(d.keys())
    for key in all_keys:
        total_value = 0
        for d in dicts:
            if key in d:
                total_value += d[key]
        result[key] = total_value
    return result
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
print(max_dict(dict_1, dict_2))
print(sum_dict(dict_1, dict_4, dict_3))
print(max_dict(dict_1, dict_2, dict_3, dict_4))
print(sum_dict(dict_1, dict_2, dict_3, dict_4))
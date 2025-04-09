def slicer(t, element):
    first_index = -1
    second_index = -1
    for i, value in enumerate(t):
        if value == element:
            if first_index == -1:
                first_index = i
            elif second_index == -1:
                second_index = i
    if first_index == -1:
        return ()
    if second_index == -1:
        return t[first_index:]
    return t[first_index:second_index + 1]
print(slicer((1, 2, 3, 4, 2, 5), 2))
print(slicer((1, 2, 3, 4, 5), 6))
print(slicer((1, 2, 3, 4, 2, 5), 3))
print(slicer((1, 2, 3, 4, 2, 5), 1))
print(slicer((1, 1, 1, 1), 1))
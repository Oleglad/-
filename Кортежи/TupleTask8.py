def tpl_sort(t):
    if all(isinstance(x, int) for x in t):
        return tuple(sorted(t))
    else:
        return t
print(tpl_sort((3, 1, 4, 1, 5, 9)))
print(tpl_sort((3, 1, 4, 'a', 5, 9)))
print(tpl_sort((10, -2, 0)))
print(tpl_sort((1, 2, 3, 4.5)))

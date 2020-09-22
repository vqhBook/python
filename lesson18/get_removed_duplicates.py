def get_removed_duplicates(li):
    if len(li) == 0:
        return []
    else:
        rest = get_removed_duplicates(li[1:])
        return rest if li[0] in rest else [li[0]] + rest

li = [1, 2, 3, 2, 1]
print(get_removed_duplicates(li))
print(li)

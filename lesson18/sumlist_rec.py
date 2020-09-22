def sum_list(li):
    if len(li) == 0:
        return 0

    return li[0] + sum_list(li[1:])

def remove_duplicates(li):
    i = 0
    while i < len(li):
        j = i + 1
        while j < len(li):
            if li[j] == li[i]:
                del li[j]
            else:
                j += 1
        i += 1

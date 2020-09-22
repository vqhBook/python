def remove_duplicates(li, s=0):
    if s >= len(li):
        return

    if li[s] in li[s+1:]:
        del li[s]
        remove_duplicates(li, s)
    else:
        remove_duplicates(li, s + 1)

li = [1, 2, 3, 2, 1]
print(remove_duplicates(li))
print(li)

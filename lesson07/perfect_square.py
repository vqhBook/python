a, b = 10, 100
for i in range(a, b + 1): # tìm số chính phương trong [a, b]
    if i % 2 == 0:
        pass # TODO: thay bằng continue để bỏ qua số chẵn

    if int(i**0.5)**2 == i: # i là số chính phương
        print(i)
        pass # TODO: thay bằng break nếu chỉ muốn tìm một số

print("Done!")

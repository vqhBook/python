def char_freq(text):
    chars = set(text)
    print(f"Có {len(chars)} kí tự trong chuỗi {text}")
    for c in sorted(chars):
        print(f"{c} xuất hiện {text.count(c)} lần")
    if chars:
        most =  max([(c, text.count(c)) for c in chars],
                    key=lambda pair: pair[1])
        print("Nhiều nhất là %s xuất hiện %d lần" % most)
    
char_freq(input("Nhập chuỗi nào đó: "))

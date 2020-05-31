from collections import Counter

def char_freq(text):
    chars = Counter(text)
    print(f"Có {len(chars)} kí tự trong chuỗi {text}")
    for c in sorted(chars):
        print(f"{c} xuất hiện {chars[c]} lần")
    if chars:
        most =  chars.most_common(1)[0]
        print("Nhiều nhất là %s xuất hiện %d lần" % most)
    
char_freq(input("Nhập chuỗi nào đó: "))

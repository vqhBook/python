def sayhello(*name_language_pairs):
    if not name_language_pairs:
        name_language_pairs = (("World", "en"), ) # Bộ có 1 phần tử
    for name, language in name_language_pairs:
        hello_verb = ("Chào" if language == "vi" else "Hello")
        hello_string = f" {hello_verb} {name} "
        print("=" * (len(hello_string) + 2))
        print("|" + hello_string + "|")
        print("=" * (len(hello_string) + 2))

sayhello()
sayhello(("Python", "en"), ("Vũ Quốc Hoàng", "vi"), ("Guido", "en"))

names = []
while name := input("Nhập tên: "):
    if name.isascii():
        names.append((name, "en"))
    else:
        names.append((name, "vi"))
sayhello(*names)

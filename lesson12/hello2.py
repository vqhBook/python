def sayhello(*names, language="en"):
    if not names:
        names = ("World", ) # Bộ có 1 phần tử
    for name in names:
        hello_verb = ("Chào" if language == "vi" else "Hello")
        hello_string = f" {hello_verb} {name} "
        print("=" * (len(hello_string) + 2))
        print("|" + hello_string + "|")
        print("=" * (len(hello_string) + 2))

sayhello()
sayhello("Python", "Hoang Vu Quoc", "Guido van Rossum")

names = []
while name := input("Nhập tên: "):
    names.append(name)
sayhello(*names, language="vi")

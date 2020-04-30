def sayhello(name="World", language="en"):
    hello_verb = ("Chào" if language == "vi" else "Hello")
    hello_string = f" {hello_verb} {name} "
    print("=" * (len(hello_string) + 2))
    print("|" + hello_string + "|")
    print("=" * (len(hello_string) + 2))

sayhello()
sayhello("Python")
sayhello(language="en")
sayhello("Vũ Quốc Hoàng", language="vi")
sayhello(language="en", name="Guido van Rossum")
a_name = input("Tên của bạn là gì? ")
sayhello(a_name, "vi")

def sayhello(name):
    hello_string = " Chào " + name + " "
    print("=" * (len(hello_string) + 2))
    print("|" + hello_string + "|")
    print("=" * (len(hello_string) + 2))

sayhello("Python")
sayhello("Vũ Quốc Hoàng")
sayhello("Guido van Rossum")
a_name = input("Tên của bạn là gì? ")
sayhello(a_name)

def sayhello(*names):
    for name in names:
        hello_string = " Chào " + name + " "
        print("=" * (len(hello_string) + 2))
        print("|" + hello_string + "|")
        print("=" * (len(hello_string) + 2))
            
sayhello("Python", "Vũ Quốc Hoàng", "Guido van Rossum")

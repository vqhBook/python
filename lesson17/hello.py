import sys

def sayhello(*names, file=sys.stdout):
    for name in names:
        hello_string = " Chào " + name + " "
        print("=" * (len(hello_string) + 2), file=file)
        print("|" + hello_string + "|", file=file)
        print("=" * (len(hello_string) + 2), file=file)
            
sayhello("Python", "Vũ Quốc Hoàng", "Guido van Rossum")
f = open("hello_message.txt", "wt", encoding="utf-8")
sayhello("Python", "Vũ Quốc Hoàng", "Guido van Rossum", file=f)
f.close()

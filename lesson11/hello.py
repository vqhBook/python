import sys

if len(sys.argv) < 2:
    name = input("What's your name? ")
else:
    name = " ".join(sys.argv[1:])
print("Hello", name)

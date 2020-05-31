def func1(d):
    # global a
    a = d
    print(a)
    
def func2(d):
    def func3():
        # nonlocal a
        a = 2 * d
        print(a)
        
    a = d
    func3()
    print(a)
    
a = 0
func1(1)
print(a)
func2(2)
print(a)
# func3()

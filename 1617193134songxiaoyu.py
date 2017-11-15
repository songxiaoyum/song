def prt1(x):
    for i in range(x):
        print("+",end='')
        print("-"*4,end='')
    print("+")
def prt2(y):
    for i in range(y):
        print("|",end='      ')
    print("|")
    
def prttzg(a,b):
    for i in range(a):
        prt1(b)
        prt2(b)
        prt2(b)
        prt2(b)
    prt1(b)

prttzg(8,8)

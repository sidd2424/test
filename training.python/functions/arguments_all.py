def foo13(a, b, c=100, *args, **kwargs):
    print(a, b, c, args, kwargs)


foo13(1, 2, 3, 4, 5, 6, A=1, B=2, C=3)

###########################


def foo15(a=[], b={}):
    print(a, b)
    a.append(len(a))
    b[len(a)] = len(a)


foo15()
foo15()

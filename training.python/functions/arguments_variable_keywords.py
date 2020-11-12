def foo11(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('Key - ', key, ' and Value - ', value)


foo11(**{'a': 1, 'b': 2, 'c': 3})
# foo11(data_set)

def generate_squares_simply(upto):
    result = []
    for number in range(1, upto):
        result.append(number*number)
    return result


print(generate_squares_simply(11))
print('')


def generate_squares(upto):
    for number in range(1,upto):
        yield number * number


print(generate_squares(11))
print(list(generate_squares(11)))

squares= generate_squares(11)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

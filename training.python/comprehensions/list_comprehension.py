# Square manual
squares=[]
for number in range(1,11):
    squares.append(number*number)
print(squares)
print('')

# Squares using utils
squares= map(lambda number: number * number, range(1,11))
print(list(squares))
print('')


# Square with list comprehension

squares=[number * number for number in range(1,11) if number>5]
print(squares)
print('')
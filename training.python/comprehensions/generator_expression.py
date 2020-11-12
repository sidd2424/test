odd_cubes1 = filter(
    lambda cube: cube % 2,
    [number ** 3 for number in range(11)]
)
print(list(odd_cubes1))
print('')


odd_cubes2 = (number ** 3 for number in range(11) if number % 2)
print(list(odd_cubes2))
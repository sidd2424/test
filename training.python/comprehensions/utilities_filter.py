obj =[2, 4, 1, 10, 20, 50, 3]
obj_filtered= filter(lambda number: number>3 , obj)
for number in obj_filtered:
    print(number)
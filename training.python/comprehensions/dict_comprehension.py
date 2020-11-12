from string import ascii_lowercase


alphabet_map = {
    character : position
    for(position, character) in enumerate(ascii_lowercase, 1)
}
print(alphabet_map)




# Set Comprehension
# data_set = { character in character 'Hello'}
# print(data_set)
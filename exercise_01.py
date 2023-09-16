def get_unique_list(list_input):
    list_output = []
    for i in range(len(list_input)):
        if list_input[i] not in list_output:
            list_output.append(list_input[i])
    return list_output
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
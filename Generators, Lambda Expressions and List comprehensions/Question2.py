def compose_lst(lst):
    return [dict(inner_tuple for inner_tuple in lst)[new_index] if new_index in list(inner_tuple[0] for inner_tuple in lst)
                else -1000 for new_index in list(index for index in range(max(list(inner_tuple[0] for inner_tuple in lst))+1))]


print(compose_lst([(4,9), (0,2), (1,4), (3,2)]))  #will print [2, 4, -1000, 2, 9]

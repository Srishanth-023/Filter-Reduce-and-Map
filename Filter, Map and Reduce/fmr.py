def odd_even_sum(my_list):
    from functools import reduce
    odd_list = list(filter(lambda x: x % 2 == 1, my_list))
    even_list = list(filter(lambda x: x % 2 == 0, my_list))
    
    odd_list_sum = reduce(lambda x, y: x + y, map(lambda x: x, odd_list), 0)
    even_list_sum = reduce(lambda x, y: x + y, map(lambda x: x, even_list), 0)
    
    return odd_list, even_list, odd_list_sum, even_list_sum

odd_list, even_list, odd_list_sum, even_list_sum = odd_even_sum([1, 2, 3, 4, 5, 6])

print(f"ODD LIST : {odd_list}")
print(f"SUM OF ODD LIST : {odd_list_sum}")
print(f"EVEN LIST : {even_list}")
print(f"SUM OF EVEN LIST : {even_list_sum}")
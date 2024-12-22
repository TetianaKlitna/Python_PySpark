my_set = {1, 10, 15}
print(my_set)
new_set = {item*item for item in my_set if item > 1}
print(new_set)

my_scores = {'a': 100, 'b': 80, 'c': 60}
scores = [my_scores[key] for key in my_scores]
print(type(scores))  # class list
print(scores)
new_scores = {key: value + 5 for key, value in my_scores.items()}
print(type(new_scores), new_scores)  # class dict

nums = (1, 2, 3)
new_nums = (num*num for num in nums)
print(type(new_nums))  # class generator

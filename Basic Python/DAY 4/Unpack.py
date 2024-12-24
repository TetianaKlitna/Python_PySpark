my_fruits = ['banana', 'apple', 'orange']
print(my_fruits, type(my_fruits))
v_banana, v_apple, v_orange = my_fruits
print(v_banana, v_apple, v_orange)
first_fruit, *remaining_fruits = my_fruits
print(first_fruit, type(remaining_fruits))

my_languages = ('Python', 'Java', 'Javascript') 
print(my_languages, type(my_languages))
my_language1, *other_languages = my_languages
print(other_languages, type(tuple(other_languages)))

user_profile = {
    'name': 'Tania',
    'comments_qty': 10,
}

def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    
    return f"{name} has {comments_qty} comments"

print(user_info(**user_profile))

user_profile = ['Tania', 10]
print(user_info(*user_profile))
    

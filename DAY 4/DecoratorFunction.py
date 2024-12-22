def decorator_function1(original_fynction):
    def wrapper_function(*args, **kwargs):
        print("Before")
        result = original_fynction(*args, **kwargs)
        print("After")

        return result

    return wrapper_function


@decorator_function1
def my_function(a, b=10):
    print("This is my Function!")
    return (a, b)


print(my_function(12))

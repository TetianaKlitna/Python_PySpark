def concat(*args, **kwargs):

    result = ""
    
    for arg in args:
        result += " " + arg

    for kwarg in kwargs.values():
        result += " " + kwarg
    return result

print(concat("Python", "is", "great!"))
print(concat(start="Python", middle="is", end="great!"))

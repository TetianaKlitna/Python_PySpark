def snake_case_v1(text):
    try:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
    except:
        print("The snake_case() function expects a string as an argument, please check the data type provided.")


snake_case_v1("User Name 187")


def snake_case_v2(text):
    if isinstance(text, str):
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
    else:
        raise TypeError(
            "The snake_case() function expects a string as an argument, please check the data type provided.")


snake_case_v2("User Name 187")

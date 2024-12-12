def calculate_love_score(name1, name2):
    combination_names = list(name1 + name2)
    cnt_true = 0
    cnt_love = 0
    for item in combination_names:
        if item.lower() in "true":
            cnt_true += 1
        if item.lower() in "love":
            cnt_love += 1
    print(str(cnt_true) + str(cnt_love))

calculate_love_score("Kanye West", "Kim Kardashian")
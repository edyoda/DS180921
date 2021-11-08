import fruits

def boy(no_of_seeds):
    if no_of_seeds == 1:
        print(fruits.one_seed_fruit())
    elif no_of_seeds == 0:
        print(fruits.seedless_fruit())
boy(1)
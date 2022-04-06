def custom_sort(e):
    # return e # sort by alphabetical order
    return len(e) # sort by the length of the string


def display_sandwiches(sandwiches, sample=-1):

    nb_sandwiches = len(sandwiches)
    if nb_sandwiches == 0:
        print("OUT OF SANDWICH")
        return

    print(f"----- Our sandwiches ({nb_sandwiches}) -----")
    sandwiches.sort(reverse=True, key=custom_sort)

    if sample == -1:
        for sandwich in sandwiches:
            print(sandwich)
    else:
        for sandwich in sandwiches[:sample:]:
            print(sandwich)

    print(f"- First sandwich : {sandwiches[0]}")
    print(f"- Last sandwich : {sandwiches[-1]}")


def add_sandwich(sandwiches):

    display_sandwiches(sandwiches)
    flag = False
    while not flag:
        sandwich = input("\nAdd a new sandwich :\n")
        if sandwich.lower() in sandwiches:
            print(f"ERROR : {sandwich} already exists\n")
        else:
            sandwiches.append(sandwich)
            print(f"{sandwich} has been added")
            display_sandwiches(sandwiches, 3)
            flag = True


sandwiches = ["dagobert", "poulet curry", "norvégien", "fermier"]
add_sandwich(sandwiches)

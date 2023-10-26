def input_set():
    input_1 = input("\nВведіть множину A: ")
    input_2 = input("Введіть множину B: ")
    return input_1, input_2


def define_sets():
    set1, set2 = input_set()
    set1 = set(int(item) for item in set1.split())
    set2 = set(int(item) for item in set2.split())
    return set1, set2


def set_union(a, b):
    set3 = a.copy()
    for item in b:
        if item in a:
            continue
        else:
            set3.add(item)
    return set3


def set_intersection(a, b):
    set3 = set()
    for item in b:
        if item in a:
            set3.add(item)
        else:
            continue
    return set3


def subset_check(a, b):
    a_subset = False
    b_subset = False
    equals = False
    for item in a:
        if item in b:
            a_subset = True
        else:
            a_subset = False
            break
    for item in b:
        if item in a:
            b_subset = True
        else:
            b_subset = False
            break
    if a_subset and b_subset == True:
        equals = True

    return a_subset, b_subset, equals


def set_difference(a, b):
    set3a = a.copy()
    for item in b:
        if item in a:
            set3a.remove(item)
        else:
            continue
    set3b = b.copy()
    for item in a:
        if item in b:
            set3b.remove(item)
        else:
            continue
    return set3a, set3b


def set_symdifference(a, b):
    sym_dif = a.copy()
    sym_dif = sym_dif | b
    sym_dif = sym_dif - set_intersection(a, b)
    return sym_dif


def set_dir_product(a, b):
    dir_pr = set()
    for item in a:
        for item1 in b:
            pair = (item, item1)
            dir_pr.add(pair)
    dir_pr_copy = dir_pr.copy()
    for pair in dir_pr:
        stored_pair = pair
        for pair1 in dir_pr:
            if stored_pair == pair1[::-1]:
                dir_pr_copy.remove(pair1)
            else:
                continue
    return dir_pr_copy


# def binary(a, b):
#     a1 = str(a.copy())
#     b1 = str(b.copy())
#     a1 = bytearray(a1)
#     b1 = bytearray(b1)
#     return a1, b1


try:
    my_set1, my_set2 = define_sets()
    a_sub, b_sub, equals = subset_check(my_set1, my_set2)
    dif_a, dif_b = set_difference(my_set1, my_set2)
    # bin_a, bin_b = binary(my_set1, my_set2)
    print(f"\n{my_set1}\n{my_set2}\n")
    print(f"Обʼєднання множин:{set_union(my_set1, my_set2)}")
    print(f"Перетин множин:{set_intersection(my_set1, my_set2)}")
    if a_sub:
        print("\nПерша множина є підмножиною другої\n")
    if b_sub:
        print("\nДруга множина є підмножиною першої\n")
    if equals:
        print("\nМножини є рівними\n")
    print(f"A - B = {dif_a}\nB - A = {dif_b}")
    print(f"A ∩ B = {dif_b}\nB ∩ A = {dif_a}")
    print(f"Симетрична різниця:{set_symdifference(my_set1, my_set2)}")
    print(f"Декартовий добуток:{set_dir_product(my_set1, my_set2)}")
    # print(f"\n{bin_a}\n{bin_b}\n")

except ValueError:
    print("Exception occurred. Please check input data formatting")

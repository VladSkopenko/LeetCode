def merge_sorted_lists_into_list1(list1, list2):
    list1 += [None] * len(list2)

    # Індекси
    i = len(list1) - len(list2) - 1
    j = len(list2) - 1
    k = len(list1) - 1  # Останній елемент першого списку а також наш поінтер

    while j >= 0:  # Поки не закінчився список2
        if i >= 0 and list1[i] > list2[j]:
            list1[k] = list1[i]
            i -= 1
        else:  # Умовою зрівнюєм елменти списків і ставимо на індекс поінтера
            list1[k] = list2[j]
            j -= 1
        k -= 1  #


list1 = [1, 2, 3, 5, 6, 6, 6, 7, 9, 12, 13]
list2 = [2, 3, 4, 5, 5, 6, 7]

merge_sorted_lists_into_list1(list1, list2)
print(list1)

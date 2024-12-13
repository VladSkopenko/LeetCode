l1 = [2, 4, 3]
l2 = [5, 6, 4, 12, 4, 6]


def merged2list_intolist1(list1, list2):
    list1 += [None] * len(list2)

    i = len(list1) - len(list2) - 1
    j = len(list2) - 1
    k = len(list1) - 1

    while j >= 0:
        if i >= 0 and list1[i] > list2[j]:
            list1[k] = list1[i]
            i -= 1
        else:
            list1[k] = list2[j]
            j -= 1
        k -= 1


merged2list_intolist1(l1, l2)
print(l1)

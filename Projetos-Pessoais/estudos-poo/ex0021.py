def merge_two_sorted_lists(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    mergedList = []
    for i in list1:
        mergedList.append(i)
    for i in list2:
        mergedList.append(i)
    mergedList = sorted(mergedList)
    return mergedList


print(merge_two_sorted_lists([1, 2, 4], [1, 3, 4]))

def positives_negatives(nums=[]):
    pos = []
    neg = []
    zero = [0]
    for i in nums:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    return neg, zero, pos


def mod(num=0):
    if num >= 0:
        return num
    else:
        return -1 * num


def num_pairs(nums=None):
    if nums is None:
        nums = []

    processed_nums = []
    container = []

    for i in nums:
        if i < 0 and -i in processed_nums:
            container.append([i, -i])
        processed_nums.append(i)
    return container


print(num_pairs(nums=[0, 1, -1, 2, -2, 3]))

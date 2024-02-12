

def max_change(a, b):
    b = sorted(b)

    aa = [i for i in a]
    bb = [i for i in b]

    len_a = len(a)
    len_b = len(b)

    j = len_b - 1
    for i in range(len_a):

        if j < 0:
            break

        if (bb[j] > aa[i]):
            aa[i] = bb[j]
            j -= 1

    res = "".join(aa)
    return res


a = input("a = ")
b = input("b = ")

print(max_change(a, b))


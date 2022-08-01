
# intersection
def list_intersect_gen(A, B):
    Ag = (i for i in A)
    Bg = (i for i in B)
    C = []

    b = next(Bg)
    for a in Ag:
        if not b:
            break

        while a > b:
            print(f'> a:{a},b:{b}')
            b = next(Bg, None)
        if a == b:
            print(f'== a:{a},b:{b}')
            C.append(a)
            b = next(Bg, None)
            continue
        # consider removing elif
        #elif a < b:
        #    print(f'< a:{a},b:{b}')
        #    continue

    return C


def list_intersect_gen2(A, B):
    Ag = (i for i in A)
    Bg = (i for i in B)
    C = []

    a = next(Ag)
    b = next(Bg)
    while a is not None and b is not None:
        if a == b:
            C.append(a)
            a = next(Ag, None)
            b = next(Bg, None)
        elif a < b:
            a = next(Ag, None)
        elif a > b:
            b = next(Bg, None)

    return C




def test_list_intersect_gen():
    assert list_intersect_gen([1,2,3,4], [5,6,7,8]) == []
    assert list_intersect_gen([1,2,3,4], [3,4,5,6]) == [3,4]
    assert list_intersect_gen([1,2,3,4], [3,4]) == [3,4]
    assert list_intersect_gen([1,5,9], [2,5,10]) == [5]
    assert list_intersect_gen([1,2,3,4,5,6,7,8,9,10], [2,9]) == [2,9]



# union

# set_diff

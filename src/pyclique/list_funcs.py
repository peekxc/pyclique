
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

    a = next(Ag, None)
    b = next(Bg, None)
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



from math import inf
# union
def list_union_unique(A, B):
    Ag = (a for a in A)
    Bg = (b for b in B)
    C = []

    a = next(Ag, inf)
    b = next(Bg, inf)
    c = -inf
    while a is not inf or b is not inf:
        if a == b:
            print(f'= a: {a}, b: {b}, c: {c}')
            if a > c:           # change to >= to include duplicates
                c = a
                C.append(c)
            a = next(Ag, inf)
            b = next(Bg, inf)
        elif a < b:
            print(f'< a: {a}, b: {b}, c: {c}')
            if a > c:           # change to >= to include duplicates
                c = a
                C.append(c)
            a = next(Ag, inf)
        elif a > b:
            print(f'> a: {a}, b: {b}, c: {c}')
            if b > c:           # change to >= to include duplicates
                c = b
                C.append(c)
            b = next(Bg, inf)

    return C


    

def test_list_union_unique():
    assert list_union_unique([1,2,3,4], [5,6,7,8]) == [1,2,3,4,5,6,7,8]
    assert list_union_unique([1,2,3,4], [3,4,5,6]) == [1,2,3,4,5,6]
    assert list_union_unique([1,2,3,4], [3,4]) == [1,2,3,4]
    assert list_union_unique([1,5,9], [2,5,10]) == [1,2,5,9,10]
    assert list_union_unique([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,2,3,4,5,6,7,8,9,10]
    assert list_union_unique([1,7,9], [2,5,6]) == [1,2,5,6,7,9]
    assert list_union_unique([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,5,9,27,28,29,107,1037]


# set_diff

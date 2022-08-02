
# intersection
def list_intersect(A, B):
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


def test_list_intersect():
    assert list_intersect([1,2,3,4], [5,6,7,8]) == []
    assert list_intersect([1,2,3,4], [3,4,5,6]) == [3,4]
    assert list_intersect([1,2,3,4], [3,4]) == [3,4]
    assert list_intersect([1,5,9], [2,5,10]) == [5]
    assert list_intersect([1,2,3,4,5,6,7,8,9,10], [2,9]) == [2,9]


def list_intersect2(A, B):
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


def test_list_intersect2():
    assert list_intersect2([1,2,3,4], [5,6,7,8]) == []
    assert list_intersect2([1,2,3,4], [3,4,5,6]) == [3,4]
    assert list_intersect2([1,2,3,4], [3,4]) == [3,4]
    assert list_intersect2([1,5,9], [2,5,10]) == [5]
    assert list_intersect2([1,2,3,4,5,6,7,8,9,10], [2,9]) == [2,9]


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
            if a > c:
                c = a
                C.append(c)
            a = next(Ag, inf)
            b = next(Bg, inf)
        elif a < b:
            print(f'< a: {a}, b: {b}, c: {c}')
            if a > c:
                c = a
                C.append(c)
            a = next(Ag, inf)
        elif a > b:
            print(f'> a: {a}, b: {b}, c: {c}')
            if b > c:
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


def list_union_duplicate(A, B):
    Ag = (a for a in A)
    Bg = (b for b in B)
    C = []

    a = next(Ag, inf)
    b = next(Bg, inf)
    c = -inf
    while a is not inf or b is not inf:
        if a <= b:
            print(f'= a: {a}, b: {b}, c: {c}')
            if a >= c:
                c = a
                C.append(c)
            a = next(Ag, inf)
        elif a > b:
            print(f'> a: {a}, b: {b}, c: {c}')
            if b >= c:
                c = b
                C.append(c)
            b = next(Bg, inf)

    return C


def test_list_union_duplicate():
    assert list_union_duplicate([1,2,3,4], [5,6,7,8]) == [1,2,3,4,5,6,7,8]
    assert list_union_duplicate([1,2,3,4], [3,4,5,6]) == [1,2,3,3,4,4,5,6]
    assert list_union_duplicate([1,2,3,4], [3,4]) == [1,2,3,3,4,4]
    assert list_union_duplicate([1,5,9], [2,5,10]) == [1,2,5,5,9,10]
    assert list_union_duplicate([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,2,2,3,4,5,6,7,8,9,9,10]
    assert list_union_duplicate([1,7,9], [2,5,6]) == [1,2,5,6,7,9]
    assert list_union_duplicate([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,0,0,0,5,5,9,27,28,29,107,1037]


# set_diff
def set_diff_add(A, B):
    Bg = (b for b in B)
    C = []

    b = next(Bg, inf)
    last_added = None
    for a in A:
        while a > b:
            b = next(Bg, inf)

        if a == b:
            continue
        elif a < b and a != last_added:
            C.append(a)
            last_added = a

    return C


def test_set_diff_add():
    assert set_diff_add([1,2,3,4], [5,6,7,8]) == [1,2,3,4]
    assert set_diff_add([1,2,3,4], [3,4,5,6]) == [1,2]
    assert set_diff_add([1,2,3,4], [3,4]) == [1,2]
    assert set_diff_add([1,5,9], [2,5,10]) == [1,9]
    assert set_diff_add([1,2,3,4,5,6,7,8,9,10], [2,9]) == [1,3,4,5,6,7,8,10]
    assert set_diff_add([1,7,9], [2,5,6]) == [1,7,9]
    assert set_diff_add([0,0,0,0,5,9,1037], [5,27,28,29,107]) == [0,9,1037]

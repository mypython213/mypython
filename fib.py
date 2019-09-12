def func(n, r):
    r +=n
    if (n<=0):
        return r
    else:
        n -= 1
        return func(n, r)

def func2(n):
    if len(n)>0:
        return n[0] + func2(n[1:])
    else:
        return 0



fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

print (func (5, 0))
print (func2 ([5, 1, 42]))


def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib2(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


# print(fib2(20))
# print(fib(20))



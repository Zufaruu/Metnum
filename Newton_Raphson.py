import math


# f(x)
def f(x):
    return (x * (math.e ** (-x))) + math.cos(2*x)

# turunan f(x)
def g(x):
    return ((1-x) * (math.e ** (-x))) - 2 * math.sin(2*x)


# fungsi metode Newton_Raphson
def newtonraphson(x0, e, N):
    iterasi = 0
    is_convergen = True
    x1 = 0

    condition = True            # condition bernilai benar selama nilai f(x) lebih dari nilai error e
    while condition:
        # perulangan berhenti jika turunan f(x) bernilai 0
        if g(x0) == 0.0:
            print('Error pembagi 0, ganti nilai x0!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iterasi ke-%d, x1 = %0.10f, f(x1) = %0.10f, g(x0) = %0.10f' % (iterasi, x1, f(x1), g(x0)))
        x0 = x1
        iterasi = iterasi + 1

        # perulangan berhenti jika nilai iterasi lebih dari N
        if iterasi > N:
            is_convergen = 0
            break

        condition = abs(f(x1)) > e

    if is_convergen == 1:
        print('\nNilai akar: %0.10f' % x1)
    else:
        print('\nTidak konvergen')


if __name__ == "__main__":
    x0 = 0.176281
    e = 0.0000000001
    N = 10

    print(f"x0: {x0}\n e: {e}\n N: {N}\n ")
    newtonraphson(x0, e, N)
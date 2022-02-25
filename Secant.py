import math


# f(x) di sini merupakan turunan dari f(x) -> (x**2) + 1 - ((x+1) * (math.e ** (-2*x)))
def f(x):
    return 2*x + ((2*x)+1)*(math.e)**(-2*x)


# fungsi metode secant
def secant(x0, x1, e, N):
    iterasi = 0
    x2 = 0

    condition = True            # condition bernilai benar selama nilai f(x) lebih dari nilai error e
    while condition:

        if f(x0) == f(x1):
            print('Error pembagi 0!')
            break

        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        print('Iterasi ke-%d, x2 = %0.10f, f(x2) = %0.10f' % (iterasi, x2, f(x2)))
        x0 = x1
        x1 = x2
        iterasi = iterasi + 1

        if iterasi > N:
            break

        condition = abs(f(x2)) > e

    print('\nNilai akar: %0.10f' % x2)


if __name__ == "__main__":
    x0 = 0.8
    x1 = 0.9
    e = 0.0000000001
    N = 10

    print(f"x0: {x0}\n x1: {x1}\n e: {e}\n N: {N}\n ")
    secant(x0, x1, e, N)

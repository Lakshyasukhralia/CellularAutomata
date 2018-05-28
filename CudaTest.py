import numba as nb

@nb.jit(nopython=True)
def loop():
    a = 0
    for i in range(0,100000000000000000000000000000000000):
        a = a + 2

loop()

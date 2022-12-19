import time
def time_function(func, args, n_trials=10):
    "Returns the time in seconds using func time and args"
    start_seconds = time.time()
    for i in range(n_trials):
        func(args)
    end_seconds = time.time()
    return end_seconds - start_seconds

    
def time_function_flexible(f, args, n_trials=10):
    "Returns a function/method through the argument and returns the output using trials as an integer"
    return f(*args)


if __name__ == '__main__':
    # Some tests to see if time_function works
    def add_2_nums(p1, p2): 
        return p1 + p2

    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    sum1 = time_function_flexible(add_2_nums, (3,4)) # created sum function and tested that it works using 3 arguments 3 + 4 = 7

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
    print(sum1)
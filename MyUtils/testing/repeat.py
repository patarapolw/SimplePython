import pytest
from time import time
from functools import partial


def repeat(rep=50):
    pytest.main(['--count={}'.format(rep), '-m', 'repeat'])


def repeat_until_failure(rep=1000):
    pytest.main(['--count={}'.format(rep), '-x', 'repeat'])


def timeit(func, validator=lambda x: True, rep=50):
    time_record = []
    i = 0
    try:
        for i in range(rep):
            print('Running test {} of {}'.format(i+1, rep))
            start = time()
            x = func()
            if validator(x):
                time_record.append(time() - start)
            else:
                print('Test failed!')
    except KeyboardInterrupt:
        pass

    print('Success {} of {}'.format(len(time_record), i+1))
    if len(time_record) > 0:
        average = sum(time_record)/len(time_record)
        if isinstance(func, partial):
            function_name = func.func.__qualname__
        elif callable(func):
            function_name = func.__qualname__
        else:
            function_name = ''
        print('{:.4f} seconds per {}'.format(average, function_name))

    return time_record


def success_rate(func, validator=lambda x: x, rep=50):
    return timeit(func, validator=validator, rep=rep)

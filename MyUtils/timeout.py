import signal


def timeout_function(func, args=(), kwargs=None, timeout_duration=20, default=None):
    """
    This function is OS-specific, however. Usable only in OSX/Linux/Unix-based.

    :param func:
    :param args:
    :param dict kwargs:
    :param timeout_duration:
    :param default:
    :return:
    """
    class MyTimeoutError(TimeoutError):
        pass

    def handler(signum, frame):
        raise MyTimeoutError

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except MyTimeoutError:
        result = default
    finally:
        signal.alarm(0)

    return result

import requests
from time import time


def get_timeout(url, local_function=None, timeout=5, wait_for_download=False, verify_function=None, encoding='utf-8'):
    data = None
    try:
        start = time()
        with requests.get(url, stream=True, timeout=timeout) as r:
            r.raise_for_status()
            content = bytes()
            content_gen = r.iter_content(1024)
            while True:
                if wait_for_download:
                    if time() - start > timeout:
                        raise TimeoutError('Time out! ({} seconds)'.format(timeout))
                try:
                    content += next(content_gen)
                except StopIteration:
                    break
            data = content.decode(encoding)
            if verify_function:
                if not verify_function(data):
                    raise ValueError('Bad requests data')
    except (requests.exceptions.RequestException, ValueError, TimeoutError) as e:
        print(e)
        if local_function:
            data = local_function()

    return data

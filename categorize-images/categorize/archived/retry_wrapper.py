import functools
import time

def retry(retry_count=5, delay=5, allowed_exceptions=()):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(retry_count):
                # everything in here would be the same
                try:
                    result = f(*args, **kwargs)
                    if result: return result
                except allowed_exceptions as e:
                    print(e)
                    time.sleep(delay)
        return wrapper
    return decorator

import random

@retry(retry_count=5, delay=5, allowed_exceptions=ValueError)
def testing_retry(divisor):
    number = random.randint(1,101)
    if number % divisor == 0:
        print(str(number) + " is divisible by " + str(divisor))
        return True
    else:
        print(str(number) + " is NOT divisible by " + str(divisor))
        raise ValueError('number is not divisble by:' + str(divisor))

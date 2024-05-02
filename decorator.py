from timeit import default_timer as timer

def timed(func):
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

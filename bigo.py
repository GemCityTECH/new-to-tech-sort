import time
from decorator import timed

def expensive_operation():
    time.sleep(0.001)

@timed
def constant_time(n):
    expensive_operation()

@timed
def linear_time(n):
    for i in range(0,n):
        expensive_operation()

@timed
def logarithmic_time(n):
    i = n
    while i > 1:
        expensive_operation()
        i //= 2

@timed
def quadratic_time(n):
    for i in range(0,n):
        for j in range(0,n):
            expensive_operation()

@timed
def cubic_time(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                expensive_operation()

@timed
def exponential_time(n):
    exponential_time_inner(n)

def exponential_time_inner(n):
    if n <= 1:
        return n
    expensive_operation()
    return exponential_time_inner(n-1) + exponential_time_inner(n-2)

@timed
def log_linear_time(n):
    for i in range(n):
        m = i
        while m > 1:
            expensive_operation()
            m //= 2

from generators import generate_dlids, generate_numbers
from sort import bubbleSort, quickSort_wrapper, selectionSort, timSort
from bigo import constant_time, linear_time, logarithmic_time, quadratic_time, exponential_time, cubic_time, log_linear_time

def compare_worst_best_case(n):
    arr = generate_numbers(n)
    sorted_arr = sorted(arr.copy())
    reverse_sorted_arr = sorted_arr.copy()
    reverse_sorted_arr.reverse()
    print("Standard case:")
    bubbleSort(arr)
    print("Best case:")
    bubbleSort(sorted_arr)
    print("Worst case:")
    bubbleSort(reverse_sorted_arr)

def compare_algorithms(n):
    arr = generate_numbers(n)
    bubbleSort(arr.copy())
    selectionSort(arr.copy(), n)
    quickSort_wrapper(arr.copy(), 0, n-1)
    timSort(arr.copy())

def compare_algorithms_alphanumeric(n):
    arr = generate_dlids(n)
    bubbleSort(arr.copy())
    selectionSort(arr.copy(), n)
    quickSort_wrapper(arr.copy(), 0, n-1)
    timSort(arr.copy())

# Suggest no more than 20!
def compare_bigo(n):
    constant_time(n)
    logarithmic_time(n)
    linear_time(n)
    log_linear_time(n)
    quadratic_time(n)
    cubic_time(n)
    exponential_time(n)
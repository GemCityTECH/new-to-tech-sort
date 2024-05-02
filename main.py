from generators import generate_dlids, generate_numbers
from sort import bubbleSort, quickSort_wrapper, selectionSort, timSort

print("Here's what the random number generator produces:")
print(generate_numbers(5))
print("How long does it take to generate a million random numbers?")
generate_numbers(1000000)

print("Here's what the random drivers license number generator produces:")
print(generate_dlids(5))
print("How long does it take to generate a million random IDs?")
generate_dlids(1000000)

print("Running bubble sort on 5000 numbers")
n = 5000
bubbleSort(generate_numbers(n))

print("Running selection sort on 5000 numbers")
selectionSort(generate_numbers(n), n)

print("Running quick sort on 5000 numbers")
quickSort_wrapper(generate_numbers(n), 0, n-1)

print("Running lead sort on 5000 numbers")
timSort(generate_numbers(n))
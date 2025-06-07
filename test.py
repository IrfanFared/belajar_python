import timeit

# For loop - optimized iterator protocol
def for_loop_test():
    total = 0
    for i in range(1000000):
        total += i
    return total

# While loop equivalent
def while_loop_test():
    total = 0
    i = 0
    while i < 1000000:
        total += i
        i += 1
    return total

# Benchmark results typically show for loop 15-20% faster
for_time = timeit.timeit(for_loop_test, number=100)
while_time = timeit.timeit(while_loop_test, number=100)

print(f"For loop: {for_time:.4f}s")
print(f"While loop: {while_time:.4f}s")
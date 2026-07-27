fib = [1, 2]
evens = [2]

while True:
    next_fib = fib[-1] + fib[-2]
    if next_fib >= 4000000:
        break
    else:
        fib.append(next_fib)
        if next_fib % 2 ==0:
            evens.append(next_fib)

total = sum(evens)
print(total)
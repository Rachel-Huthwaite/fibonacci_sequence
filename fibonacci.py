def fibonacci_sequence(n):
    if n in [1,2]:
        return 1
    
    return fibonacci_sequence (n-1) + fibonacci_sequence (n-2)

for i in range(1,10):
    print(fibonacci_sequence(i))


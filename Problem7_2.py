def fibonacci_sequence(n):
   #Input Phase
    a, b = 1, 1


    print(f"Fibonacci Sequence (first {n} numbers):")
    print(a)  
    print(b) 

#Process phase
    for _ in range(2, n):
        next_number = a + b
        print(next_number)
        a, b = b, next_number  

#Output phase
fibonacci_sequence(20)
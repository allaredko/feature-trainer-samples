for n in range(1, 100):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial of ", n, "is: ")
    print(fact, "\n")


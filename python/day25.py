def fib():
    n = int(input("Enter positive integer: "))
    t = [0, 1]
    if n > 1:
        for i in range(2, n+1):
            t.append(t[i - 1] + t[i - 2])
    print(t)

fib()
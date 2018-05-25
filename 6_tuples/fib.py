# 1 1 2 3 5 8 13 ...
# fib(3) -> 2
# fib(5) -> 5

def fib(n):
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a+b # 這次的a等於上次的b，這次的b等於上次的a+b
    return b

print(fib(3))
print(fib(5))
print(fib(7))